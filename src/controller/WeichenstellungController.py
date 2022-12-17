from src.model.Weichenstellung import Weichenstellung
from src.serial.WeichenControlBote import WeichenControlBote


class WeichenstellungController:
    @staticmethod
    def aendere_weichenstellung(weiche):
        if Weichenstellung.GERADE == weiche.weichenstellung:
            WeichenstellungController.set_weichenstellung(weiche, Weichenstellung.ABZWEIGEND)
        else:
            WeichenstellungController.set_weichenstellung(weiche, Weichenstellung.GERADE)

    @staticmethod
    def set_weichenstellung(weiche, wunsch_weichenstellung):
        weiche.weichenstellung = wunsch_weichenstellung
        WeichenControlBote().aendere_weichenstellung(weiche.adresse, weiche.weichenstellung)

