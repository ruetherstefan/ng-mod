import serial.tools.list_ports

from src.baustein.Weichenstellung import Weichenstellung
from src.baustein.Weichenadresse import Weichenadresse


class WeichenControlBote:

    weichenadresse_mapping = {Weichenadresse.W1: b'\01',
                              Weichenadresse.W2: b'\02'}

    def aendere_weichenstellung(self, weichenadresse, weichenstellung):
        print(weichenadresse, str(Weichenstellung.GERADE == weichenstellung))
        weichen_control.turnout_set_for_route(self.weichenadresse_mapping.get(weichenadresse), b'\00',
                                              Weichenstellung.GERADE == weichenstellung)
        weichen_control.turnout_free(self.weichenadresse_mapping.get(weichenadresse), b'\00')


offline = serial.tools.list_ports.comports() == []
if offline:
    from src.serial.WeichenControlOffline import WeichenControlOffline
    weichen_control = WeichenControlOffline()
else:
    from src.serial.WeichenControl import WeichenControl
    weichen_control = WeichenControl()
