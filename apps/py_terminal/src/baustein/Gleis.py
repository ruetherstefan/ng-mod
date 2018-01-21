import pygame
from enum import Enum

from src.baustein.Baustein import Baustein


class GleisHorizontal(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_trh.xpm").convert()

class GleisVertikal(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_trv.xpm").convert()

class GleisUntenNachRechts(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_cr2.xpm").convert()

class GleisObenNachLinks(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_cr4.xpm").convert()

class GleisLinksNachOben(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_cl1.xpm").convert()

class GleisLinksNachUnten(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_cr1.xpm").convert()

class GleisRechtsNachUnten(Baustein):
    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_cl3.xpm").convert()



#Weichen

class Weichenstellung(Enum):
    GERADE = 1
    ABZWEIGEND = 2



class Weiche(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.weichenstellung = Weichenstellung.GERADE
        self.weichenstellung_bild = {}


class WeicheRechtsNachUnten(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_tl3.xpm").convert()


class WeicheRechtsNachOben(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_tr3.xpm").convert()


class WeicheLinksNachUnten(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_tr1.xpm").convert()


class WeicheLinksNachOben(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_tl1.xpm").convert()


class WeicheLinksUntenNachOben(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_dtr.xpm").convert()

        self.weichenstellung_bild[Weichenstellung.GERADE] = pygame.image.load(
            Baustein.bilder_ordner + "Markierungen/WeicheRechtsOben.png")

        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = pygame.image.load(
            Baustein.bilder_ordner + "Markierungen/WeicheRechtsMitte.png")

    def draw(self):
        super().draw()
        self.screen.blit(self.weichenstellung_bild.get(self.weichenstellung), self.get_position())

class WeicheYR(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_syr.xpm").convert()
