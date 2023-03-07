from src.model.BesetztModul import BesetztModulVerwalter
from src.model.zug.Fahrstrecke import Fahrstrecke
from src.model.zug.SpeedModifier import SpeedModifier
from src.model.zug.Zug import Zug


class ZugController:

    @staticmethod
    def update_zug_position(zug: Zug, fahrstrecke: Fahrstrecke, verwalter: BesetztModulVerwalter):
        if zug.anfang is None:
            zug.anfang = fahrstrecke.besetzt_module[0]
            zug.ende = fahrstrecke.besetzt_module[0]

        zug_anfang_modul_nummer: int = fahrstrecke.besetzt_module.index(zug.anfang)
        while zug_anfang_modul_nummer + 1 < len(fahrstrecke.besetzt_module) \
                and verwalter.get(fahrstrecke.besetzt_module[zug_anfang_modul_nummer + 1]).besetzt:
            zug_anfang_modul_nummer += 1
        zug.anfang = fahrstrecke.besetzt_module[zug_anfang_modul_nummer]

        if verwalter.get(zug.anfang).besetzt:
            zug_ende_modul_nummer: int = fahrstrecke.besetzt_module.index(zug.ende)
            while zug_ende_modul_nummer + 1 < len(fahrstrecke.besetzt_module) \
                    and not verwalter.get(fahrstrecke.besetzt_module[zug_ende_modul_nummer]).besetzt:
                verwalter.get(fahrstrecke.besetzt_module[zug_ende_modul_nummer]).fahrstrasse = False
                zug_ende_modul_nummer += 1

            zug.ende = fahrstrecke.besetzt_module[zug_ende_modul_nummer]
        else:
            zug.anfang = None
            zug.ende = None

    @staticmethod
    def update_zug_speed(zug: Zug, fahrstrecke: Fahrstrecke):
        speed_zugende = ZugController.berechne_geschwindigkeit_an_adresse(zug.anfang, fahrstrecke, zug)
        speed_zuganfang = ZugController.berechne_geschwindigkeit_an_adresse(zug.ende, fahrstrecke, zug)
        zug.lok.speed = min(speed_zuganfang, speed_zugende)

    @staticmethod
    def berechne_geschwindigkeit_an_adresse(besetzt_modul_adresse, fahrstrecke, zug):
        if besetzt_modul_adresse not in fahrstrecke.speed_modifier:
            return zug.speeds[SpeedModifier.STRECKE_GERADE]
        else:
            if fahrstrecke.speed_modifier[besetzt_modul_adresse] == SpeedModifier.BAHNHOF_STOP:
                return 0
            else:
                return zug.speeds[fahrstrecke.speed_modifier[besetzt_modul_adresse]]
