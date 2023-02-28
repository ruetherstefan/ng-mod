from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.weiche.Weiche import Weiche
from src.model.weiche.Weichenstellung import Weichenstellung
from src.model.zug.SpeedModifier import SpeedModifier
from src.model.zug.Zug import Zug


class Fahrstrecke:
    def __init__(self):
        self.besetzt_module: [BesetztModulAdresse] = []
        self.weichenstellungen: {Weiche: Weichenstellung} = {}
        self.speed_modifier: {BesetztModulAdresse: SpeedModifier} = {}


DEMO_FAHRSTRECKE_HIN = Fahrstrecke()
DEMO_FAHRSTRECKE_HIN.besetzt_module = [BesetztModulAdresse.H1, BesetztModulAdresse.H2, BesetztModulAdresse.H3,
                                       BesetztModulAdresse.H4]
DEMO_FAHRSTRECKE_HIN.speed_modifier = {
    DEMO_FAHRSTRECKE_HIN.besetzt_module[0]: SpeedModifier.BAHNHOF_FAHRT,
    DEMO_FAHRSTRECKE_HIN.besetzt_module[-1]: SpeedModifier.BAHNHOF_STOP}

DEMO_FAHRSTRECKE_ZURUECK = Fahrstrecke()
DEMO_FAHRSTRECKE_ZURUECK.besetzt_module = list(
    reversed(DEMO_FAHRSTRECKE_HIN.besetzt_module))
DEMO_FAHRSTRECKE_ZURUECK.speed_modifier = {
    DEMO_FAHRSTRECKE_ZURUECK.besetzt_module[0]: SpeedModifier.BAHNHOF_FAHRT,
    DEMO_FAHRSTRECKE_ZURUECK.besetzt_module[-1]: SpeedModifier.BAHNHOF_STOP}


def neue_fahrstrecke_mit_richtungswechsel(fahrstrecken: [], strecke: Fahrstrecke, zug: Zug):
    fahrstrecken.append(strecke)
    zug.lok.forwaerts = not zug.lok.forwaerts

    anfang = zug.anfang
    zug.anfang = zug.ende
    zug.ende = anfang
