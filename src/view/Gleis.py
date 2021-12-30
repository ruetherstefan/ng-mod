from src.view.Baustein import Baustein
from src.util.Bilder import Bilder


class GleisHorizontal(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_trh.xpm")


class GleisVertikal(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "gleis_vertical.png")


class GleisUntenNachRechts(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_cr2.xpm")


class GleisUntenNachLinks(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_cl2.xpm")


class GleisObenNachRechts(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_cl4.xpm")


class GleisObenNachLinks(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_cr4.xpm")


class GleisLinksNachOben(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_cl1.xpm")


class GleisLinksNachUnten(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_cr1.xpm")


class GleisRechtsNachOben(Baustein):
    def __init__(self, screen):
        super().__init__(screen)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_cr3.xpm")


class GleisRechtsNachUnten(Baustein):
    def __init__(self, screen):
        super().__init__(screen)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "spdritem_cl3.xpm")


class GleisLinksUntenNachOben(Baustein):

    def __init__(self, screen):
        super().__init__(screen)

        self.bild = Bilder().get_image(Baustein.bilder_ordner + "gleis_von_links_unten_nach_rechts_oben.png")
