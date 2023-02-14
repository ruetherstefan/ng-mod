from src.view.BausteinView import BausteinView
from src.util.Bilder import Bilder


class GleisViewHorizontal(BausteinView):

    def __init__(self):
        super().__init__()

        self.bild = Bilder().get_image("spdritem_trh.xpm")


class GleisViewVertikal(BausteinView):

    def __init__(self):
        super().__init__()

        self.bild = Bilder().get_image("gleis_vertical.png")


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
