from src.baustein.Gleis import *
from src.baustein.Baustein import Gleisschrauber


class Streckenplaner:

    def plane_ennepetal(self, screen):
        gleis1 = GleisHorizontal(screen)
        gleis1.set_position_index([23, 9])

        # Hauptbahnhof
        gleise = Gleisschrauber().neu(gleis1) \
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













#gleis2 = GleisVertikal(screen)
#gleis2.set_position_index([gleis1.get_position_index()[0] + 1, gleis1.get_position_index()[1] + 1])

#abschnitt2 = Gleisschrauber().neu(gleis2)\
#    .unterer_nachbar(GleisObenNachLinks(screen))\
#gleise.extend(abschnitt2)