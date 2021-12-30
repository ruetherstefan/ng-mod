from src.model.Weichenstellung import Weichenstellung
from src.view.WeichenstellungBildLookup import *
from src.serial.WeichenControlBote import WeichenControlBote
from src.util.Bilder import Bilder


class Weiche(Baustein):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen)

        self.adresse = weichenadresse

        self.weichenstellung = Weichenstellung.GERADE

        self.gleisbelegung = Gleisbelegung.FREI
        self.markierungsart = {}

    def aendere_weichenstellung(self):
        if self.weichenstellung == Weichenstellung.GERADE:
            self.weichenstellung = Weichenstellung.ABZWEIGEND
        else:
            self.weichenstellung = Weichenstellung.GERADE
        WeichenControlBote().aendere_weichenstellung(self.adresse, self.weichenstellung)

    def toggleFahrstrasse(self):
        if Gleisbelegung.FREI == self.gleisbelegung:
            self.gleisbelegung = Gleisbelegung.FAHRSTRASSE
        elif Gleisbelegung.FAHRSTRASSE == self.gleisbelegung:
            self.gleisbelegung = Gleisbelegung.FREI


    def draw(self):
        super().draw()
        self.screen.blit(WeichenstellungBildLookup.lookup(self.markierungsart[self.weichenstellung], self.gleisbelegung), self.get_position())


class WeicheRechtsNachUnten(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_tl3.xpm")
        self.markierungsart[Weichenstellung.GERADE] = Markierungsart.LINKS_MITTE
        self.markierungsart[Weichenstellung.ABZWEIGEND] = Markierungsart.LINKS_UNTEN


class WeicheRechtsNachOben(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_tr3.xpm")
        self.markierungsart[Weichenstellung.GERADE] = Markierungsart.LINKS_MITTE
        self.markierungsart[Weichenstellung.ABZWEIGEND] = Markierungsart.LINKS_OBEN


class WeicheLinksNachUnten(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_tr1.xpm")
        self.markierungsart[Weichenstellung.GERADE] = Markierungsart.RECHTS_MITTE
        self.markierungsart[Weichenstellung.ABZWEIGEND] = Markierungsart.RECHTS_UNTEN


class WeicheLinksNachOben(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_tl1.xpm")
        self.markierungsart[Weichenstellung.GERADE] = Markierungsart.RECHTS_OBEN
        self.markierungsart[Weichenstellung.ABZWEIGEND] = Markierungsart.RECHTS_MITTE


class WeicheRechtsObenNachUnten(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_dbr.xpm")
        self.markierungsart[Weichenstellung.GERADE] = Markierungsart.LINKS_MITTE
        self.markierungsart[Weichenstellung.ABZWEIGEND] = Markierungsart.LINKS_UNTEN


class WeicheRechtsUntenNachOben(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_dtl.xpm")
        self.markierungsart[Weichenstellung.GERADE] = Markierungsart.LINKS_MITTE
        self.markierungsart[Weichenstellung.ABZWEIGEND] = Markierungsart.LINKS_OBEN


class WeicheLinksObenNachUnten(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_dbl.xpm")
        self.markierungsart[Weichenstellung.GERADE] = Markierungsart.RECHTS_UNTEN
        self.markierungsart[Weichenstellung.ABZWEIGEND] = Markierungsart.RECHTS_MITTE

class WeicheLinksUntenNachOben(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_dtr.xpm")
        self.markierungsart[Weichenstellung.GERADE] = Markierungsart.RECHTS_OBEN
        self.markierungsart[Weichenstellung.ABZWEIGEND] = Markierungsart.RECHTS_MITTE
