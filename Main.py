import random
import sys
import time

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pygame
from numpy import genfromtxt
from pygame.locals import *

# Konfiguracja programu
pygame.init()
window_w = 1000
window_h = 600
screen = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption('Test sprawnosci psychomotorycznej')
font = pygame.font.SysFont("Times New Roman", 28)

# Kolory RGB
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

text_1 = "Test sprawności psychomotorycznej"
text_2 = "Z poniższego menu wybierz co chcesz zrobić"
text_3 = "Postępuj zgodnie z instrukcjami wyświetlającymi się na ekranie"
text_4 = "Wersja szkoleniowa - wzrok"
text_5 = "Wersja szkoleniowa - słuch"
text_6 = "Wersja szkoleniowa - koordynacja"
text_7 = "Test Wzroku"
text_8 = "Test Słuchu"
text_9 = "Test Koordynacji"
text_10 = "Naciskaj na swojej klawiaturze przyciski kolejno wyświetlające się na ekranie"
text_11 = "Naciskaj spację gdy usłyszysz sygnał dźwiękowy"
text_12 = "Na twoim ekranie pojawiło się nagranie video obrazujące przebieg testu"
text_13 = "W trakcie testu staraj się jak najszybciej klikać na pojawiające się kwadraty"
text_14 = "Używaj lewego przycisku myszy, w trakcie testu cel pojawi się 30-krotnie"
text_15 = "Wyniki"
text_16 = "W trakcie właściwego testu czynność powtórzy się 10-krotnie"
text_17 = "Czyść"
text_18 = "Szkolenie"

# Stworzenie list przechowujących czasy reakcji w poszczególnych testach
vision_reaction_lst = []
sound_reaction_lst = []

# Załadowanie plików dźwiękowych, grafik oraz nagrań wykorzystywanych w aplikacji
horn_sound = pygame.mixer.Sound('horn_sound.wav')
mov = cv2.VideoCapture('movie.mp4')
img_1 = pygame.image.load(r'C:\Users\Maciej\PycharmProjects\ASK\keyboard_1.PNG')
img_1_width = img_1.get_width()
img_2 = pygame.image.load(r'C:\Users\Maciej\PycharmProjects\ASK\keyboard_2.PNG')
img_2_width = img_2.get_width()


def save_results(file, lst):  # Funkcja umożliwiająca zapis czasów reakcji użytkownika do pliku tekstowego
    f = open(file, 'a')
    for n in lst:
        f.write(str(n) + ' ')
    f.close()


def erase_file(file):  # Funkcja umożliwiająca czyszczenie plików tekstowych zawierających czasy reakcji
    f = open(file, 'r+')
    f.truncate(0)
    f.close()


def draw_text(text, font, color, surface, x, y):  # Funkcja umożliwiająca umieszczanie tekstu w oknie programu
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


def show_result(lst):  # Funkcja umożliwiająca reprezentację graficzną wyników testów
    x_axis = np.arange(1, len(lst) + 1, 1)
    plt.figure('Wyniki')
    plt.xlabel('Numer próbki')
    plt.ylabel('Czas reakcji [ms]')
    plt.bar(x_axis, lst, align='center', alpha=1)
    plt.grid(True)
    plt.show()


def training():  # Tryb szkoleniowy testów: wzrokowego oraz słuchowego
    running = True
    while running:
        # ----------------------- SZKOLENIE - WZROK --------------------------------
        # Wypełnienie tła okna programu, dodanie napisów oraz grafiki instruktażowej
        screen.fill(GREY)
        draw_text(text_4, font, BLACK, screen, window_w / 2, 40)
        draw_text(text_10, font, BLACK, screen, window_w / 2, 100)
        screen.blit(img_1, ((window_w - img_1_width) / 2, 160))
        draw_text(text_16, font, BLACK, screen, window_w / 2, 500)

        # Aktualizacja okna programu oraz 8 sekund pauzy dla użytkownika na zapoznanie się z instrukcjami
        pygame.display.update()
        time.sleep(8)

        for _ in range(3):
            screen.fill(GREY)
            pygame.display.update()

            # Zmienna losowa - czas oczekiwania pomiędzy powtórzeniami 1-3 [s]
            wait = random.randint(1, 3)
            time.sleep(wait)

            # Zmienna losowa - decydująca o rodzaju klawisza wyświetlonego na ekranie w trakcie szkolenia
            rnd_button = random.randint(0, 7)

            # Rozmiar prostokąta imitującego przycisk
            rect_w = 50
            rect_h = 50

            # Listy określające rodzaj wyświetlanego klawisza oraz klawisza do naciśnięcia
            button = [pygame.K_q, pygame.K_z, pygame.K_e, pygame.K_c, pygame.K_t, pygame.K_b, pygame.K_u, pygame.K_m]
            button_txt = ['Q', 'Z', 'E', 'C', 'T', 'B', 'U', 'M']

            # Stworzenie prostokąta imitującego przycisk oraz wyświetlenie go razem z symbolem przycisku
            game_button = pygame.Rect((window_w - rect_w) / 2, (window_h - rect_h) / 2, rect_w, rect_h)
            pygame.draw.rect(screen, BLACK, game_button)
            draw_text(button_txt[rnd_button], font, GREY, screen, game_button.centerx, game_button.centery)

            # Aktualizacja okna programu - wyświetlenie przycisku
            pygame.display.update()

            # Oczekiwanie na przyciśnięcie odpowiedniego klawisza
            game_running = True
            while game_running:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == button[rnd_button]:
                            game_running = False

        # ----------------------- SZKOLENIE - SŁUCH --------------------------------
        # Wypełnienie tła okna programu, wyświetlenie go oraz sekundowa pauza pomiędzy szkoleniami
        screen.fill(GREY)
        pygame.display.update()
        time.sleep(1)
        # Dodanie napisów oraz grafiki instruktażowej
        draw_text(text_5, font, BLACK, screen, window_w / 2, 40)
        draw_text(text_11, font, BLACK, screen, window_w / 2, 100)
        screen.blit(img_2, ((window_w - img_2_width) / 2, 160))
        draw_text(text_16, font, BLACK, screen, window_w / 2, 500)

        # Aktualizacja okna programu oraz 8 sekund pauzy dla użytkownika na zapoznanie się z instrukcjami
        pygame.display.update()
        time.sleep(8)

        for _ in range(3):
            # Zmienna losowa - czas oczekiwania pomiędzy powtórzeniami 2-4 [s]
            wait = random.randint(2, 4)
            time.sleep(wait)

            # Odtwórz dźwięk
            horn_sound.play()

            # Oczekiwanie na przyciśnięcie spacji
            game_running = True
            while game_running:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            game_running = False

        running = False

    pygame.display.update()


def coord_training():  # Wersja szkoleniowa testu koordynacji w postaci instrukcji tekstowej oraz nagrania wideo
    while mov.isOpened():
        screen.fill(GREY)
        draw_text(text_9, font, BLACK, screen, window_w / 2, 40)
        draw_text(text_12, font, BLACK, screen, window_w / 2, 100)
        draw_text(text_13, font, BLACK, screen, window_w / 2, 160)
        draw_text(text_14, font, BLACK, screen, window_w / 2, 220)

        pygame.display.update()

        # Przechwytywanie klatka po klatce
        ret, frame = mov.read()
        if ret:
            # Wyświetlanie wynikowej ramki
            cv2.imshow('Frame', frame)

            # Wyjście przyciskiem 'q'
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Zerwanie pętli
        else:
            break

    # Po odtworzeniu filmu, uwolnienie
    mov.release()

    # Zamknięcie wszystkich ramek
    cv2.destroyAllWindows()


def vision_reaction_test():  # Właściwy test wzroku
    running = True
    while running:
        # Wypełnienie tła okna programu, dodanie napisów oraz grafiki instruktażowej
        screen.fill(GREY)
        draw_text(text_7, font, BLACK, screen, window_w / 2, 40)
        draw_text(text_10, font, BLACK, screen, window_w / 2, 100)
        screen.blit(img_1, ((window_w - img_1_width) / 2, 160))

        # Aktualizacja okna programu oraz 8 sekund pauzy dla użytkownika w celu przypomnienia instrukcji
        pygame.display.update()
        time.sleep(8)

        # Wyczyszczenie ekranu
        screen.fill(GREY)
        pygame.display.update()

        for _ in range(10):
            pygame.display.update()

            # Zmienna losowa - czas oczekiwania pomiędzy powtórzeniami 1-3 [s]
            wait = random.randint(1, 3)
            time.sleep(wait)

            # Zmienna losowa - decydująca o rodzaju klawisza wyświetlonego na ekranie w trakcie testu
            rnd_button = random.randint(0, 7)

            # Rozmiar prostokąta imitującego przycisk
            rect_w = 50
            rect_h = 50

            # Listy określające rodzaj wyświetlanego klawisza oraz klawisza do naciśnięcia
            button = [pygame.K_q, pygame.K_z, pygame.K_e, pygame.K_c, pygame.K_t, pygame.K_b, pygame.K_u, pygame.K_m]
            button_txt = ['Q', 'Z', 'E', 'C', 'T', 'B', 'U', 'M']

            # Stworzenie prostokąta imitującego przycisk oraz wyświetlenie go razem z symbolem przycisku
            pygame.draw.rect(screen, BLACK, ((window_w - rect_w) / 2, (window_h - rect_h) / 2, rect_w, rect_h))
            txt = font.render(button_txt[rnd_button], 0, GREY)
            txt_pos = txt.get_rect(center=screen.get_rect().center)
            screen.blit(txt, txt_pos)

            # Rozpoczęcie odliczania czasu reakcji użytkownika na wyświetlenie przycisku
            reaction_start = time.time()

            # Aktualizacja okna programu - wyświetlenie przycisku
            pygame.display.update()

            # Oczekiwanie na przyciśnięcie odpowiedniego klawisza i po otrzymaniu kliknięcia zatrzymanie czasu
            game_running = True
            while game_running:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == button[rnd_button]:
                            reaction_time = round((time.time() - reaction_start), 3)
                            if reaction_start != time.time():
                                game_running = False

            # Zapisanie czasu reakcji
            vision_reaction_lst.append(reaction_time)

            # Wyświelenie czasu reakcji w czasie rzeczywistym w oknie programu
            screen.fill(GREY)
            draw_text("Reaction Time: " + str(reaction_time) + " ms", font, BLACK, screen, 500, 60)

        running = False

        # Zapisanie listy zawierającej wszystkie czasy reakcji z danego testu do pliku tekstowego
        save_results('Vision_reaction_results.txt', vision_reaction_lst)

    pygame.display.update()


def sound_reaction_test():  # Właściwy test słuchu
    running = True
    while running:
        # Wypełnienie tła okna programu, dodanie napisów oraz grafiki instruktażowej
        screen.fill(GREY)
        draw_text(text_8, font, BLACK, screen, window_w / 2, 40)
        draw_text(text_11, font, BLACK, screen, window_w / 2, 100)
        screen.blit(img_2, ((window_w - img_2_width) / 2, 160))

        # Aktualizacja okna programu oraz 8 sekund pauzy dla użytkownika w celu przypomnienia instrukcji
        pygame.display.update()
        time.sleep(8)

        for _ in range(10):
            screen.fill(GREY)
            # Zmienna losowa - czas oczekiwania pomiędzy powtórzeniami 2-4 [s]
            wait = random.randint(2, 4)
            time.sleep(wait)

            # Rozpoczęcie odliczania czasu reakcji użytkownika na wyświetlenie przycisku
            reaction_start = time.time()

            # Odtwórz dźwięk
            horn_sound.play()

            # Oczekiwanie na przyciśnięcie spacji i po otrzymaniu kliknięcia zatrzymanie czasu
            game_running = True
            while game_running:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            reaction_time = round((time.time() - reaction_start), 3)
                            if reaction_start != time.time():
                                game_running = False

            # Zapisanie czasu reakcji
            sound_reaction_lst.append(reaction_time)

            # Wyświelenie czasu reakcji w czasie rzeczywistym w oknie programu
            draw_text("Reaction Time: " + str(reaction_time) + " ms", font, BLACK, screen, 500, 60)
            pygame.display.update()

        running = False

        # Zapisanie listy zawierającej wszystkie czasy reakcji z danego testu do pliku tekstowego
        save_results('Sound_reaction_results.txt', sound_reaction_lst)

    pygame.display.update()


def main_menu():  # Główne menu programu,
    click_menu = False
    while True:
        # Wypełnienie tła okna programu
        screen.fill(GREY)

        # Dodanie napisów
        draw_text(text_1, font, BLACK, screen, window_w / 2, 40)
        draw_text(text_2, font, BLACK, screen, window_w / 2, 100)
        draw_text(text_3, font, BLACK, screen, window_w / 2, 160)

        # Pobranie pozycji myszy w oknie programu
        mx, my = pygame.mouse.get_pos()

        # Stworzenie przycisków wyświetlanych w głównym menu programu
        menu_button_1 = pygame.draw.rect(screen, BLACK, (250, 250, 200, 50))
        menu_button_2 = pygame.draw.rect(screen, BLACK, (700, 250, 200, 50))
        menu_button_3 = pygame.draw.rect(screen, BLACK, (100, 340, 200, 50))
        menu_button_4 = pygame.draw.rect(screen, BLACK, (400, 340, 200, 50))
        menu_button_5 = pygame.draw.rect(screen, BLACK, (700, 340, 200, 50))
        menu_button_6 = pygame.draw.rect(screen, BLACK, (100, 430, 200, 50))
        menu_button_7 = pygame.draw.rect(screen, BLACK, (400, 430, 200, 50))
        menu_button_8 = pygame.draw.rect(screen, BLACK, (700, 430, 200, 50))
        menu_button_9 = pygame.draw.rect(screen, BLACK, (150, 520, 100, 50))
        menu_button_10 = pygame.draw.rect(screen, BLACK, (450, 520, 100, 50))
        menu_button_11 = pygame.draw.rect(screen, BLACK, (750, 520, 100, 50))

        # Zdefiniowanie funkcjonalności wszystkich wyświetlanych przycisków w zależności od przeznaczenia
        if menu_button_1.collidepoint(mx, my):
            if click_menu:
                training()
        if menu_button_2.collidepoint(mx, my):
            if click_menu:
                coord_training()
        if menu_button_3.collidepoint(mx, my):
            if click_menu:
                vision_reaction_test()
        if menu_button_4.collidepoint(mx, my):
            if click_menu:
                sound_reaction_test()
        if menu_button_5.collidepoint(mx, my):
            if click_menu:
                # Odpalenie skryptu testu koordynacji w osobnym oknie
                exec(open("CoordinationTest.py").read())
        if menu_button_6.collidepoint(mx, my):
            if click_menu:
                vision_reaction = genfromtxt('Vision_reaction_results.txt', delimiter=' ')
                show_result(vision_reaction)
        if menu_button_7.collidepoint(mx, my):
            if click_menu:
                sound_reaction = genfromtxt('Sound_reaction_results.txt', delimiter=' ')
                show_result(sound_reaction)
        if menu_button_8.collidepoint(mx, my):
            if click_menu:
                coordination_reaction = genfromtxt('Coord_reaction_results.txt', delimiter=' ')
                show_result(coordination_reaction)
        if menu_button_9.collidepoint(mx, my):
            if click_menu:
                erase_file('Vision_reaction_results.txt')
        if menu_button_10.collidepoint(mx, my):
            if click_menu:
                erase_file('Sound_reaction_results.txt')
        if menu_button_11.collidepoint(mx, my):
            if click_menu:
                erase_file('Coord_reaction_results.txt')

        # Opisanie wszystkich przycisków znajdujących się w menu głównym (określenie czcionki, koloru i położenia)
        draw_text(text_18, font, GREY, screen, menu_button_1.centerx, menu_button_1.centery)
        draw_text(text_18, font, GREY, screen, menu_button_2.centerx, menu_button_2.centery)
        draw_text(text_7, font, GREY, screen, menu_button_3.centerx, menu_button_3.centery)
        draw_text(text_8, font, GREY, screen, menu_button_4.centerx, menu_button_4.centery)
        draw_text(text_9, font, GREY, screen, menu_button_5.centerx, menu_button_5.centery)
        draw_text(text_15, font, GREY, screen, menu_button_6.centerx, menu_button_6.centery)
        draw_text(text_15, font, GREY, screen, menu_button_7.centerx, menu_button_7.centery)
        draw_text(text_15, font, GREY, screen, menu_button_8.centerx, menu_button_8.centery)
        draw_text(text_17, font, GREY, screen, menu_button_9.centerx, menu_button_9.centery)
        draw_text(text_17, font, GREY, screen, menu_button_10.centerx, menu_button_10.centery)
        draw_text(text_17, font, GREY, screen, menu_button_11.centerx, menu_button_11.centery)

        click_menu = False
        # Oczekiwanie na interakcję użytkownika przy użyciu myszy, klawiszy służących opuszczeniu programu (esc) (x)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_menu = True

        pygame.display.update()


main_menu()
