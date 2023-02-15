from src.controller.ZugController import ZugController
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.zug.Fahrstrecke import Fahrstrecke
from src.model.zug.Lok import Lok
from src.model.zug.SpeedModifier import SpeedModifier
from src.model.zug.Zug import Zug


def gegeben_zug_mit_anfang(besetzt_modul):
    zug: Zug = Zug()
    zug.anfang = besetzt_modul
    zug.lok = Lok(42)
    return zug


def gegeben_fahrstrecke_mit_einem_modul():
    fahrstrecke: Fahrstrecke = Fahrstrecke()
    fahrstrecke.besetzt_module = [BesetztModulAdresse.H1]
    return fahrstrecke


def test_update_zug_speed_strecke_gerade():
    fahrstrecke = gegeben_fahrstrecke_mit_einem_modul()
    zug = gegeben_zug_mit_anfang(BesetztModulAdresse.H1)

    fahrstrecke.speed_modifier = {}
    zug.speeds = {SpeedModifier.STRECKE_GERADE: 10}

    ZugController().update_zug_speed(zug, fahrstrecke)
    assert zug.lok.speed == zug.speeds[SpeedModifier.STRECKE_GERADE]


def test_update_zug_speed_strecke_abwaerts():
    fahrstrecke = gegeben_fahrstrecke_mit_einem_modul()
    zug = gegeben_zug_mit_anfang(BesetztModulAdresse.H1)

    fahrstrecke.speed_modifier = {BesetztModulAdresse.H1: SpeedModifier.STRECKE_ABWAERTS}
    zug.speeds = {SpeedModifier.STRECKE_ABWAERTS: 7,
                  SpeedModifier.STRECKE_AUFWAERTS: 15}

    ZugController().update_zug_speed(zug, fahrstrecke)
    assert zug.lok.speed == zug.speeds[SpeedModifier.STRECKE_ABWAERTS]


def test_update_zug_speed_strecke_aufwaerts():
    fahrstrecke = gegeben_fahrstrecke_mit_einem_modul()
    zug = gegeben_zug_mit_anfang(BesetztModulAdresse.H1)

    fahrstrecke.speed_modifier = {BesetztModulAdresse.H1: SpeedModifier.STRECKE_AUFWAERTS}
    zug.speeds = {SpeedModifier.STRECKE_ABWAERTS: 7,
                  SpeedModifier.STRECKE_AUFWAERTS: 15}

    ZugController().update_zug_speed(zug, fahrstrecke)
    assert zug.lok.speed == zug.speeds[SpeedModifier.STRECKE_AUFWAERTS]


def test_update_zug_speed_bahnhof_stop():
    fahrstrecke = gegeben_fahrstrecke_mit_einem_modul()
    zug = gegeben_zug_mit_anfang(BesetztModulAdresse.H1)

    fahrstrecke.speed_modifier = {BesetztModulAdresse.H1: SpeedModifier.BAHNHOF_STOP}
    zug.speeds = {}

    ZugController().update_zug_speed(zug, fahrstrecke)
    assert zug.lok.speed == 0
