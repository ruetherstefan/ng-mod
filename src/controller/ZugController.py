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
                zug_ende_modul_nummer += 1

            zug.ende = fahrstrecke.besetzt_module[zug_ende_modul_nummer]
        else:
            zug.anfang = None
            zug.ende = None

    @staticmethod
    def update_zug_speed(zug: Zug, fahrstrecke: Fahrstrecke):
        if zug.anfang not in fahrstrecke.speed_modifier:
            zug.lok.speed = zug.speeds[SpeedModifier.STRECKE_GERADE]
        else:
            if fahrstrecke.speed_modifier[zug.anfang] == SpeedModifier.BAHNHOF_STOP:
                zug.lok.speed = 0
            else:
                zug.lok.speed = zug.speeds[fahrstrecke.speed_modifier[zug.anfang]]
