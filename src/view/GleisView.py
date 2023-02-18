from src.model.BesetztModul import BesetztModul
from src.util.Bilder import Bilder
from src.view.BausteinView import BausteinView


class GleisView(BausteinView):
    def draw(self, screen):
        super().draw(screen)
        if self.model is not None:
            screen.blit(Bilder().get_image(
                "Markierungen/" + self.get_bildmodiefier_weichenbelegung(self.model) + self.gleis_markierung_bild),
                self.get_position())

    @staticmethod
    def get_bildmodiefier_weichenbelegung(model):
        if model.besetzt:
            return "Besetzt"
        elif model.fahrstrasse:
            return "Fahrstrasse"
        else:
            return ""


class GleisViewHorizontal(GleisView):

    def __init__(self, besetztmodul=None):
        super().__init__()

        self.bild = Bilder().get_image("spdritem_trh.xpm")

        self.gleis_markierung_bild = "GleisHorizontal.png"
        self.model: BesetztModul = besetztmodul


class GleisViewVertikal(GleisView):

    def __init__(self, besetztmodul=None):
        super().__init__()

        self.bild = Bilder().get_image("gleis_vertical.png")

        self.gleis_markierung_bild = "GleisVertikal.png"
        self.model = besetztmodul


class GleisViewUntenNachRechts(BausteinView):

    def __init__(self):
        super().__init__()

        self.bild = Bilder().get_image("spdritem_cr2.xpm")


class GleisViewUntenNachLinks(BausteinView):

    def __init__(self):
        super().__init__()

        self.bild = Bilder().get_image("spdritem_cl2.xpm")


class GleisViewObenNachRechts(BausteinView):

    def __init__(self):
        super().__init__()

        self.bild = Bilder().get_image("spdritem_cl4.xpm")


class GleisViewObenNachLinks(BausteinView):

    def __init__(self):
        super().__init__()

        self.bild = Bilder().get_image("spdritem_cr4.xpm")


class GleisViewLinksNachOben(BausteinView):

    def __init__(self):
        super().__init__()

        self.bild = Bilder().get_image("spdritem_cl1.xpm")


class GleisViewLinksNachUnten(BausteinView):

    def __init__(self):
        super().__init__()

        self.bild = Bilder().get_image("spdritem_cr1.xpm")


class GleisViewRechtsNachOben(BausteinView):
    def __init__(self):
        super().__init__()

        self.bild = Bilder().get_image("spdritem_cr3.xpm")


class GleisViewRechtsNachUnten(BausteinView):
    def __init__(self):
        super().__init__()

        self.bild = Bilder().get_image("spdritem_cl3.xpm")


class GleisViewLinksUntenNachOben(BausteinView):

    def __init__(self):
        super().__init__()

        self.bild = Bilder().get_image("gleis_von_links_unten_nach_rechts_oben.png")
