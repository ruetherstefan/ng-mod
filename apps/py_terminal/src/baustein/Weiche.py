from src.baustein.Baustein import Baustein
from src.baustein.Weichenstellung import Weichenstellung
from src.serial.WeichenControlBote import WeichenControlBote
from src.util.Bilder import Bilder


class Weiche(Baustein):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen)

        self.adresse = weichenadresse

        self.weichenstellung = Weichenstellung.GERADE
        self.weichenstellung_bild = {}

        self.markierung_links_mitte = Bilder().get_image(Baustein.bilder_ordner + "Markierungen/WeicheLinksMitte.png")
        self.markierung_links_oben = Bilder().get_image(Baustein.bilder_ordner + "Markierungen/WeicheLinksOben.png")
        self.markierung_links_unten = Bilder().get_image(Baustein.bilder_ordner + "Markierungen/WeicheLinksUnten.png")
        self.markierung_rechts_mitte = Bilder().get_image(Baustein.bilder_ordner + "Markierungen/WeicheRechtsMitte.png")
        self.markierung_rechts_oben = Bilder().get_image(Baustein.bilder_ordner + "Markierungen/WeicheRechtsOben.png")
        self.markierung_rechts_unten = Bilder().get_image(Baustein.bilder_ordner + "Markierungen/WeicheRechtsUnten.png")

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
        self.weichenstellung_bild[Weichenstellung.GERADE] = self.markierung_links_mitte
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = self.markierung_links_unten


class WeicheRechtsNachOben(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_tr3.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = self.markierung_links_mitte
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = self.markierung_links_oben


class WeicheLinksNachUnten(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_tr1.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = self.markierung_rechts_mitte
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = self.markierung_rechts_unten


class WeicheLinksNachOben(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_tl1.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = self.markierung_rechts_oben
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = self.markierung_rechts_mitte


class WeicheRechtsObenNachUnten(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_dbr.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = self.markierung_links_mitte
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = self.markierung_links_unten


class WeicheRechtsUntenNachOben(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_dtl.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = self.markierung_links_mitte
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = self.markierung_links_oben


class WeicheLinksObenNachUnten(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_dbl.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = self.markierung_rechts_unten
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = self.markierung_rechts_mitte


class WeicheLinksUntenNachOben(Weiche):

    def __init__(self, screen, weichenadresse):
        super().__init__(screen, weichenadresse)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_dtr.xpm")
        self.weichenstellung_bild[Weichenstellung.GERADE] = self.markierung_rechts_oben
        self.weichenstellung_bild[Weichenstellung.ABZWEIGEND] = self.markierung_rechts_mitte
