from src.serial.WeichenControl import *
from src.baustein.Weichenstellung import Weichenstellung


class WeichenControlBote:
    def aendere_weichenstellung(self, weichenname, weichenstellung):
        print(weichenname, str(Weichenstellung.GERADE == weichenstellung))
        turnout_set_for_route(b'\01', b'\00', Weichenstellung.GERADE == weichenstellung)
        turnout_free(b'\01', b'\00')
