from src.model.Weichenstellung import Weichenstellung
from src.view.WeichenstellungBildLookup import *
from src.serial.WeichenControlBote import WeichenControlBote
from src.util.Bilder import Bilder


class WeicheView(BausteinView):

    def __init__(self, screen, model):
        super().__init__(screen)

        self.model = model
        self.markierungsart = {}

    def toggle_fahrstrasse(self):
        if Gleisbelegung.FREI == self.model.gleisbelegung:
            self.model.gleisbelegung = Gleisbelegung.FAHRSTRASSE
        elif Gleisbelegung.FAHRSTRASSE == self.model.gleisbelegung:
            self.model.gleisbelegung = Gleisbelegung.FREI

    def draw(self):
        super().draw()
        self.screen.blit(
            WeichenstellungBildLookup.lookup(self.markierungsart[self.model.weichenstellung], self.model.gleisbelegung),
            self.get_position())


class WeicheViewRechtsNachUnten(WeicheView):

    def __init__(self, screen, model):
        super().__init__(screen, model)

        self.bild = Bilder().get_image("spdritem_tl3.xpm")
        self.markierungsart[Weichenstellung.GERADE] = Markierungsart.LINKS_MITTE
        self.markierungsart[Weichenstellung.ABZWEIGEND] = Markierungsart.LINKS_UNTEN


class WeicheViewRechtsNachOben(WeicheView):

    def __init__(self, screen, model):
        super().__init__(screen, model)

        self.bild = Bilder().get_image("spdritem_tr3.xpm")
        self.markierungsart[Weichenstellung.GERADE] = Markierungsart.LINKS_MITTE
        self.markierungsart[Weichenstellung.ABZWEIGEND] = Markierungsart.LINKS_OBEN


class WeicheViewLinksNachUnten(WeicheView):

    def __init__(self, screen, model):
        super().__init__(screen, model)

        self.bild = Bilder().get_image("spdritem_tr1.xpm")
        self.markierungsart[Weichenstellung.GERADE] = Markierungsart.RECHTS_MITTE
        self.markierungsart[Weichenstellung.ABZWEIGEND] = Markierungsart.RECHTS_UNTEN


class WeicheViewLinksNachOben(WeicheView):

    def __init__(self, screen, model):
        super().__init__(screen, model)

        self.bild = Bilder().get_image("spdritem_tl1.xpm")
        self.markierungsart[Weichenstellung.GERADE] = Markierungsart.RECHTS_OBEN
        self.markierungsart[Weichenstellung.ABZWEIGEND] = Markierungsart.RECHTS_MITTE


class WeicheViewRechtsObenNachUnten(WeicheView):

    def __init__(self, screen, model):
        super().__init__(screen, model)

        self.bild = Bilder().get_image("spdritem_dbr.xpm")
        self.markierungsart[Weichenstellung.GERADE] = Markierungsart.LINKS_MITTE
        self.markierungsart[Weichenstellung.ABZWEIGEND] = Markierungsart.LINKS_UNTEN


class WeicheViewRechtsUntenNachOben(WeicheView):

    def __init__(self, screen, model):
        super().__init__(screen, model)

        self.bild = Bilder().get_image("spdritem_dtl.xpm")
        self.markierungsart[Weichenstellung.GERADE] = Markierungsart.LINKS_MITTE
        self.markierungsart[Weichenstellung.ABZWEIGEND] = Markierungsart.LINKS_OBEN


class WeicheViewLinksObenNachUnten(WeicheView):

    def __init__(self, screen, model):
        super().__init__(screen, model)

        self.bild = Bilder().get_image("spdritem_dbl.xpm")
        self.markierungsart[Weichenstellung.GERADE] = Markierungsart.RECHTS_UNTEN
        self.markierungsart[Weichenstellung.ABZWEIGEND] = Markierungsart.RECHTS_MITTE


class WeicheViewLinksUntenNachOben(WeicheView):

    def __init__(self, screen, model):
        super().__init__(screen, model)

        self.bild = Bilder().get_image("spdritem_dtr.xpm")
        self.markierungsart[Weichenstellung.GERADE] = Markierungsart.RECHTS_OBEN
        self.markierungsart[Weichenstellung.ABZWEIGEND] = Markierungsart.RECHTS_MITTE
