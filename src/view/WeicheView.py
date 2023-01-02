from src.controller.WeichenstellungController import WeichenstellungController
from src.model.weiche.Weichenstellung import Weichenstellung
from src.view.BausteinView import BausteinView
from src.view.WeichenstellungBildLookup import *
from src.util.Bilder import Bilder
from src.view.util import PygameConstant
from src.controller.FahrstrasseController import FahrstrasseController


class WeicheView(BausteinView):

    def __init__(self, screen, model):
        super().__init__(screen)

        self.model = model
        self.markierungsart = {}

    def draw(self):
        super().draw()
        self.screen.blit(
            WeichenstellungBildLookup.lookup(self.markierungsart[self.model.weichenstellung], self.model.gleisbelegung()),
            self.get_position())

    def click(self, event):
        if PygameConstant.MOUSE_CLICK_LEFT == event.button:
            WeichenstellungController().aendere_weichenstellung(self.model)
        elif PygameConstant.MOUSE_CLICK_RIGHT == event.button:
            FahrstrasseController().toggle_fahrstrasse(self.model)


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
