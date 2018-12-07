from src.baustein.Gleis import *
from src.serial.WeichenControl import *


class WeichenControlBote:
    def aendereWeichenstellung(self, weichenname, tes):
        print(weichenname)
        turnout_set_for_route(b'\01', b'\00', True)
        turnout_free(b'\01', b'\00')
