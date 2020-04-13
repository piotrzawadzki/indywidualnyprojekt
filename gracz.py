import pygame
from pygame.math import Vector2
import random
import sys


class Gracz(object):

    def __init__(self, gra):
        self.gra = gra
        self.promien_kulki = 10
        self.wielkosc_okna = self.gra.okno.get_size()
        self.pozycja_paletki1 = Vector2(0, 250)
        self.pozycja_paletki2 = Vector2(0, 250)
        self.pozycja_kulki = Vector2(self.wielkosc_okna[0] / 2, self.wielkosc_okna[1] / 2)
        self.predkosc = Vector2(0, 0)
        self.przyspieszenie = Vector2(0, 0)
        self.czcionka = pygame.font.SysFont("Times New Roman, Arial", 60)
        self.czcionka1 = pygame.font.SysFont("Times New Roman, Arial", 50)
        self.czcionka2 = pygame.font.SysFont("Times New Roman, Arial", 30)
        self.czcionka3 = pygame.font.SysFont("Times New Roman, Arial", 200)
        self.tekst1 = 0
        self.tekst2 = 0
        self.paletka1 = pygame.image.load("paletka.jpg")
        self.paletka2 = pygame.image.load("paletka.jpg")
        self.kulka1 = pygame.image.load("kulka.jpg")
        self.dzwiek_pilki = pygame.mixer.Sound("dzwiekpilki.wav")
        self.dzwiek_punktu = pygame.mixer.Sound("dzwiekpunktu.wav")
        self.sprawdzenie_menu = True
        self.komputer = False
        self.trudnosc = 0
        self.start1 = 0
        self.zmianamuzyki = 1
        self.polozenieinfo = 120
        self.sprawdzenie_skorki = False

    def przyciski(self):
        # Poruszanie
        przyciski = pygame.key.get_pressed()
        if przyciski[pygame.K_w]:
            if self.pozycja_paletki1.y != 0:
                self.pozycja_paletki1.y -= 1
            else:
                self.pozycja_paletki1.y -= 0
        if przyciski[pygame.K_s]:
            if self.pozycja_paletki1.y != self.wielkosc_okna[1] - 100:
                self.pozycja_paletki1.y += 1
            else:
                self.pozycja_paletki1.y += 0
        if self.komputer == False:
            if przyciski[pygame.K_UP]:
                if self.pozycja_paletki2.y != 0:
                    self.pozycja_paletki2.y -= 1
                else:
                    self.pozycja_paletki2.y -= 0
            if przyciski[pygame.K_DOWN]:
                if self.pozycja_paletki2.y != self.wielkosc_okna[1] - 100:
                    self.pozycja_paletki2.y += 1
                else:
                    self.pozycja_paletki2.y += 0
        else:
            if self.trudnosc == 0:
                if self.pozycja_paletki2.y >= self.pozycja_kulki.y - 50 >= 0:
                    self.pozycja_paletki2.y -= random.choice([-1, 1, 1])
                elif self.pozycja_paletki2.y < self.pozycja_kulki.y - 50 <= self.wielkosc_okna[1] - 100:
                    self.pozycja_paletki2.y += random.choice([-1, 1, 1])
            elif self.trudnosc == 1:
                if self.pozycja_paletki2.y >= self.pozycja_kulki.y - 50 >= 0:
                    self.pozycja_paletki2.y -= random.choice([-1, 1, 1, 1, 1, 1])
                elif self.pozycja_paletki2.y < self.pozycja_kulki.y - 50 <= self.wielkosc_okna[1] - 100:
                    self.pozycja_paletki2.y += random.choice([-1, 1, 1, 1, 1, 1])
            elif self.trudnosc == 2:
                if self.pozycja_paletki2.y >= self.pozycja_kulki.y - 50 >= 0:
                    self.pozycja_paletki2.y -= random.choice([-1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
                elif self.pozycja_paletki2.y < self.pozycja_kulki.y - 50 <= self.wielkosc_okna[1] - 100:
                    self.pozycja_paletki2.y += random.choice([-1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

        # Fizyka
        if self.pozycja_kulki.y <= self.promien_kulki:
            self.dzwiek_pilki.play()
            self.predkosc.y *= -1
        if self.pozycja_kulki.y >= self.wielkosc_okna[1] - self.promien_kulki:
            self.dzwiek_pilki.play()
            self.predkosc.y *= -1
        if self.promien_kulki + 30 - abs(
                self.predkosc.x) <= self.pozycja_kulki.x <= self.promien_kulki + 30.0 and self.pozycja_paletki1.y <= self.pozycja_kulki.y <= self.pozycja_paletki1.y + 100:
            self.dzwiek_pilki.play()
            self.predkosc.x *= -1
            self.predkosc *= 1.05
            self.predkosc.y *= random.uniform(0.9, 1.1)
        if self.wielkosc_okna[0] - self.promien_kulki - 30 + abs(self.predkosc.x) >= self.pozycja_kulki.x >= \
                self.wielkosc_okna[
                    0] - self.promien_kulki - 30.0 and self.pozycja_paletki2.y <= self.pozycja_kulki.y <= self.pozycja_paletki2.y + 100:
            self.dzwiek_pilki.play()
            self.predkosc.x *= -1
            self.predkosc *= 1.05
            self.predkosc.y *= random.uniform(0.9, 1.1)
        if self.promien_kulki - 10 <= self.pozycja_kulki.x <= self.promien_kulki:
            if self.tekst2 <= 3:
                self.tekst2 += 1
            else:
                self.tekst2 = "Wygrałeś"
            self.start1 = 0
            self.pozycja_kulki = Vector2(self.wielkosc_okna[0] / 2, self.wielkosc_okna[1] / 2)
            self.predkosc = Vector2(0, 0)
            self.przyspieszenie = Vector2(0, 0)
            self.dzwiek_punktu.play()
        if self.wielkosc_okna[0] - self.promien_kulki + 10 >= self.pozycja_kulki.x >= self.wielkosc_okna[
            0] - self.promien_kulki:
            if self.tekst1 <= 3:
                self.tekst1 += 1
            else:
                self.tekst1 = "Wygrałeś"
            self.start1 = 0
            self.pozycja_kulki = Vector2(self.wielkosc_okna[0] / 2, self.wielkosc_okna[1] / 2)
            self.predkosc = Vector2(0, 0)
            self.przyspieszenie = Vector2(0, 0)
            self.dzwiek_punktu.play()
        self.predkosc.x += self.przyspieszenie.x * 0.5
        self.predkosc.y += self.przyspieszenie.y * 0.5
        self.pozycja_kulki.x += self.predkosc.x
        self.pozycja_kulki.y += self.predkosc.y
        self.przyspieszenie *= 0

    def dodaj_moc(self, moc):
        self.przyspieszenie += moc

    def start(self):
        liczba1 = random.choice([-1, 1])
        liczba2 = random.choice([-1, 1])
        if self.start1 == 0:
            self.start1 = 1
            self.polozenieinfo += 5000
            self.dodaj_moc(Vector2(liczba1, liczba2))
            if self.tekst1 == "Wygrałeś" or self.tekst2 == "Wygrałeś":
                self.tekst1, self.tekst2 = 0, 0
        else:
            pass

    def rysowanie(self):
        kulka = (int(self.pozycja_kulki.x), int(self.pozycja_kulki.y))
        paletka1 = pygame.Rect(10, self.pozycja_paletki1.y, 20, 100)
        paletka2 = pygame.Rect(1170, self.pozycja_paletki2.y, 20, 100)
        pygame.draw.rect(self.gra.okno, (0, 0, 0), paletka1)
        pygame.draw.rect(self.gra.okno, (0, 0, 0), paletka2)
        pygame.draw.circle(self.gra.okno, (0, 0, 0), kulka, self.promien_kulki)
        punktacja = self.czcionka.render("{} : {}".format(self.tekst1, self.tekst2), True, (255, 255, 255))
        self.gra.okno.blit(punktacja, (self.wielkosc_okna[0] / 2 - punktacja.get_rect().width / 2, 50))
        self.gra.okno.blit(self.paletka1, (10, self.pozycja_paletki1.y))
        self.gra.okno.blit(self.paletka2, (1170, self.pozycja_paletki2.y))
        self.gra.okno.blit(self.kulka1, (int(self.pozycja_kulki.x) - 10, int(self.pozycja_kulki.y) - 10))
        sterowanie = self.czcionka.render("STEROWANIE", True, (255, 255, 255))
        self.gra.okno.blit(sterowanie, (self.wielkosc_okna[0] / 2 - sterowanie.get_rect().width / 2, self.polozenieinfo))
        sterowanie1 = self.czcionka2.render("Gracz 1: W S    Gracz 2: ↑ ↓    Start: SPACJA    Menu: M", True, (255, 255, 255))
        self.gra.okno.blit(sterowanie1, (self.wielkosc_okna[0] / 2 - sterowanie1.get_rect().width / 2, self.polozenieinfo + 60))

    def skorki(self):
        kolor1 = (0, 0, 255)
        kolor2 = (200, 200, 200)
        kolor3 = (200, 200, 200)
        kolor4 = (200, 200, 200)
        kolor5 = (0, 255, 0)
        kolor6 = (200, 200, 200)
        kolor7 = (200, 200, 200)
        kolor8 = (200, 200, 200)
        kolor9 = (200, 200, 200)
        kolor10 = (255, 0, 0)
        kolor11 = (200, 200, 200)
        kolor12 = (200, 200, 200)
        kolor13 = (200, 200, 200)
        kolor14 = (200, 200, 200)
        kolor15 = (200, 200, 200)
        kolor16 = (200, 200, 200)
        kolor17 = (200, 200, 200)
        while self.sprawdzenie_skorki:
            pozycja_myszy = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and 950 < pozycja_myszy[0] < 1150 and self.wielkosc_okna[1] /\
                        2 + 150 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 250:
                    self.sprawdzenie_menu = True
                    self.sprawdzenie_skorki = False
                if event.type == pygame.MOUSEBUTTONDOWN and 50 < pozycja_myszy[0] < 70 and self.wielkosc_okna[1] /\
                        4 < pozycja_myszy[1] < self.wielkosc_okna[1] / 4 + 20:
                    kolor1 = (0, 0, 255)
                    kolor2 = (200, 200, 200)
                    kolor3 = (200, 200, 200)
                    kolor4 = (200, 200, 200)
                    self.paletka1 = pygame.image.load("paletka.jpg")
                elif event.type == pygame.MOUSEBUTTONDOWN and 150 < pozycja_myszy[0] < 170 and self.wielkosc_okna[1] /\
                        4 < pozycja_myszy[1] < self.wielkosc_okna[1] / 4 + 20:
                    kolor1 = (200, 200, 200)
                    kolor2 = (0, 0, 255)
                    kolor3 = (200, 200, 200)
                    kolor4 = (200, 200, 200)
                    self.paletka1 = pygame.image.load("paletka1.jpg")
                elif event.type == pygame.MOUSEBUTTONDOWN and 250 < pozycja_myszy[0] < 270 and self.wielkosc_okna[1] /\
                        4 < pozycja_myszy[1] < self.wielkosc_okna[1] / 4 + 20:
                    kolor1 = (200, 200, 200)
                    kolor2 = (200, 200, 200)
                    kolor3 = (0, 0, 255)
                    kolor4 = (200, 200, 200)
                    self.paletka1 = pygame.image.load("paletka2.jpg")
                elif event.type == pygame.MOUSEBUTTONDOWN and 350 < pozycja_myszy[0] < 370 and self.wielkosc_okna[1] /\
                        4 < pozycja_myszy[1] < self.wielkosc_okna[1] / 4 + 20:
                    kolor1 = (200, 200, 200)
                    kolor2 = (200, 200, 200)
                    kolor3 = (200, 200, 200)
                    kolor4 = (0, 0, 255)
                    self.paletka1 = pygame.image.load("paletka3.jpg")
                elif 950 < pozycja_myszy[0] < 1150 and self.wielkosc_okna[1] /\
                        2 + 150 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 250:
                    kolor9 = (255, 255, 255)
                if event.type == pygame.MOUSEBUTTONDOWN and 50 < pozycja_myszy[0] < 70 and self.wielkosc_okna[1] /\
                        2 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 20:
                    kolor5 = (0, 255, 0)
                    kolor6 = (200, 200, 200)
                    kolor7 = (200, 200, 200)
                    kolor8 = (200, 200, 200)
                    kolor14 = (200, 200, 200)
                    kolor15 = (200, 200, 200)
                    kolor16 = (200, 200, 200)
                    kolor17 = (200, 200, 200)
                    self.kulka1 = pygame.image.load("kulka.jpg")
                elif event.type == pygame.MOUSEBUTTONDOWN and 150 < pozycja_myszy[0] < 170 and self.wielkosc_okna[1] /\
                        2 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 20:
                    kolor5 = (200, 200, 200)
                    kolor6 = (0, 255, 0)
                    kolor7 = (200, 200, 200)
                    kolor8 = (200, 200, 200)
                    kolor14 = (200, 200, 200)
                    kolor15 = (200, 200, 200)
                    kolor16 = (200, 200, 200)
                    kolor17 = (200, 200, 200)
                    self.kulka1 = pygame.image.load("kulka1.jpg")
                elif event.type == pygame.MOUSEBUTTONDOWN and 250 < pozycja_myszy[0] < 270 and self.wielkosc_okna[1] /\
                        2 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 20:
                    kolor5 = (200, 200, 200)
                    kolor6 = (200, 200, 200)
                    kolor7 = (0, 255, 0)
                    kolor8 = (200, 200, 200)
                    kolor14 = (200, 200, 200)
                    kolor15 = (200, 200, 200)
                    kolor16 = (200, 200, 200)
                    kolor17 = (200, 200, 200)
                    self.kulka1 = pygame.image.load("kulka2.jpg")
                elif event.type == pygame.MOUSEBUTTONDOWN and 350 < pozycja_myszy[0] < 370 and self.wielkosc_okna[1] /\
                        2 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 20:
                    kolor5 = (200, 200, 200)
                    kolor6 = (200, 200, 200)
                    kolor7 = (200, 200, 200)
                    kolor8 = (0, 255, 0)
                    kolor14 = (200, 200, 200)
                    kolor15 = (200, 200, 200)
                    kolor16 = (200, 200, 200)
                    kolor17 = (200, 200, 200)
                    self.kulka1 = pygame.image.load("kulka3.jpg")
                if event.type == pygame.MOUSEBUTTONDOWN and 830 < pozycja_myszy[0] < 850 and self.wielkosc_okna[1] /\
                        4 < pozycja_myszy[1] < self.wielkosc_okna[1] / 4 + 20:
                    kolor10 = (255, 0, 0)
                    kolor11 = (200, 200, 200)
                    kolor12 = (200, 200, 200)
                    kolor13 = (200, 200, 200)
                    self.paletka2 = pygame.image.load("paletka.jpg")
                elif event.type == pygame.MOUSEBUTTONDOWN and 930 < pozycja_myszy[0] < 950 and self.wielkosc_okna[1] /\
                        4 < pozycja_myszy[1] < self.wielkosc_okna[1] / 4 + 20:
                    kolor10 = (200, 200, 200)
                    kolor11 = (255, 0, 0)
                    kolor12 = (200, 200, 200)
                    kolor13 = (200, 200, 200)
                    self.paletka2 = pygame.image.load("paletka1.jpg")
                elif event.type == pygame.MOUSEBUTTONDOWN and 1030 < pozycja_myszy[0] < 1050 and self.wielkosc_okna[1] /\
                        4 < pozycja_myszy[1] < self.wielkosc_okna[1] / 4 + 20:
                    kolor10 = (200, 200, 200)
                    kolor11 = (200, 200, 200)
                    kolor12 = (255, 0, 0)
                    kolor13 = (200, 200, 200)
                    self.paletka2 = pygame.image.load("paletka2.jpg")
                elif event.type == pygame.MOUSEBUTTONDOWN and 1130 < pozycja_myszy[0] < 1150 and self.wielkosc_okna[1] /\
                        4 < pozycja_myszy[1] < self.wielkosc_okna[1] / 4 + 20:
                    kolor10 = (200, 200, 200)
                    kolor11 = (200, 200, 200)
                    kolor12 = (200, 200, 200)
                    kolor13 = (255, 0, 0)
                    self.paletka2 = pygame.image.load("paletka3.jpg")
                if event.type == pygame.MOUSEBUTTONDOWN and 830 < pozycja_myszy[0] < 850 and self.wielkosc_okna[1] /\
                        2 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 20:
                    kolor5 = (200, 200, 200)
                    kolor6 = (200, 200, 200)
                    kolor7 = (200, 200, 200)
                    kolor8 = (200, 200, 200)
                    kolor14 = (0, 255, 0)
                    kolor15 = (200, 200, 200)
                    kolor16 = (200, 200, 200)
                    kolor17 = (200, 200, 200)
                    self.kulka1 = pygame.image.load("kulka4.jpg")
                elif event.type == pygame.MOUSEBUTTONDOWN and 930 < pozycja_myszy[0] < 950 and self.wielkosc_okna[1] /\
                        2 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 20:
                    kolor5 = (200, 200, 200)
                    kolor6 = (200, 200, 200)
                    kolor7 = (200, 200, 200)
                    kolor8 = (200, 200, 200)
                    kolor14 = (200, 200, 200)
                    kolor15 = (0, 255, 0)
                    kolor16 = (200, 200, 200)
                    kolor17 = (200, 200, 200)
                    self.kulka1 = pygame.image.load("kulka5.jpg")
                elif event.type == pygame.MOUSEBUTTONDOWN and 1030 < pozycja_myszy[0] < 1050 and self.wielkosc_okna[1] /\
                        2 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 20:
                    kolor5 = (200, 200, 200)
                    kolor6 = (200, 200, 200)
                    kolor7 = (200, 200, 200)
                    kolor8 = (200, 200, 200)
                    kolor14 = (200, 200, 200)
                    kolor15 = (200, 200, 200)
                    kolor16 = (0, 255, 0)
                    kolor17 = (200, 200, 200)
                    self.kulka1 = pygame.image.load("kulka6.jpg")
                elif event.type == pygame.MOUSEBUTTONDOWN and 1130 < pozycja_myszy[0] < 1150 and self.wielkosc_okna[1] /\
                        2 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 20:
                    kolor5 = (200, 200, 200)
                    kolor6 = (200, 200, 200)
                    kolor7 = (200, 200, 200)
                    kolor8 = (200, 200, 200)
                    kolor14 = (200, 200, 200)
                    kolor15 = (200, 200, 200)
                    kolor16 = (200, 200, 200)
                    kolor17 = (0, 255, 0)
                    self.kulka1 = pygame.image.load("kulka.jpg")
                if 950 > pozycja_myszy[0] or pozycja_myszy[0] > 1150 or self.wielkosc_okna[1] /\
                        2 + 150 > pozycja_myszy[1] or pozycja_myszy[1] > self.wielkosc_okna[1] / 2 + 250:
                    kolor9 = (200, 200, 200)

            self.gra.okno.fill((0, 0, 0))
            self.przyciski_skorki(kolor1, kolor2, kolor3, kolor4, kolor5, kolor6, kolor7, kolor8, kolor9, kolor10, kolor11, kolor12, kolor13, kolor14, kolor15, kolor16, kolor17)
            pygame.display.flip()

    def przyciski_skorki(self, kolor1, kolor2, kolor3, kolor4, kolor5, kolor6, kolor7, kolor8, kolor9, kolor10, kolor11, kolor12, kolor13, kolor14, kolor15, kolor16, kolor17):
        przyciskpaletki1 = pygame.Rect(50, self.wielkosc_okna[1] / 4, 20, 20)
        przyciskpaletki2 = pygame.Rect(150, self.wielkosc_okna[1] / 4, 20, 20)
        przyciskpaletki3 = pygame.Rect(250, self.wielkosc_okna[1] / 4, 20, 20)
        przyciskpaletki4 = pygame.Rect(350, self.wielkosc_okna[1] / 4, 20, 20)
        przyciskpilki1 = pygame.Rect(50, self.wielkosc_okna[1] / 2, 20, 20)
        przyciskpilki2 = pygame.Rect(150, self.wielkosc_okna[1] / 2, 20, 20)
        przyciskpilki3 = pygame.Rect(250, self.wielkosc_okna[1] / 2, 20, 20)
        przyciskpilki4 = pygame.Rect(350, self.wielkosc_okna[1] / 2, 20, 20)
        przyciskpaletki5 = pygame.Rect(830, self.wielkosc_okna[1] / 4, 20, 20)
        przyciskpaletki6 = pygame.Rect(930, self.wielkosc_okna[1] / 4, 20, 20)
        przyciskpaletki7 = pygame.Rect(1030, self.wielkosc_okna[1] / 4, 20, 20)
        przyciskpaletki8 = pygame.Rect(1130, self.wielkosc_okna[1] / 4, 20, 20)
        przyciskpilki5 = pygame.Rect(830, self.wielkosc_okna[1] / 2, 20, 20)
        przyciskpilki6 = pygame.Rect(930, self.wielkosc_okna[1] / 2, 20, 20)
        przyciskpilki7 = pygame.Rect(1030, self.wielkosc_okna[1] / 2, 20, 20)
        przyciskpilki8 = pygame.Rect(1130, self.wielkosc_okna[1] / 2, 20, 20)
        przyciskmenu = pygame.Rect(950, self.wielkosc_okna[1] / 2 + 150, 200, 100)
        pygame.draw.rect(self.gra.okno, kolor1, przyciskpaletki1)
        pygame.draw.rect(self.gra.okno, kolor2, przyciskpaletki2)
        pygame.draw.rect(self.gra.okno, kolor3, przyciskpaletki3)
        pygame.draw.rect(self.gra.okno, kolor4, przyciskpaletki4)
        pygame.draw.rect(self.gra.okno, kolor5, przyciskpilki1)
        pygame.draw.rect(self.gra.okno, kolor6, przyciskpilki2)
        pygame.draw.rect(self.gra.okno, kolor7, przyciskpilki3)
        pygame.draw.rect(self.gra.okno, kolor8, przyciskpilki4)
        pygame.draw.rect(self.gra.okno, kolor10, przyciskpaletki5)
        pygame.draw.rect(self.gra.okno, kolor11, przyciskpaletki6)
        pygame.draw.rect(self.gra.okno, kolor12, przyciskpaletki7)
        pygame.draw.rect(self.gra.okno, kolor13, przyciskpaletki8)
        pygame.draw.rect(self.gra.okno, kolor14, przyciskpilki5)
        pygame.draw.rect(self.gra.okno, kolor15, przyciskpilki6)
        pygame.draw.rect(self.gra.okno, kolor16, przyciskpilki7)
        pygame.draw.rect(self.gra.okno, kolor17, przyciskpilki8)
        pygame.draw.rect(self.gra.okno, kolor9, przyciskmenu)
        self.gra.okno.blit(pygame.image.load("paletka.jpg"), (50, self.wielkosc_okna[1] / 4 - 120))
        self.gra.okno.blit(pygame.image.load("paletka1.jpg"), (150, self.wielkosc_okna[1] / 4 - 120))
        self.gra.okno.blit(pygame.image.load("paletka2.jpg"), (250, self.wielkosc_okna[1] / 4 - 120))
        self.gra.okno.blit(pygame.image.load("paletka3.jpg"), (350, self.wielkosc_okna[1] / 4 - 120))
        self.gra.okno.blit(pygame.image.load("paletka.jpg"), (830, self.wielkosc_okna[1] / 4 - 120))
        self.gra.okno.blit(pygame.image.load("paletka1.jpg"), (930, self.wielkosc_okna[1] / 4 - 120))
        self.gra.okno.blit(pygame.image.load("paletka2.jpg"), (1030, self.wielkosc_okna[1] / 4 - 120))
        self.gra.okno.blit(pygame.image.load("paletka3.jpg"), (1130, self.wielkosc_okna[1] / 4 - 120))
        self.gra.okno.blit(pygame.image.load("kulka.jpg"), (50, self.wielkosc_okna[1] / 2 - 30))
        self.gra.okno.blit(pygame.image.load("kulka1.jpg"), (150, self.wielkosc_okna[1] / 2 - 30))
        self.gra.okno.blit(pygame.image.load("kulka2.jpg"), (250, self.wielkosc_okna[1] / 2 - 30))
        self.gra.okno.blit(pygame.image.load("kulka3.jpg"), (350, self.wielkosc_okna[1] / 2 - 30))
        self.gra.okno.blit(pygame.image.load("kulka4.jpg"), (830, self.wielkosc_okna[1] / 2 - 30))
        self.gra.okno.blit(pygame.image.load("kulka5.jpg"), (930, self.wielkosc_okna[1] / 2 - 30))
        self.gra.okno.blit(pygame.image.load("kulka6.jpg"), (1030, self.wielkosc_okna[1] / 2 - 30))
        self.gra.okno.blit(pygame.image.load("kulka.jpg"), (1130, self.wielkosc_okna[1] / 2 - 30))
        napis_menu = self.czcionka.render("MENU", True, (0, 0, 0))
        self.gra.okno.blit(napis_menu, (960, self.wielkosc_okna[1] / 2 + 165))

    def menu(self):
        kolor1 = (200, 200, 200)
        kolor2 = (200, 200, 200)
        if self.komputer == False:
            kolor3 = (200, 0, 0)
            kolor4 = (0, 200, 0)
        elif self.komputer == True:
            kolor3 = (0, 200, 0)
            kolor4 = (200, 0, 0)
        if self.trudnosc == 0:
            kolor5 = (0, 200, 0)
            kolor6 = (200, 0, 0)
            kolor7 = (200, 0, 0)
        elif self.trudnosc == 1:
            kolor5 = (200, 0, 0)
            kolor6 = (0, 200, 0)
            kolor7 = (200, 0, 0)
        elif self.trudnosc == 2:
            kolor5 = (200, 0, 0)
            kolor6 = (200, 0, 0)
            kolor7 = (0, 200, 0)
        kolor8 = (200, 200, 200)
        while self.sprawdzenie_menu:
            pozycja_myszy = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and 200 < pozycja_myszy[0] < 400 and self.wielkosc_okna[
                    1] / 2 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 100:
                    self.sprawdzenie_menu = False
                elif event.type == pygame.MOUSEBUTTONDOWN and 800 < pozycja_myszy[0] < 1000 and self.wielkosc_okna[
                    1] / 2 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 100:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and 200 < pozycja_myszy[0] < 400 and self.wielkosc_okna[
                    1] / 2 + 125 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 175:
                    self.komputer = True
                    kolor4 = (200, 0, 0)
                    kolor3 = (0, 200, 0)
                    self.tekst1, self.tekst2 = 0, 0
                elif event.type == pygame.MOUSEBUTTONDOWN and 500 < pozycja_myszy[0] < 700 and self.wielkosc_okna[
                    1] / 2 + 50 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 100:
                    self.trudnosc = 0
                    kolor5 = (0, 200, 0)
                    kolor6 = (200, 0, 0)
                    kolor7 = (200, 0, 0)
                    self.tekst1, self.tekst2 = 0, 0
                elif event.type == pygame.MOUSEBUTTONDOWN and 500 < pozycja_myszy[0] < 700 and self.wielkosc_okna[
                    1] / 2 + 125 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 175:
                    self.trudnosc = 1
                    kolor5 = (200, 0, 0)
                    kolor6 = (0, 200, 0)
                    kolor7 = (200, 0, 0)
                    self.tekst1, self.tekst2 = 0, 0
                elif event.type == pygame.MOUSEBUTTONDOWN and 500 < pozycja_myszy[0] < 700 and self.wielkosc_okna[
                    1] / 2 + 200 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 250:
                    self.trudnosc = 2
                    kolor5 = (200, 0, 0)
                    kolor6 = (200, 0, 0)
                    kolor7 = (0, 200, 0)
                    self.tekst1, self.tekst2 = 0, 0
                elif event.type == pygame.MOUSEBUTTONDOWN and 200 < pozycja_myszy[0] < 400 and self.wielkosc_okna[
                    1] / 2 + 200 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 250:
                    self.komputer = False
                    kolor3 = (200, 0, 0)
                    kolor4 = (0, 200, 0)
                    self.tekst1, self.tekst2 = 0, 0
                elif event.type == pygame.MOUSEBUTTONDOWN and 800 < pozycja_myszy[0] < 1000 and self.wielkosc_okna[1] /\
                        2 + 150 < pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 250:
                    self.sprawdzenie_menu = False
                    self.sprawdzenie_skorki = True
                elif 200 < pozycja_myszy[0] < 400 and self.wielkosc_okna[1] / 2 < \
                        pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 100:
                    kolor1 = (255, 255, 255)
                elif 500 < pozycja_myszy[0] < 700 and self.wielkosc_okna[1] / 2 + 50 < \
                        pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 100:
                    if kolor5 == (0, 200, 0):
                        kolor5 = (0, 255, 0)
                    elif kolor5 == (200, 0, 0):
                        kolor5 = (255, 0, 0)
                elif 500 < pozycja_myszy[0] < 700 and self.wielkosc_okna[1] / 2 + 125 < \
                        pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 175:
                    if kolor6 == (0, 200, 0):
                        kolor6 = (0, 255, 0)
                    elif kolor6 == (200, 0, 0):
                        kolor6 = (255, 0, 0)
                elif 500 < pozycja_myszy[0] < 700 and self.wielkosc_okna[1] / 2 + 200 < \
                        pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 250:
                    if kolor7 == (0, 200, 0):
                        kolor7 = (0, 255, 0)
                    elif kolor7 == (200, 0, 0):
                        kolor7 = (255, 0, 0)
                elif 800 < pozycja_myszy[0] < 1000 and self.wielkosc_okna[1] / 2 < \
                        pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 100:
                    kolor2 = (255, 255, 255)
                elif 800 < pozycja_myszy[0] < 1000 and self.wielkosc_okna[1] / 2 + 150 < \
                        pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 250:
                    kolor8 = (255, 255, 255)
                elif 200 < pozycja_myszy[0] < 400 and self.wielkosc_okna[1] / 2 + 125 < \
                        pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 175:
                    if kolor3 == (0, 200, 0):
                        kolor3 = (0, 255, 0)
                    elif kolor3 == (200, 0, 0):
                        kolor3 = (255, 0, 0)
                elif 200 < pozycja_myszy[0] < 400 and self.wielkosc_okna[1] / 2 + 200 < \
                        pozycja_myszy[1] < self.wielkosc_okna[1] / 2 + 250:
                    if kolor4 == (0, 200, 0):
                        kolor4 = (0, 255, 0)
                    elif kolor4 == (200, 0, 0):
                        kolor4 = (255, 0, 0)
                elif 200 > pozycja_myszy[0] or 800 > pozycja_myszy[0] > 400 or pozycja_myszy[0] > 1000 or \
                        self.wielkosc_okna[1] / 2 > pozycja_myszy[1] or self.wielkosc_okna[1] / 2 + 125 > \
                        pozycja_myszy[1] > self.wielkosc_okna[1] / 2 + 100 or self.wielkosc_okna[1] / 2 + 200 > \
                        pozycja_myszy[1] > self.wielkosc_okna[1] / 2 + 175 or pozycja_myszy[1] > \
                        self.wielkosc_okna[1] / 2 + 250:
                    kolor1 = (200, 200, 200)
                    kolor2 = (200, 200, 200)
                    kolor8 = (200, 200, 200)
                    if kolor3 == (0, 255, 0) or kolor3 == (0, 200, 0):
                        kolor3 = (0, 200, 0)
                    else:
                        kolor3 = (200, 0, 0)
                    if kolor4 == (255, 0, 0) or kolor4 == (200, 0, 0):
                        kolor4 = (200, 0, 0)
                    else:
                        kolor4 = (0, 200, 0)
                    if kolor5 == (255, 0, 0) or kolor5 == (200, 0, 0):
                        kolor5 = (200, 0, 0)
                    else:
                        kolor5 = (0, 200, 0)
                    if kolor6 == (255, 0, 0) or kolor6 == (200, 0, 0):
                        kolor6 = (200, 0, 0)
                    else:
                        kolor6 = (0, 200, 0)
                    if kolor7 == (255, 0, 0) or kolor7 == (200, 0, 0):
                        kolor7 = (200, 0, 0)
                    else:
                        kolor7 = (0, 200, 0)
            if self.zmianamuzyki == 0 and self.sprawdzenie_menu == False and self.sprawdzenie_skorki == False:
                pygame.mixer.music.load("muzyka.wav")
                pygame.mixer.music.play(-1)
                self.zmianamuzyki = 1
            elif self.zmianamuzyki == 1 and self.sprawdzenie_menu == True:
                pygame.mixer.music.load("dzwiekmenu.wav")
                pygame.mixer.music.play(-1)
                self.zmianamuzyki = 0
            elif self.zmianamuzyki == 0 and self.sprawdzenie_menu == False and self.sprawdzenie_skorki == True:
                pygame.mixer.music.load("dzwiekmenu.wav")
                pygame.mixer.music.play(-1)
                self.zmianamuzyki = 1
            self.gra.okno.fill((0, 0, 0))
            self.przyciski_menu(kolor1, kolor2, kolor3, kolor4, kolor5, kolor6, kolor7, kolor8)
            pygame.display.flip()

    def przyciski_menu(self, kolor1, kolor2, kolor3, kolor4, kolor5, kolor6, kolor7, kolor8):
        przycisk1 = pygame.Rect(200, self.wielkosc_okna[1] / 2, 200, 100)
        przycisk2 = pygame.Rect(800, self.wielkosc_okna[1] / 2, 200, 100)
        przycisk3 = pygame.Rect(200, self.wielkosc_okna[1] / 2 + 125, 200, 50)
        przycisk4 = pygame.Rect(200, self.wielkosc_okna[1] / 2 + 200, 200, 50)
        przycisk5 = pygame.Rect(500, self.wielkosc_okna[1] / 2 + 50, 200, 50)
        przycisk6 = pygame.Rect(500, self.wielkosc_okna[1] / 2 + 125, 200, 50)
        przycisk7 = pygame.Rect(500, self.wielkosc_okna[1] / 2 + 200, 200, 50)
        przycisk8 = pygame.Rect(800, self.wielkosc_okna[1] / 2 + 150, 200, 100)
        pygame.draw.rect(self.gra.okno, kolor1, przycisk1)
        pygame.draw.rect(self.gra.okno, kolor2, przycisk2)
        pygame.draw.rect(self.gra.okno, kolor3, przycisk3)
        pygame.draw.rect(self.gra.okno, kolor4, przycisk4)
        pygame.draw.rect(self.gra.okno, kolor5, przycisk5)
        pygame.draw.rect(self.gra.okno, kolor6, przycisk6)
        pygame.draw.rect(self.gra.okno, kolor7, przycisk7)
        pygame.draw.rect(self.gra.okno, kolor8, przycisk8)
        napis_start = self.czcionka.render("START", True, (0, 0, 0))
        self.gra.okno.blit(napis_start, (210, self.wielkosc_okna[1] / 2 + 15))
        napis_wyjscie = self.czcionka.render("WYJDŹ", True, (0, 0, 0))
        self.gra.okno.blit(napis_wyjscie, (798, self.wielkosc_okna[1] / 2 + 15))
        napis_info = self.czcionka1.render("SKÓRKI", True, (0, 0, 0))
        self.gra.okno.blit(napis_info, (807, self.wielkosc_okna[1] / 2 + 175))
        napis_1gracz = self.czcionka2.render("1 GRACZ", True, (0, 0, 0))
        self.gra.okno.blit(napis_1gracz, (235, self.wielkosc_okna[1] / 2 + 135))
        napis_2graczy = self.czcionka2.render("2 GRACZY", True, (0, 0, 0))
        self.gra.okno.blit(napis_2graczy, (225, self.wielkosc_okna[1] / 2 + 210))
        tytul = self.czcionka3.render("PONG WAR", True, (255, 255, 255))
        self.gra.okno.blit(tytul, (75, 10))
        napis_0trudnosc = self.czcionka2.render("ŁATWY", True, (0, 0, 0))
        self.gra.okno.blit(napis_0trudnosc, (550, self.wielkosc_okna[1] / 2 + 60))
        napis_1trudnosc = self.czcionka2.render("TRUDNY", True, (0, 0, 0))
        self.gra.okno.blit(napis_1trudnosc, (535, self.wielkosc_okna[1] / 2 + 135))
        napis_2trudnosc = self.czcionka2.render("NIEMOŻLIWY", True, (0, 0, 0))
        self.gra.okno.blit(napis_2trudnosc, (502, self.wielkosc_okna[1] / 2 + 210))
