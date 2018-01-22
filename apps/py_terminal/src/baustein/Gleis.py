import pygame
from enum import Enum

from src.baustein.Baustein import Baustein
from src.util.Bilder import *


class GleisHorizontal(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_trh.xpm")


class GleisVertikal(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_trv.xpm")

class GleisUntenNachRechts(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_cr2.xpm")

class GleisObenNachLinks(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_cr4.xpm")

class GleisLinksNachOben(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_cl1.xpm")

class GleisLinksNachUnten(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_cr1.xpm")

class GleisRechtsNachUnten(Baustein):
    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_cl3.xpm")



#Weichen

class Weichenstellung(Enum):
    GERADE = 1
    ABZWEIGEND = 2



class Weiche(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.weichenstellung = Weichenstellung.GERADE
        self.weichenstellung_bild = {}

    def aendereWeichenstellung(self):
        if self.weichenstellung == Weichenstellung.GERADE:
            self.weichenstellung = Weichenstellung.ABZWEIGEND
        else:
            self.weichenstellung = Weichenstellung.GERADE

class WeicheRechtsNachUnten(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_tl3.xpm")


class WeicheRechtsNachOben(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_tr3.xpm")


class WeicheLinksNachUnten(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_tr1.xpm")


class WeicheLinksNachOben(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_tl1.xpm")


class WeicheLinksUntenNachOben(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_dtr.xpm")

        self.weichenstellung_bild[Weichenstellung.GERADE] = get_image(
            Baustein.bilder_ordner + "Markierungen/WeicheRechtsOben.png")

        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = get_image(
            Baustein.bilder_ordner + "Markierungen/WeicheRechtsMitte.png")

    def draw(self):
        super().draw()
        self.screen.blit(self.weichenstellung_bild.get(self.weichenstellung), self.get_position())

class WeicheYR(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_syr.xpm").convert()
