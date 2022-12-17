from src.controller.WeichenstellungController import WeichenstellungController
from src.model.BesetztModul import BesetztModul
from src.model.Gleisbelegung import Gleisbelegung
from src.model.Weiche import Weiche
from src.model.Weichenstellung import Weichenstellung


class FahrstrasseController:
    @staticmethod
    def alles_frei(besetzt_module: [BesetztModul]):
        for besetzt_modul in besetzt_module:
            if besetzt_modul.besetzt or besetzt_modul.gleisbelegung() != Gleisbelegung.FREI:
                return False
        return True

    @staticmethod
    def keine_weiche_gesperrt(weichenstellungen: {Weiche: Weichenstellung}):
        for weiche in weichenstellungen:
            if weiche.gesperrt:
                return False
        return True

    @staticmethod
    def stelle_fahrstrasse(fahrstrecke):
        if FahrstrasseController().alles_frei(fahrstrecke.besetzt_module) and \
           FahrstrasseController().keine_weiche_gesperrt(fahrstrecke.weichenstellungen):
            for besetztmodel in fahrstrecke.besetzt_module:
                besetztmodel.fahrstrasse = True
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