from src.serial import SerialConnector

from src.model.weiche.Weichenstellung import Weichenstellung
from src.model.weiche.Weichenadresse import Weichenadresse

NEGIERTE_WEICHEN = [Weichenadresse.W2,
                    Weichenadresse.W3,
                    Weichenadresse.W4,
                    Weichenadresse.W5,
                    Weichenadresse.W8,
                    Weichenadresse.W9,
                    Weichenadresse.W10,
                    Weichenadresse.W22,
                    Weichenadresse.W23,
                    Weichenadresse.W28]


class WeichenControlBote:

    weichenadresse_mapping = {
                            Weichenadresse.W1: b'\12',
                            Weichenadresse.W2: b'\14',
                            Weichenadresse.W3: b'\11',
                            Weichenadresse.W4: b'\13',
                            Weichenadresse.W5: b'\20',
                            Weichenadresse.W6: b'\17',
                            Weichenadresse.W7: b'\16',
                            Weichenadresse.W8: b'\15',
                            Weichenadresse.W9: b'\24',
                            Weichenadresse.W10: b'\23',

                            # Ebene 1
                            Weichenadresse.W20: b'\55',
                            Weichenadresse.W21: b'\01',
                            Weichenadresse.W22: b'\02',
                            Weichenadresse.W23: b'\04',
                            Weichenadresse.W24: b'\55',
                            Weichenadresse.W25: b'\05',
                            Weichenadresse.W26: b'\06',
                            Weichenadresse.W27: b'\07',
                            Weichenadresse.W28: b'\10',
                            Weichenadresse.W29: b'\55',
                            Weichenadresse.W30: b'\55',
                            }  # Die Adressen sind in oktal anzugeben.

    def aendere_weichenstellung(self, weichenadresse, weichenstellung):
        # print(weichenadresse, self.weichenadresse_mapping.get(weichenadresse), str(
        #     self.invertiere_weichenstellung(weichenstellung, weichenadresse)))

        weichen_control.turnout_set_for_route(self.weichenadresse_mapping.get(weichenadresse), b'\00',
                                              self.invertiere_weichenstellung(weichenstellung, weichenadresse))
        weichen_control.turnout_free(self.weichenadresse_mapping.get(weichenadresse), b'\00')

    def invertiere_weichenstellung(self, weichenstellung, weichenadresse):
        if weichenadresse in NEGIERTE_WEICHEN:
            return not Weichenstellung.GERADE == weichenstellung
        else:
            return Weichenstellung.GERADE == weichenstellung


if SerialConnector.is_offline():
    from src.serial.WeichenControlOffline import WeichenControlOffline

    weichen_control = WeichenControlOffline()
else:
    from src.serial.WeichenControl import WeichenControl

    weichen_control = WeichenControl()
