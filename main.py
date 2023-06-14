import pygame
import time
import random

# Inicjalizacja modułu Pygame
pygame.init()

# Ustawienia okna gry
okno_szerokosc = 800
okno_wysokosc = 600
plansza_rozmiar = 20
ekran = pygame.display.set_mode((okno_szerokosc, okno_wysokosc))
pygame.display.set_caption("Snake Game")

# Kolory
kolor_tla = (0, 0, 0)
kolor_glowa = (0, 255, 0)
kolor_cialo = (0, 200, 0)
kolor_jedzenie = (255, 0, 0)

# Czas opóźnienia
opoznienie = 0.1

# Wartości początkowe dla węża
waz_pocz_x = okno_szerokosc // 2
waz_pocz_y = okno_wysokosc // 2
waz_rozmiar = 1
waz_x = [waz_pocz_x]
waz_y = [waz_pocz_y]
kierunek = 0  # 0 - góra, 1 - prawo, 2 - dół, 3 - lewo

# Generowanie początkowego położenia jedzenia
jedzenie_x = round(random.randrange(0, okno_szerokosc - plansza_rozmiar) / plansza_rozmiar) * plansza_rozmiar
jedzenie_y = round(random.randrange(0, okno_wysokosc - plansza_rozmiar) / plansza_rozmiar) * plansza_rozmiar

# Punkty
punkty = 0

# Główna pętla gry
koniec_gry = False
while not koniec_gry:
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            koniec_gry = True

        # Obsługa ruchu węża
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_UP] and kierunek != 2:
                kierunek = 0
            elif keys[pygame.K_RIGHT] and kierunek != 3:
                kierunek = 1
            elif keys[pygame.K_DOWN] and kierunek != 0:
                kierunek = 2
            elif keys[pygame.K_LEFT] and kierunek != 1:
                kierunek = 3

    # Aktualizacja położenia węża
    if kierunek == 0:
        waz_pocz_y -= plansza_rozmiar
    elif kierunek == 1:
        waz_pocz_x += plansza_rozmiar
    elif kierunek == 2:
        waz_pocz_y += plansza_rozmiar
    elif kierunek == 3:
        waz_pocz_x -= plansza_rozmiar

    # Aktualizacja położenia głowy węża
    waz_x.append(waz_pocz_x)
    waz_y.append(waz_pocz_y)

    # Usunięcie ostatniego segmentu węża, jeśli przekracza jego rozmiar
    if len(waz_x) > waz_rozmiar:
        del waz_x[0]
        del waz_y[0]

    if waz_pocz_x == jedzenie_x and waz_pocz_y == jedzenie_y:
        jedzenie_x = round(random.randrange(0, okno_szerokosc - plansza_rozmiar) / plansza_rozmiar) * plansza_rozmiar
        jedzenie_y = round(random.randrange(0, okno_wysokosc - plansza_rozmiar) / plansza_rozmiar) * plansza_rozmiar
        waz_rozmiar += 1
        punkty += 1

    if waz_pocz_x >= okno_szerokosc or waz_pocz_x < 0 or waz_pocz_y >= okno_wysokosc or waz_pocz_y < 0:
        koniec_gry = True

    if (waz_pocz_x, waz_pocz_y) in zip(waz_x[:-1], waz_y[:-1]):
        koniec_gry = True

    ekran.fill(kolor_tla)

    for i in range(len(waz_x)):
        pygame.draw.rect(ekran, kolor_cialo, (waz_x[i], waz_y[i], plansza_rozmiar, plansza_rozmiar))

    pygame.draw.rect(ekran, kolor_jedzenie, (jedzenie_x, jedzenie_y, plansza_rozmiar, plansza_rozmiar))

    pygame.display.update()

    time.sleep(opoznienie)

print("Koniec gry! Uzyskano", punkty, "punktów.")

pygame.quit()
