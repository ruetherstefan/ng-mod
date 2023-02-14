from src.view.GleisView import *
from src.view.WeicheView import *
from src.view.GleisViewSchrauber import GleisViewSchrauber
from src.model.weiche.Weichenadresse import Weichenadresse


class Streckenmaler:

    def __init__(self, models):
        self.strecke_y = 9
        self.strecke_x = 20
        self.models = models

    def plane_ennepetal_view(self):
        gleise = self.erstelle_haupt_und_schattenbahnhof()
        gleise.extend(self.erstelle_ebene1_hinten())
        gleise.extend(self.erstelle_ebene2())

        return gleise

    def erstelle_haupt_und_schattenbahnhof(self, ):
        haupt1 = GleisViewHorizontal()
        haupt1.set_position_index([self.strecke_x, self.strecke_y])
        gleise = GleisViewSchrauber().neu(haupt1) \
            .linker_nachbar(WeicheViewLinksNachUnten(self.get_model(Weichenadresse.W20))) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewRechtsNachUnten()) \
            .links_unten_nachbar(WeicheViewLinksUntenNachOben(self.get_model(Weichenadresse.W24))) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(WeicheViewRechtsNachOben(self.get_model(Weichenadresse.W23))) \
            .rechter_nachbar(WeicheViewLinksNachOben(self.get_model(Weichenadresse.W22))) \
            .rechter_nachbar(GleisViewLinksNachUnten()) \
            .rechts_unten_nachbar(WeicheViewRechtsUntenNachOben(self.get_model(Weichenadresse.W21))) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(WeicheViewLinksNachOben(self.get_model(Weichenadresse.W25))) \
 \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(WeicheViewLinksUntenNachOben(self.get_model(Weichenadresse.W26))) \
            .links_unten_nachbar(GleisViewUntenNachRechts()) \
            .unterer_nachbar(GleisViewVertikal()) \
            .unterer_nachbar(GleisViewVertikal()) \
            .unterer_nachbar(GleisViewVertikal()) \
            .unterer_nachbar(GleisViewVertikal()) \
            .unterer_nachbar(GleisViewVertikal()) \
            .unterer_nachbar(GleisViewVertikal()) \
            .unterer_nachbar(GleisViewVertikal()) \
            .unterer_nachbar(GleisViewVertikal()) \
            .unterer_nachbar(GleisViewVertikal()) \
            .unterer_nachbar(GleisViewVertikal()) \
            .unterer_nachbar(GleisViewObenNachRechts()) \
            .rechts_unten_nachbar(GleisViewRechtsNachOben()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
 \
            .rechter_nachbar(WeicheViewLinksNachOben(self.get_model(Weichenadresse.W1))) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewLinksNachOben()) \
            .rechts_oben_nachbar(WeicheViewRechtsNachUnten(self.get_model(Weichenadresse.W6))) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewLinksNachOben()) \
            .rechts_oben_nachbar(GleisViewObenNachLinks()) \
            .oberer_nachbar(GleisViewVertikal()) \
            .oberer_nachbar(GleisViewVertikal()) \
            .oberer_nachbar(GleisViewVertikal()) \
            .oberer_nachbar(GleisViewVertikal()) \
            .oberer_nachbar(GleisViewUntenNachLinks()) \
            .links_oben_nachbar(GleisViewLinksNachUnten()) \
            .linker_nachbar(WeicheViewRechtsNachUnten(self.get_model(Weichenadresse.Undefiniert))) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewRechtsNachUnten()) \
 \
            .links_unten_nachbar(GleisViewLinksUntenNachOben()) \
            .rechter_nachbar(GleisViewRechtsNachUnten()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(WeicheViewRechtsObenNachUnten(self.get_model(Weichenadresse.Undefiniert))) \
            .links_unten_nachbar(WeicheViewRechtsObenNachUnten(self.get_model(Weichenadresse.Undefiniert))) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(WeicheViewLinksNachOben(self.get_model(Weichenadresse.W10))) \
            .linker_nachbar(WeicheViewLinksUntenNachOben(self.get_model(Weichenadresse.W9))) \
 \
            .links_unten_nachbar(GleisViewLinksUntenNachOben()) \
            .rechter_nachbar(GleisViewRechtsNachUnten()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(WeicheViewRechtsObenNachUnten(self.get_model(Weichenadresse.Undefiniert))) \
            .links_unten_nachbar(WeicheViewRechtsObenNachUnten(self.get_model(Weichenadresse.Undefiniert))) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(WeicheViewLinksNachOben(self.get_model(Weichenadresse.W8))) \
            .linker_nachbar(WeicheViewLinksUntenNachOben(self.get_model(Weichenadresse.W7))) \
 \
            .links_unten_nachbar(GleisViewLinksUntenNachOben()) \
            .rechter_nachbar(GleisViewRechtsNachUnten()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(WeicheViewRechtsObenNachUnten(self.get_model(Weichenadresse.Undefiniert))) \
            .links_unten_nachbar(GleisViewLinksNachOben()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(WeicheViewLinksNachOben(self.get_model(Weichenadresse.W5))) \
            .linker_nachbar(WeicheViewLinksUntenNachOben(self.get_model(Weichenadresse.W4))) \
 \
            .links_unten_nachbar(WeicheViewLinksNachOben(self.get_model(Weichenadresse.W3))) \
            .linker_nachbar(WeicheViewRechtsNachUnten(self.get_model(Weichenadresse.W2))) \
            .linker_nachbar(GleisViewRechtsNachOben()) \
            .links_oben_nachbar(GleisViewObenNachRechts()) \
            .oberer_nachbar(GleisViewVertikal()) \
            .oberer_nachbar(GleisViewVertikal()) \
            .oberer_nachbar(GleisViewVertikal()) \
            .oberer_nachbar(GleisViewVertikal()) \
            .oberer_nachbar(GleisViewVertikal()) \
            .oberer_nachbar(GleisViewVertikal()) \
            .oberer_nachbar(GleisViewUntenNachRechts()) \
            .rechts_oben_nachbar(GleisViewRechtsNachUnten()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewLinksNachOben()) \
            .rechts_oben_nachbar(GleisViewObenNachLinks()) \
            .oberer_nachbar(GleisViewUntenNachLinks()) \
            .ende()
        return gleise

    def erstelle_ebene1_hinten(self, ):
        ebene1hintenbeginn = GleisViewObenNachLinks()
        ebene1hintenbeginn.set_position_index([self.strecke_x + 2, self.strecke_y])

        ebene1hinten = GleisViewSchrauber().neu(ebene1hintenbeginn) \
            .oberer_nachbar(GleisViewVertikal()) \
            .oberer_nachbar(GleisViewUntenNachLinks()) \
            .links_oben_nachbar(GleisViewLinksNachUnten()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(WeicheViewLinksNachOben(self.get_model(Weichenadresse.W30))) \
            .linker_nachbar(WeicheViewRechtsNachUnten(self.get_model(Weichenadresse.W29))) \
            .links_unten_nachbar(GleisViewLinksNachOben()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(WeicheViewLinksUntenNachOben(self.get_model(Weichenadresse.W27))) \
            .links_unten_nachbar(GleisViewUntenNachRechts()) \
            .unterer_nachbar(GleisViewVertikal()) \
            .unterer_nachbar(GleisViewObenNachLinks()) \
            .ende()

        oberer_teil_gleis1 = GleisViewHorizontal()
        oberer_teil_gleis1.set_position_index([self.strecke_x - 8, self.strecke_y - 3])
        oberer_teil = GleisViewSchrauber().neu(oberer_teil_gleis1) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(WeicheViewRechtsNachOben(self.get_model(Weichenadresse.W28))) \
            .linker_nachbar(GleisViewRechtsNachUnten()) \
            .oberer_nachbar(GleisViewLinksNachUnten()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .ende()

        ebene1hinten.extend(oberer_teil)

        return ebene1hinten

    def erstelle_ebene2(self, ):
        ebene2beginn = GleisViewRechtsNachUnten()
        ebene2beginn.set_position_index([self.strecke_x - 5, self.strecke_y - 4])

        ebene2 = GleisViewSchrauber().neu(ebene2beginn) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewLinksNachOben()) \
            .rechts_oben_nachbar(GleisViewObenNachLinks()) \
            .oberer_nachbar(GleisViewVertikal()) \
            .oberer_nachbar(GleisViewUntenNachLinks()) \
            .links_oben_nachbar(GleisViewLinksNachUnten()) \
            .linker_nachbar(WeicheViewRechtsNachOben(self.get_model(Weichenadresse.Undefiniert))) \
            .linker_nachbar(WeicheViewRechtsNachUnten(self.get_model(Weichenadresse.Undefiniert))) \
            .links_unten_nachbar(GleisViewLinksNachOben()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .links_oben_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechts_oben_nachbar(GleisViewLinksNachUnten()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewRechtsNachUnten()) \
            .links_unten_nachbar(WeicheViewLinksNachOben(self.get_model(Weichenadresse.Undefiniert))) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(WeicheViewRechtsNachUnten(self.get_model(Weichenadresse.Undefiniert))) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .linker_nachbar(GleisViewHorizontal()) \
            .unterer_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewHorizontal()) \
            .rechter_nachbar(GleisViewLinksNachOben()) \
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

