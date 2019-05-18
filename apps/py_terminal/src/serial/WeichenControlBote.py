import serial.tools.list_ports

from src.baustein.Weichenstellung import Weichenstellung
from src.baustein.Weichenadresse import Weichenadresse


class WeichenControlBote:

    weichenadresse_mapping = {
                            Weichenadresse.W1: b'\09',
                            Weichenadresse.W2: b'\10',
                            Weichenadresse.W3: b'\11',
                            Weichenadresse.W4: b'\12',
                            Weichenadresse.W5: b'\13',
                            Weichenadresse.W6: b'\14',
                            Weichenadresse.W7: b'\15',
                            Weichenadresse.W8: b'\16',
                            Weichenadresse.W9: b'\19',
                            Weichenadresse.W10: b'\20',

                            # Ebene 1
                            Weichenadresse.W20: b'\01',
                            Weichenadresse.W21: b'\01',
                            Weichenadresse.W22: b'\02',
                            Weichenadresse.W23: b'\03',
                            Weichenadresse.W24: b'\04',
                            Weichenadresse.W25: b'\05',
                            Weichenadresse.W26: b'\06',
                            Weichenadresse.W27: b'\07',
                            Weichenadresse.W28: b'\08',
                            Weichenadresse.W29: b'\01',
                            Weichenadresse.W30: b'\01',
                            }

    def aendere_weichenstellung(self, weichenadresse, weichenstellung):
        print(weichenadresse, self.weichenadresse_mapping.get(weichenadresse), str(Weichenstellung.GERADE == weichenstellung))
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
