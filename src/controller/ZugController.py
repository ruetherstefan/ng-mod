from src.model.zug.SpeedModifier import SpeedModifier


class ZugController:

    @staticmethod
    def update_zug_position(zug, fahrstrecke):
        zug_anfang_modul_nummer: int = fahrstrecke.besetzt_module.index(zug.anfang)
        while zug_anfang_modul_nummer + 1 < len(fahrstrecke.besetzt_module) \
                and fahrstrecke.besetzt_module[zug_anfang_modul_nummer + 1].besetzt:
            zug_anfang_modul_nummer += 1
        zug.anfang = fahrstrecke.besetzt_module[zug_anfang_modul_nummer]
        if not zug.anfang.besetzt:
            zug.anfang = None

        zug_ende_modul_nummer: int = fahrstrecke.besetzt_module.index(zug.ende)
        while zug_ende_modul_nummer + 1 < len(fahrstrecke.besetzt_module) \
                and not fahrstrecke.besetzt_module[zug_ende_modul_nummer].besetzt:
            zug_ende_modul_nummer += 1

        zug.ende = fahrstrecke.besetzt_module[zug_ende_modul_nummer]
        if not zug.ende.besetzt:
            zug.ende = None

    @staticmethod
    def update_zug_speed(zug, fahrstrecke):
        if zug.anfang not in fahrstrecke.speed_modifier:
            zug.lok.speed = zug.speeds[SpeedModifier.STRECKE_GERADE]
        else:
            if fahrstrecke.speed_modifier[zug.anfang] == SpeedModifier.BAHNHOF_STOP:
                zug.lok.speed = 0
            else:
                zug.lok.speed = zug.speeds[fahrstrecke.speed_modifier[zug.anfang]]
