from src.view.GleisView import *
from src.view.WeicheView import *
from src.view.GleisViewSchrauber import GleisViewSchrauber
from src.model.weiche.Weichenadresse import Weichenadresse


class Streckenmaler:

    def __init__(self, models):
        self.strecke_y = 9
        self.strecke_x = 20
        self.models = models

    def plane_ennepetal_view(self, screen):
        gleise = self.erstelle_haupt_und_schattenbahnhof(screen)
        gleise.extend(self.erstelle_ebene1_hinten(screen))
        gleise.extend(self.erstelle_ebene2(screen))

        return gleise

    def erstelle_haupt_und_schattenbahnhof(self, screen):
        haupt1 = GleisViewHorizontal(screen)
        haupt1.set_position_index([self.strecke_x, self.strecke_y])
        gleise = GleisViewSchrauber().neu(haupt1) \
            .linker_nachbar(WeicheViewLinksNachUnten(screen, self.get_model(Weichenadresse.W20))) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewRechtsNachUnten(screen)) \
            .links_unten_nachbar(WeicheViewLinksUntenNachOben(screen, self.get_model(Weichenadresse.W24))) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(WeicheViewRechtsNachOben(screen, self.get_model(Weichenadresse.W23))) \
            .rechter_nachbar(WeicheViewLinksNachOben(screen, self.get_model(Weichenadresse.W22))) \
            .rechter_nachbar(GleisViewLinksNachUnten(screen)) \
            .rechts_unten_nachbar(WeicheViewRechtsUntenNachOben(screen, self.get_model(Weichenadresse.W21))) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(WeicheViewLinksNachOben(screen, self.get_model(Weichenadresse.W25))) \
 \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(WeicheViewLinksUntenNachOben(screen, self.get_model(Weichenadresse.W26))) \
            .links_unten_nachbar(GleisViewUntenNachRechts(screen)) \
            .unterer_nachbar(GleisViewVertikal(screen)) \
            .unterer_nachbar(GleisViewVertikal(screen)) \
            .unterer_nachbar(GleisViewVertikal(screen)) \
            .unterer_nachbar(GleisViewVertikal(screen)) \
            .unterer_nachbar(GleisViewVertikal(screen)) \
            .unterer_nachbar(GleisViewVertikal(screen)) \
            .unterer_nachbar(GleisViewVertikal(screen)) \
            .unterer_nachbar(GleisViewVertikal(screen)) \
            .unterer_nachbar(GleisViewVertikal(screen)) \
            .unterer_nachbar(GleisViewVertikal(screen)) \
            .unterer_nachbar(GleisViewObenNachRechts(screen)) \
            .rechts_unten_nachbar(GleisViewRechtsNachOben(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
 \
            .rechter_nachbar(WeicheViewLinksNachOben(screen, self.get_model(Weichenadresse.W1))) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewLinksNachOben(screen)) \
            .rechts_oben_nachbar(WeicheViewRechtsNachUnten(screen, self.get_model(Weichenadresse.W6))) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewLinksNachOben(screen)) \
            .rechts_oben_nachbar(GleisViewObenNachLinks(screen)) \
            .oberer_nachbar(GleisViewVertikal(screen)) \
            .oberer_nachbar(GleisViewVertikal(screen)) \
            .oberer_nachbar(GleisViewVertikal(screen)) \
            .oberer_nachbar(GleisViewVertikal(screen)) \
            .oberer_nachbar(GleisViewUntenNachLinks(screen)) \
            .links_oben_nachbar(GleisViewLinksNachUnten(screen)) \
            .linker_nachbar(WeicheViewRechtsNachUnten(screen, self.get_model(Weichenadresse.Undefiniert))) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewRechtsNachUnten(screen)) \
 \
            .links_unten_nachbar(GleisViewLinksUntenNachOben(screen)) \
            .rechter_nachbar(GleisViewRechtsNachUnten(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(WeicheViewRechtsObenNachUnten(screen, self.get_model(Weichenadresse.Undefiniert))) \
            .links_unten_nachbar(WeicheViewRechtsObenNachUnten(screen, self.get_model(Weichenadresse.Undefiniert))) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(WeicheViewLinksNachOben(screen, self.get_model(Weichenadresse.W10))) \
            .linker_nachbar(WeicheViewLinksUntenNachOben(screen, self.get_model(Weichenadresse.W9))) \
 \
            .links_unten_nachbar(GleisViewLinksUntenNachOben(screen)) \
            .rechter_nachbar(GleisViewRechtsNachUnten(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(WeicheViewRechtsObenNachUnten(screen, self.get_model(Weichenadresse.Undefiniert))) \
            .links_unten_nachbar(WeicheViewRechtsObenNachUnten(screen, self.get_model(Weichenadresse.Undefiniert))) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(WeicheViewLinksNachOben(screen, self.get_model(Weichenadresse.W8))) \
            .linker_nachbar(WeicheViewLinksUntenNachOben(screen, self.get_model(Weichenadresse.W7))) \
 \
            .links_unten_nachbar(GleisViewLinksUntenNachOben(screen)) \
            .rechter_nachbar(GleisViewRechtsNachUnten(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(WeicheViewRechtsObenNachUnten(screen, self.get_model(Weichenadresse.Undefiniert))) \
            .links_unten_nachbar(GleisViewLinksNachOben(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(WeicheViewLinksNachOben(screen, self.get_model(Weichenadresse.W5))) \
            .linker_nachbar(WeicheViewLinksUntenNachOben(screen, self.get_model(Weichenadresse.W4))) \
 \
            .links_unten_nachbar(WeicheViewLinksNachOben(screen, self.get_model(Weichenadresse.W3))) \
            .linker_nachbar(WeicheViewRechtsNachUnten(screen, self.get_model(Weichenadresse.W2))) \
            .linker_nachbar(GleisViewRechtsNachOben(screen)) \
            .links_oben_nachbar(GleisViewObenNachRechts(screen)) \
            .oberer_nachbar(GleisViewVertikal(screen)) \
            .oberer_nachbar(GleisViewVertikal(screen)) \
            .oberer_nachbar(GleisViewVertikal(screen)) \
            .oberer_nachbar(GleisViewVertikal(screen)) \
            .oberer_nachbar(GleisViewVertikal(screen)) \
            .oberer_nachbar(GleisViewVertikal(screen)) \
            .oberer_nachbar(GleisViewUntenNachRechts(screen)) \
            .rechts_oben_nachbar(GleisViewRechtsNachUnten(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewLinksNachOben(screen)) \
            .rechts_oben_nachbar(GleisViewObenNachLinks(screen)) \
            .oberer_nachbar(GleisViewUntenNachLinks(screen)) \
            .ende()
        return gleise

    def erstelle_ebene1_hinten(self, screen):
        ebene1hintenbeginn = GleisViewObenNachLinks(screen)
        ebene1hintenbeginn.set_position_index([self.strecke_x + 2, self.strecke_y])

        ebene1hinten = GleisViewSchrauber().neu(ebene1hintenbeginn) \
            .oberer_nachbar(GleisViewVertikal(screen)) \
            .oberer_nachbar(GleisViewUntenNachLinks(screen)) \
            .links_oben_nachbar(GleisViewLinksNachUnten(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(WeicheViewLinksNachOben(screen, self.get_model(Weichenadresse.W30))) \
            .linker_nachbar(WeicheViewRechtsNachUnten(screen, self.get_model(Weichenadresse.W29))) \
            .links_unten_nachbar(GleisViewLinksNachOben(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(WeicheViewLinksUntenNachOben(screen, self.get_model(Weichenadresse.W27))) \
            .links_unten_nachbar(GleisViewUntenNachRechts(screen)) \
            .unterer_nachbar(GleisViewVertikal(screen)) \
            .unterer_nachbar(GleisViewObenNachLinks(screen)) \
            .ende()

        oberer_teil_gleis1 = GleisViewHorizontal(screen)
        oberer_teil_gleis1.set_position_index([self.strecke_x - 8, self.strecke_y - 3])
        oberer_teil = GleisViewSchrauber().neu(oberer_teil_gleis1) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(WeicheViewRechtsNachOben(screen, self.get_model(Weichenadresse.W28))) \
            .linker_nachbar(GleisViewRechtsNachUnten(screen)) \
            .oberer_nachbar(GleisViewLinksNachUnten(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .ende()

        ebene1hinten.extend(oberer_teil)

        return ebene1hinten

    def erstelle_ebene2(self, screen):
        ebene2beginn = GleisViewRechtsNachUnten(screen)
        ebene2beginn.set_position_index([self.strecke_x - 5, self.strecke_y - 4])

        ebene2 = GleisViewSchrauber().neu(ebene2beginn) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewLinksNachOben(screen)) \
            .rechts_oben_nachbar(GleisViewObenNachLinks(screen)) \
            .oberer_nachbar(GleisViewVertikal(screen)) \
            .oberer_nachbar(GleisViewUntenNachLinks(screen)) \
            .links_oben_nachbar(GleisViewLinksNachUnten(screen)) \
            .linker_nachbar(WeicheViewRechtsNachOben(screen, self.get_model(Weichenadresse.Undefiniert))) \
            .linker_nachbar(WeicheViewRechtsNachUnten(screen, self.get_model(Weichenadresse.Undefiniert))) \
            .links_unten_nachbar(GleisViewLinksNachOben(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .links_oben_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechts_oben_nachbar(GleisViewLinksNachUnten(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewRechtsNachUnten(screen)) \
            .links_unten_nachbar(WeicheViewLinksNachOben(screen, self.get_model(Weichenadresse.Undefiniert))) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(WeicheViewRechtsNachUnten(screen, self.get_model(Weichenadresse.Undefiniert))) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .linker_nachbar(GleisViewHorizontal(screen)) \
            .unterer_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewHorizontal(screen)) \
            .rechter_nachbar(GleisViewLinksNachOben(screen)) \
            .ende()

        return ebene2

    def get_model(self, adresse):
        result = list(filter(lambda model: model.adresse == adresse, self.models))
        if len(result) == 1:
            return result[0]
        else:
            # Liste der Elemente muss das gesuchte (nur einmal) enthalten, sonst gab es wohl einen
            # Implementierungsfehler
            raise NotImplementedError

