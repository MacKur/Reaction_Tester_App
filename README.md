# Reaction_Tester_App

## Cel Projektu

Napisanie aplikacji uzależnionej od czasu. Jednym z zadań aplikacji ma być możliwie precyzyjny pomiar lub odmierzanie czasu. Wykorzystując dowolny język programowanie dla komputerów w standardzie PC napisać aplikację spełniającą funkcję testera sprawności psychomotorycznej np. kandydatów na kierowców. Na aplikację powinna się składać seria różnych testów badających prosty i złożony czas reakcji na bodźce optyczne i akustyczne. Każdy test właściwy powinna poprzedzać informacja o przebiegu testu oraz faza szkoleniowa, w trakcie której osoba badana wykona te same czynności co w trakcie testu, ale bez oceny. Po wykonaniu serii testów osoba poddana badaniom powinna zostać poinformowana o osiągniętych wynikach.

## Realizacja

Program został zrealizowany z wykorzystaniem języka Python 3.7 w środowisku PyCharm Community Edition 2019.3.4 x64.

Stworzono aplikację umożliwiającą sprawdzenie zdolności szybkiej reakcji użytkownika na bodźce wzrokowe i słuchowe w połączeniu testem sprawności manualnej. Poszczególne testy zostały zrealizowane w postaci mini gier wykorzystując moduł pygame.

W programie wykorzystano moduły zewnętrzne:
- pygame 1.9.6
- numpy 1.18.2
- matplotlib 3.2.1
- opencv-python 4.2.0.32

Na program składają się 2 skrypty Main.py oraz CoordinationTest.py, kolejno są to menu główne zawierające większość funkcjonalności i osobny skrypt odpowiadający za test koordynacji ręka-oko. Decyzja odnośnie takiego rozwiązania została podjęta w celu utrzymania właściwej składni programu.

Program posiada menu główne z poziomu którego użytkownik ma możliwość przejścia do poszczególnych funkcji programu takich jak przejście wersji szkoleniowych poszczególnych testów, właściwe testy z pomiarami czasu reakcji oraz wgląd do wyników w postaci wykresów. 

Opis przyjętych rozwiązań w głównej mierze został stworzony w postaci komentarzy wewnątrz kodu. 

W programie każdy z testów napisany został jako odrębna funkcja wywoływana po wybraniu konkretnego testu przez użytkownika za pomocą przycisku w menu głównym. 

<img src="https://raw.githubusercontent.com/MacKur/Reaction_Tester_App/main/Program.png" width="800" height="504">

## Test Wzroku
Program w czasie rzeczywistym losuje czas oczekiwania pomiędzy interakcjami oraz rodzaj wyświetlanego przycisku (z wcześniej przygotowanych list) którego wciśnięcie przez użytkownika zatrzyma zegar odliczający czas reakcji. Ten natomiast w chwili naciśnięcia przez użytkownika przycisku, wyświetlanego na ekranie, zapisany tymczasowo do listy z której po zakończeniu testu zostaje dopisany do pliku tekstowego, skąd może zostać pobrany w celu wizualizacji wyników.

<img src="https://raw.githubusercontent.com/MacKur/Reaction_Tester_App/main/Test_Wzroku.png" width="800" height="504">

## Test Słuchu
Program w losowo określonych odstępach czasu odtwarza dźwięk klaksonu, zadaniem użytkownika jest jak najszybsza reakcja, czyli w tym przypadku naciśnięcie klawisza spacji, co skutkuje zerwaniem pętli oczekiwania na poprawną interakcję ze strony użytkownika oraz zapisaniem czasu po którym powyższa interakcja nastąpiła, analogicznie do poprzedniego testu, czas dopisywany jest do listy każdorazowo po wykonaniu się pętli, zaś po 10-krotnym wykonaniu się procedury pomiaru lista wyników zostaje zapisana w pliku tekstowym.

<img src="https://raw.githubusercontent.com/MacKur/Reaction_Tester_App/main/Test_S%C5%82uchu.png" width="800" height="504">

## Test Koordynacji
Program uruchamia osobny skrypt CoordinationTest.py po otwarciu okna programu czas w mini grze zaczyna upływać zgodnie z zegarem, w czasie rzeczywistym śledzone jest położenie kursora myszy i sprawdzane jest czy miała miejsce interakcja w postaci naciśnięcia przez użytkownika lewego przycisku myszy w polu celu, tj. czerwonego prostokąta losowo pojawiającego się wewnątrz otoczonego ramką obszaru. Gdy program wykryje, iż użytkownik poprawnie wykonał interakcję, obliczany oraz zapisywany jest czas reakcji od momentu pojawienia się celu na ekranie, losowana jest kolejna pozycja celu i finalnie odświeżany jest ekran. Po 30-krotnym wykonaniu procedury pomiaru program zapisuje wyniki do pliku tekstowego tak jak w przypadku poprzednich testów i powraca do menu głównego. 

<img src="https://raw.githubusercontent.com/MacKur/Reaction_Tester_App/main/movie.gif">
