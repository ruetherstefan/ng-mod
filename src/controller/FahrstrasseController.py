from src.controller.WeichenstellungController import WeichenstellungController
from src.model.BesetztModul import BesetztModulVerwalter
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.Gleisbelegung import Gleisbelegung
from src.model.weiche.Weiche import Weiche
from src.model.weiche.Weichenstellung import Weichenstellung
from src.model.zug.Fahrstrecke import Fahrstrecke


class FahrstrasseController:
    @staticmethod
    def alles_frei(besetzt_module: [BesetztModulAdresse], verwalter: BesetztModulVerwalter):
        for adresse in besetzt_module:
            modul = verwalter.get(adresse)
            if modul.besetzt or modul.gleisbelegung() != Gleisbelegung.FREI:
                return False
        return True

    @staticmethod
    def keine_weiche_gesperrt(weichenstellungen: {Weiche: Weichenstellung}):
        for weiche in weichenstellungen:
            if weiche.gesperrt:
                return False
        return True

    @staticmethod
    def stelle_fahrstrasse(fahrstrecke: Fahrstrecke, verwalter: BesetztModulVerwalter):
        if FahrstrasseController().alles_frei(fahrstrecke.besetzt_module, verwalter) and \
                FahrstrasseController().keine_weiche_gesperrt(fahrstrecke.weichenstellungen):
            for adresse in fahrstrecke.besetzt_module:
                verwalter.get(adresse).fahrstrasse = True
            for weiche in fahrstrecke.weichenstellungen:
                WeichenstellungController().set_weichenstellung(weiche, fahrstrecke.weichenstellungen[weiche])
            return True
        else:
            return False

    @staticmethod
    def toggle_fahrstrasse(weiche):
        if weiche.gesperrt:
            return
        elif weiche.gleisbelegung() == Gleisbelegung.FREI:
            weiche.besetztmodul.fahrstrasse = True
        else:
            weiche.besetztmodul.fahrstrasse = False
