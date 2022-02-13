from src.model.Weichenstellung import Weichenstellung
from src.serial.WeichenControlBote import WeichenControlBote


class Weichenstellungscontroller:
    def aendere_weichenstellung(self, model):
        if model.weichenstellung == Weichenstellung.GERADE:
            model.weichenstellung = Weichenstellung.ABZWEIGEND
        else:
            model.weichenstellung = Weichenstellung.GERADE
        WeichenControlBote().aendere_weichenstellung(model.adresse, model.weichenstellung)