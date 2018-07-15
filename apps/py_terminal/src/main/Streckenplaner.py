from src.baustein.Gleis import *
from src.baustein.Baustein import Gleisschrauber


class Streckenplaner:

    def plane_ennepetal(self, screen):


        gleise = self.erstelle_haupt_und_schattenbahnhof(screen)
        gleise.extend(self.erstelle_ebene1_hinten(screen))

        return gleise

    def erstelle_haupt_und_schattenbahnhof(self, screen):
        # Hauptbahnhof und Schattenbahnhof
        haupt1 = GleisHorizontal(screen)
        haupt1.set_position_index([23, 9])
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
        # Ebene1 hinten
        ebene1hintenbeginn = GleisObenNachLinks(screen)
        ebene1hintenbeginn.set_position_index([25, 9])

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
        return ebene1hinten