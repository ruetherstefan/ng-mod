from src.main.stellpult import Stellpult
from src.model.BesetztModul import BesetztModulVerwalter, BesetztModul
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.weiche.Weiche import Weiche
from src.model.weiche.Weichenadresse import Weichenadresse
from src.model.zug.Lok import Lok
from src.model.zug.SpeedModifier import SpeedModifier
from src.model.zug.Zug import Zug
from src.view.GleisView import *
from src.view.GleisViewSchrauber import GleisViewSchrauber
from src.view.WeicheView import WeicheViewRechtsNachOben, WeicheViewLinksNachOben


def get_besetzt_module() -> BesetztModulVerwalter:
    return BesetztModulVerwalter({BesetztModul(BesetztModulAdresse.H1),
                                  BesetztModul(BesetztModulAdresse.H2),
                                  BesetztModul(BesetztModulAdresse.H3),
                                  BesetztModul(BesetztModulAdresse.H4)})


def get_zug():
    zug_2015: Zug = Zug()
    zug_2015.ende = BesetztModulAdresse.H1
    zug_2015.anfang = BesetztModulAdresse.H1
    zug_2015.speeds = {SpeedModifier.STRECKE_GERADE: 15,
                       SpeedModifier.BAHNHOF_FAHRT: 8}
    zug_2015.lok = Lok(215)
    return zug_2015


def get_model_mit_zwei_weichen(verwalter):
    return [Weiche(Weichenadresse.W1, verwalter.get(BesetztModulAdresse.H3)),
            Weiche(Weichenadresse.W2, verwalter.get(BesetztModulAdresse.H3))]


def get_barmen_view(models):
    haupt1 = GleisViewHorizontal()
    haupt1.set_position_index([12, 12])

    gleise = GleisViewSchrauber().neu(haupt1) \
        .rechter_nachbar(GleisViewHorizontal()) \
        .rechter_nachbar(GleisViewHorizontal()) \
        .rechter_nachbar(WeicheViewRechtsNachOben(get_model(Weichenadresse.W1, models))) \
        .rechter_nachbar(WeicheViewLinksNachOben(get_model(Weichenadresse.W2, models))) \
        .rechts_oben_nachbar(GleisViewObenNachLinks()) \
        .ende()

    return gleise


def get_model(adresse, models):
    result = list(filter(lambda model: model.adresse == adresse, models))
    if len(result) == 1:
        return result[0]
    else:
        # Liste der Elemente muss das gesuchte (nur einmal) enthalten, sonst gab es wohl einen
        # Implementierungsfehler
        raise NotImplementedError


besetzt_modul_verwalter: BesetztModulVerwalter = get_besetzt_module()
barmen_model = get_model_mit_zwei_weichen(besetzt_modul_verwalter)
barmen_view = get_barmen_view(barmen_model)
zug = get_zug()

stellpult = Stellpult(barmen_model, barmen_view, besetzt_modul_verwalter, zug)
stellpult.run()
