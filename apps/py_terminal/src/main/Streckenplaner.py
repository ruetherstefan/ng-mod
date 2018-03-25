from src.baustein.Gleis import *
from src.baustein.Baustein import Gleisschrauber


class Streckenplaner:

    def plane_ennepetal(self, screen):
        gleis1 = GleisHorizontal(screen)
        gleis1.set_position_index([25, 10])

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
            .rechts_unten_nachbar(WeicheLinksUntenNachOben(screen)) \
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
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .linker_nachbar(GleisHorizontal(screen)) \
            .ende()
        return gleise













#gleis2 = GleisVertikal(screen)
#gleis2.set_position_index([gleis1.get_position_index()[0] + 1, gleis1.get_position_index()[1] + 1])

#abschnitt2 = Gleisschrauber().neu(gleis2)\
#    .unterer_nachbar(GleisObenNachLinks(screen))\
#gleise.extend(abschnitt2)