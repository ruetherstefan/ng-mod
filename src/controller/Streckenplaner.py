from src.model.BesetztModul import BesetztModul
from src.model.Weiche import Weiche
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.Weichenadresse import Weichenadresse


class Streckenplaner:
    def plane_ennepetal_model(self):
        models = []

        besetzt_modul = BesetztModul(BesetztModulAdresse.NOCH_NICHT_BESTIMMT)
        for adresse in Weichenadresse:
            models.append(Weiche(adresse, besetzt_modul))

        return models
