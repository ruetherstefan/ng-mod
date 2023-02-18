from src.controller.Streckenplaner import Streckenplaner
from src.main.stellpult import Stellpult
from src.model.BesetztModul import BesetztModul, BesetztModulVerwalter
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.zug.Lok import Lok
from src.model.zug.SpeedModifier import SpeedModifier
from src.model.zug.Zug import Zug
from src.view.Streckenmaler import Streckenmaler


def get_besetzt_module():
    return BesetztModulVerwalter({BesetztModul(BesetztModulAdresse.H1),
                                  BesetztModul(BesetztModulAdresse.H2),
                                  BesetztModul(BesetztModulAdresse.H3)})


def get_zug():
    zug_2015: Zug = Zug()
    zug_2015.ende = BesetztModulAdresse.H1
    zug_2015.anfang = BesetztModulAdresse.H1
    zug_2015.speeds = {SpeedModifier.STRECKE_GERADE: 15,
                       SpeedModifier.BAHNHOF_FAHRT: 8}
    zug_2015.lok = Lok(215)
    return zug_2015


ennepetal_model = Streckenplaner().plane_ennepetal_model()
ennepetal_view = Streckenmaler(ennepetal_model).plane_ennepetal_view()
besetzt_modul_verwalter: BesetztModulVerwalter = get_besetzt_module()
zug = get_zug()

stellpult = Stellpult(ennepetal_model, ennepetal_view, besetzt_modul_verwalter, zug)
stellpult.run()