from src.baustein.Baustein import Baustein
from src.baustein.Weichenstellung import Weichenstellung
from src.baustein.WeichenstellungBildLookup import *
from src.serial.WeichenControlBote import WeichenControlBote
from src.util.Bilder import Bilder


class Weiche(Baustein):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen)

        self.adresse = weichenadresse

        self.weichenstellung = Weichenstellung.GERADE
        self.weichenstellung_bild = {}

        self.gleisbelegung = Gleisbelegung.FREI

    def aendere_weichenstellung(self):
        if self.weichenstellung == Weichenstellung.GERADE:
            self.weichenstellung = Weichenstellung.ABZWEIGEND
        else:
            self.weichenstellung = Weichenstellung.GERADE
        WeichenControlBote().aendere_weichenstellung(self.adresse, self.weichenstellung)

    def draw(self):
        super().draw()
        self.screen.blit(self.weichenstellung_bild.get(self.weichenstellung), self.get_position())


class WeicheRechtsNachUnten(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_tl3.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = WeichenstellungBildLookup.lookup(Markierungsart.LINKS_MITTE, self.gleisbelegung)
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = WeichenstellungBildLookup.lookup(Markierungsart.LINKS_UNTEN, self.gleisbelegung)


class WeicheRechtsNachOben(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_tr3.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = WeichenstellungBildLookup.lookup(Markierungsart.LINKS_MITTE, self.gleisbelegung)
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = WeichenstellungBildLookup.lookup(Markierungsart.LINKS_OBEN, self.gleisbelegung)


class WeicheLinksNachUnten(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_tr1.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = WeichenstellungBildLookup.lookup(Markierungsart.RECHTS_MITTE, self.gleisbelegung)
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = WeichenstellungBildLookup.lookup(Markierungsart.RECHTS_UNTEN, self.gleisbelegung)


class WeicheLinksNachOben(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_tl1.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = WeichenstellungBildLookup.lookup(Markierungsart.RECHTS_OBEN, self.gleisbelegung)
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = WeichenstellungBildLookup.lookup(Markierungsart.RECHTS_MITTE, self.gleisbelegung)


class WeicheRechtsObenNachUnten(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_dbr.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = WeichenstellungBildLookup.lookup(Markierungsart.LINKS_MITTE, self.gleisbelegung)
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = WeichenstellungBildLookup.lookup(Markierungsart.LINKS_UNTEN, self.gleisbelegung)


class WeicheRechtsUntenNachOben(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_dtl.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = WeichenstellungBildLookup.lookup(Markierungsart.LINKS_MITTE, self.gleisbelegung)
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = WeichenstellungBildLookup.lookup(Markierungsart.LINKS_OBEN, self.gleisbelegung)


class WeicheLinksObenNachUnten(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_dbl.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = WeichenstellungBildLookup.lookup(Markierungsart.RECHTS_UNTEN, self.gleisbelegung)
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = WeichenstellungBildLookup.lookup(Markierungsart.RECHTS_MITTE, self.gleisbelegung)


class WeicheLinksUntenNachOben(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_dtr.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = WeichenstellungBildLookup.lookup(Markierungsart.RECHTS_OBEN, self.gleisbelegung)
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = WeichenstellungBildLookup.lookup(Markierungsart.RECHTS_MITTE, self.gleisbelegung)
