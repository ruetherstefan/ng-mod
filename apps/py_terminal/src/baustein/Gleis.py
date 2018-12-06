import pygame
from enum import Enum

from src.baustein.Baustein import Baustein
from src.util.Bilder import *
from src.serial.Weichen_control_bote import Weichencontrollerbote


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

class GleisUntenNachLinks(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_cl2.xpm")

class GleisObenNachRechts(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_cl4.xpm")

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

class GleisRechtsNachOben(Baustein):
    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_cr3.xpm")

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

        self.markierung_links_mitte = get_image(Baustein.bilder_ordner + "Markierungen/WeicheLinksMitte.png")
        self.markierung_links_oben = get_image(Baustein.bilder_ordner + "Markierungen/WeicheLinksOben.png")
        self.markierung_links_unten = get_image(Baustein.bilder_ordner + "Markierungen/WeicheLinksUnten.png")
        self.markierung_rechts_mitte = get_image(Baustein.bilder_ordner + "Markierungen/WeicheRechtsMitte.png")
        self.markierung_rechts_oben = get_image(Baustein.bilder_ordner + "Markierungen/WeicheRechtsOben.png")
        self.markierung_rechts_unten = get_image(Baustein.bilder_ordner + "Markierungen/WeicheRechtsUnten.png")

    def aendereWeichenstellung(self):
        if self.weichenstellung == Weichenstellung.GERADE:
            self.weichenstellung = Weichenstellung.ABZWEIGEND
        else:
            self.weichenstellung = Weichenstellung.GERADE
        Weichencontrollerbote().aendereWeichenstellung("Weicheenum1", self.weichenstellung)

    def draw(self):
        super().draw()
        self.screen.blit(self.weichenstellung_bild.get(self.weichenstellung), self.get_position())

class WeicheRechtsNachUnten(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_tl3.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = self.markierung_links_mitte
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = self.markierung_links_unten


class WeicheRechtsNachOben(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_tr3.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = self.markierung_links_mitte
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = self.markierung_links_oben


class WeicheLinksNachUnten(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_tr1.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = self.markierung_rechts_mitte
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = self.markierung_rechts_unten


class WeicheLinksNachOben(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_tl1.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = self.markierung_rechts_oben
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = self.markierung_rechts_mitte


class WeicheRechtsObenNachUnten(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_dbr.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = self.markierung_links_mitte
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = self.markierung_links_unten


class WeicheRechtsUntenNachOben(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_dtl.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = self.markierung_links_mitte
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = self.markierung_links_oben


class WeicheLinksObenNachUnten(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_dbl.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = self.markierung_rechts_unten
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = self.markierung_rechts_mitte


class WeicheLinksUntenNachOben(Weiche):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = get_image(Baustein.bilder_ordner + "spdritem_dtr.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = self.markierung_rechts_oben
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = self.markierung_rechts_mitte


