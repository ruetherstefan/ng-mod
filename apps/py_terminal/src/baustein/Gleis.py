import pygame

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

class WeicheRechtsNachUnten(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_tl3.xpm").convert()


class WeicheRechtsNachOben(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_tr3.xpm").convert()


class WeicheLinksNachUnten(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_tr1.xpm").convert()


class WeicheLinksNachOben(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_tl1.xpm").convert()


class WeicheLinksUntenNachOben(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_dtr.xpm").convert()


class WeicheYR(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = pygame.image.load(Baustein.bilder_ordner + "spdritem_syr.xpm").convert()
