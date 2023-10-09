from src.model.BesetztModul import BesetztModul, BesetztModulVerwalter
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.weiche.Weiche import Weiche
from src.model.weiche.Weichenadresse import Weichenadresse


class Streckenplaner:
    def plane_ennepetal_model(self, verwalter: BesetztModulVerwalter):
        models = []

        for adresse in Weichenadresse:
            if adresse in [Weichenadresse.W24, Weichenadresse.W25]:
                besetzt_modul = verwalter.get(BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS)
            else:
                besetzt_modul = BesetztModul(BesetztModulAdresse.NOCH_NICHT_BESTIMMT)

            models.append(Weiche(adresse, besetzt_modul))

        return models
