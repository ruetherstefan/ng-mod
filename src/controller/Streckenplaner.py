from src.model.Weiche import Weiche
from src.model.Weichenadresse import Weichenadresse


class Streckenplaner:
    def plane_ennepetal_model(self):
        models = []

        for adresse in Weichenadresse:
            #if adresse is not Weichenadresse.Undefiniert:
            models.append(Weiche(adresse))

        return models
