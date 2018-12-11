from src.baustein.Gleis import *
from src.baustein.Weiche import *
from src.baustein.Baustein import Gleisschrauber


class Streckenplaner:

    def __init__(self):
        self.strecke_y = 9
        self.strecke_x = 20

    def plane_ennepetal(self, screen):


        gleise = self.erstelle_haupt_und_schattenbahnhof(screen)
        gleise.extend(self.erstelle_ebene1_hinten(screen))
        gleise.extend(self.erstelle_ebene2(screen))

        return gleise

    def erstelle_haupt_und_schattenbahnhof(self, screen):
        haupt1 = GleisHorizontal(screen)
        haupt1.set_position_index([self.strecke_x, self.strecke_y])
        gleise = Gleisschrauber().neu(haupt1) \
            .linker_nachbar(WeicheLinksNachUnten(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisRechtsNachUnten(screen)) \
            .links_unten_nachbar(WeicheLinksUntenNachOben(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(WeicheRechtsNachOben(screen)) \
            .rechter_nachbar(WeicheLinksNachOben(screen)) \
            .rechter_nachbar(GleisLinksNachUnten(screen)) \
            .rechts_unten_nachbar(WeicheRechtsUntenNachOben(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(WeicheLinksNachOben(screen)) \
 \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(WeicheLinksUntenNachOben(screen)) \
            .links_unten_nachbar(GleisUntenNachRechts(screen)) \
            .unterer_nachbar(GleisVertikal(screen)) \
            .unterer_nachbar(GleisVertikal(screen)) \
            .unterer_nachbar(GleisVertikal(screen)) \
            .unterer_nachbar(GleisVertikal(screen)) \
            .unterer_nachbar(GleisVertikal(screen)) \
            .unterer_nachbar(GleisVertikal(screen)) \
            .unterer_nachbar(GleisVertikal(screen)) \
            .unterer_nachbar(GleisVertikal(screen)) \
            .unterer_nachbar(GleisVertikal(screen)) \
            .unterer_nachbar(GleisVertikal(screen)) \
            .unterer_nachbar(GleisObenNachRechts(screen)) \
            .rechts_unten_nachbar(GleisRechtsNachOben(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
 \
            .rechter_nachbar(WeicheLinksNachOben(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisLinksNachOben(screen)) \
            .rechts_oben_nachbar(WeicheRechtsNachUnten(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisLinksNachOben(screen)) \
            .rechts_oben_nachbar(GleisObenNachLinks(screen)) \
            .oberer_nachbar(GleisVertikal(screen)) \
            .oberer_nachbar(GleisVertikal(screen)) \
            .oberer_nachbar(GleisVertikal(screen)) \
            .oberer_nachbar(GleisVertikal(screen)) \
            .oberer_nachbar(GleisUntenNachLinks(screen)) \
            .links_oben_nachbar(GleisLinksNachUnten(screen)) \
            .linker_nachbar(WeicheRechtsNachUnten(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisRechtsNachUnten(screen)) \
            .links_unten_nachbar(WeicheLinksUntenNachOben(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(WeicheRechtsObenNachUnten(screen)) \
            .links_unten_nachbar(WeicheRechtsObenNachUnten(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(WeicheLinksUntenNachOben(screen)) \
            .links_unten_nachbar(WeicheLinksUntenNachOben(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(WeicheRechtsObenNachUnten(screen)) \
            .links_unten_nachbar(WeicheRechtsObenNachUnten(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(WeicheLinksUntenNachOben(screen)) \
            .links_unten_nachbar(WeicheLinksUntenNachOben(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(WeicheRechtsObenNachUnten(screen)) \
            .links_unten_nachbar(GleisLinksNachOben(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(WeicheLinksUntenNachOben(screen)) \
            .links_unten_nachbar(WeicheLinksNachOben(screen)) \
            .linker_nachbar(WeicheRechtsNachUnten(screen)) \
 \
            .linker_nachbar(GleisRechtsNachOben(screen)) \
            .links_oben_nachbar(GleisObenNachRechts(screen)) \
            .oberer_nachbar(GleisVertikal(screen)) \
            .oberer_nachbar(GleisVertikal(screen)) \
            .oberer_nachbar(GleisVertikal(screen)) \
            .oberer_nachbar(GleisVertikal(screen)) \
            .oberer_nachbar(GleisVertikal(screen)) \
            .oberer_nachbar(GleisVertikal(screen)) \
            .oberer_nachbar(GleisUntenNachRechts(screen)) \
            .rechts_oben_nachbar(GleisRechtsNachUnten(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisLinksNachOben(screen)) \
            .rechts_oben_nachbar(GleisObenNachLinks(screen)) \
            .oberer_nachbar(GleisUntenNachLinks(screen)) \
            .ende()
        return gleise

    def erstelle_ebene1_hinten(self, screen):
        ebene1hintenbeginn = GleisObenNachLinks(screen)
        ebene1hintenbeginn.set_position_index([self.strecke_x + 2, self.strecke_y])

        ebene1hinten = Gleisschrauber().neu(ebene1hintenbeginn)\
            .oberer_nachbar(GleisVertikal(screen)) \
            .oberer_nachbar(GleisUntenNachLinks(screen)) \
            .links_oben_nachbar(GleisLinksNachUnten(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(WeicheLinksNachOben(screen)) \
            .linker_nachbar(WeicheRechtsNachUnten(screen)) \
            .links_unten_nachbar(GleisLinksNachOben(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(WeicheLinksUntenNachOben(screen)) \
            .links_unten_nachbar(GleisUntenNachRechts(screen)) \
            .unterer_nachbar(GleisVertikal(screen)) \
            .unterer_nachbar(GleisObenNachLinks(screen)) \
            .ende()

        oberer_teil_gleis1 = GleisHorizontal(screen)
        oberer_teil_gleis1.set_position_index([self.strecke_x - 8, self.strecke_y - 3])
        oberer_teil = Gleisschrauber().neu(oberer_teil_gleis1) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(WeicheRechtsNachOben(screen)) \
            .linker_nachbar(GleisRechtsNachUnten(screen)) \
            .oberer_nachbar(GleisLinksNachUnten(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .ende()

        ebene1hinten.extend(oberer_teil)

        return ebene1hinten

    def erstelle_ebene2(self, screen):
        ebene2beginn = GleisRechtsNachUnten(screen)
        ebene2beginn.set_position_index([self.strecke_x - 5, self.strecke_y - 4])

        ebene2 = Gleisschrauber().neu(ebene2beginn) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisLinksNachOben(screen)) \
            .rechts_oben_nachbar(GleisObenNachLinks(screen)) \
            .oberer_nachbar(GleisVertikal(screen)) \
            .oberer_nachbar(GleisUntenNachLinks(screen)) \
            .links_oben_nachbar(GleisLinksNachUnten(screen)) \
            .linker_nachbar(WeicheRechtsNachOben(screen)) \
            .linker_nachbar(WeicheRechtsNachUnten(screen)) \
            .links_unten_nachbar(GleisLinksNachOben(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .links_oben_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechts_oben_nachbar(GleisLinksNachUnten(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisRechtsNachUnten(screen)) \
            .links_unten_nachbar(WeicheLinksNachOben(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(WeicheRechtsNachUnten(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .unterer_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisHorizontal(screen)) \
            .rechter_nachbar(GleisLinksNachOben(screen)) \
            .ende()

        return ebene2