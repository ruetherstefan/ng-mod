from src.model.Weichenstellung import Weichenstellung
from src.serial.WeichenControlBote import WeichenControlBote


class WeichenstellungController:
    def aendere_weichenstellung(self, weiche):
        if Weichenstellung.GERADE == weiche.weichenstellung:
            weiche.weichenstellung = Weichenstellung.ABZWEIGEND
        else:
            weiche.weichenstellung = Weichenstellung.GERADE
        WeichenControlBote().aendere_weichenstellung(weiche.adresse, weiche.weichenstellung)
