import pygame
import sys
from gracz import Gracz


class Gra(object):

    def __init__(self):
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        # Konfiguracja
        # szybkosc w ruchach na sekundę
        self.szybkosc = 800.0

        # inicjalizacja
        pygame.init()
        # Wyświetlanie okna
        self.okno = pygame.display.set_mode((1200, 600))
        self.zegar = pygame.time.Clock()
        self.zmiana = 0.0
        self.gracz = Gracz(self)
        while True:
            # Obsługa zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.gracz.start()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                    self.gracz.sprawdzenie_menu = True
                    self.gracz.paletka1 = pygame.image.load("paletka.jpg")
                    self.gracz.paletka2 = pygame.image.load("paletka.jpg")
                    self.gracz.kulka1 = pygame.image.load("kulka.jpg")
            # Szybkość klatek
            self.zmiana += self.zegar.tick() / 1000.0
            while self.zmiana > 1 / self.szybkosc:
                self.zmiana -= 1 / self.szybkosc
                self.przyciski()
            # Rysowanie
            self.menu()
            self.skorki()
            self.okno.fill((0, 0, 0))
            self.rysowanie()
            pygame.display.update()

    def przyciski(self):
        self.gracz.przyciski()

    def rysowanie(self):
        self.gracz.rysowanie()

    def menu(self):
        self.gracz.menu()

    def skorki(self):
        self.gracz.skorki()


if __name__ == "__main__":
    Gra()

