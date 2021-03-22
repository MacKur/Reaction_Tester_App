import pygame
import random
import time

# Konfiguracja programu i informacje o teście
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Test koordynacji")
font = pygame.font.SysFont('Times New Roman', 24)

# Załadowanie pliku dźwiękowego
metal_sound = pygame.mixer.Sound('metalHit.wav')

# Kolory RGB
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Przechowywanie danych testu
running = True
eliminated = True
react_time_start = 0
react_time = 0
sample = 0
coord_reaction_lst = []

# Konfiguracja startowych parametrów celu
width = 50
height = 50
rand_x = (screen_width // 2) - width // 2
rand_y = (screen_height // 2) - height // 2


def save_results(file, lst):        # Funkcja umożliwiająca zapis czasów reakcji użytkownika do pliku tekstowego
    f = open(file, 'a')
    for n in lst:
        f.write(str(n) + ' ')
    f.close()


def draw_text(text, font, color, surface, x, y):        # Funkcja umożliwiająca umieszczanie tekstu w oknie programu
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


def draw_screen(react_t, x, y):
    global react_time_start, eliminated

    # Wypełnienie pustego tła w każdej klatce programu
    screen.fill(GREY)

    # Rysowanie ramy w której wyświetlany będzie cel
    pygame.draw.rect(screen, BLACK, (200, 100, 400, 400), 10)

    # Wyświetlanie czasu reakcji w czasie rzeczywistym w oknie programu
    draw_text("Reaction Time: " + str(react_t) + " ms", font, BLACK, screen, 400, 20)

    # Rysowanie czerwonego kwadratu będącego celem
    pygame.draw.rect(screen, RED, (x, y, 50, 50))

    # Śledzenie długości czasu przez który cel był wyświetlony na ekranie przed eliminacją
    if eliminated:
        react_time_start = time.time()
        eliminated = False


while running:
    pygame.time.delay(5)

    for event in pygame.event.get():
        # Sprawdzanie czy użytkownik nie chce opuścić programu, jeśli tak powrót do głównego menu
        if event.type == pygame.QUIT:
            running = False
            exec(open("Main.py").read())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                exec(open("Main.py").read())

        # Śledzenie położenia kursora myszy i sprawdzanie czy lpm został naciśnięty w obrębie kształtu celu
        mx, my = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rand_x <= mx <= rand_x + width and rand_y <= my <= rand_y + height:
                    if sample < 29:
                        sample += 1
                        eliminated = True
                        metal_sound.play()

                        # Obliczenie i zapis czasu reakcji
                        react_time = round((time.time() - react_time_start), 3)
                        coord_reaction_lst.append(react_time)

                        # Losowanie pozycji następnego celu wyświetlonego po eliminacji bieżącego
                        rand_x = random.randint(205, 545)
                        rand_y = random.randint(105, 445)
                    else:
                        running = False
                        # Zapisanie listy zawierającej wszystkie czasy reakcji z danego testu do pliku tekstowego
                        save_results('Coord_reaction_results.txt', coord_reaction_lst)
                        exec(open("Main.py").read())

    # Rysuj i odświeżaj w każdym cyklu
    draw_screen(react_time, rand_x, rand_y)
    pygame.display.update()

pygame.quit()
exec(open("Main.py").read())
