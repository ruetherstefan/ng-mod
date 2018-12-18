from src.baustein.Weichenstellung import Weichenstellung

import serial.tools.list_ports


class WeichenControlBote:
    def aendere_weichenstellung(self, weichenname, weichenstellung):
        print(weichenname, str(Weichenstellung.GERADE == weichenstellung))
        weichen_control.turnout_set_for_route(b'\01', b'\00', Weichenstellung.GERADE == weichenstellung)
        weichen_control.turnout_free(b'\01', b'\00')


offline = serial.tools.list_ports.comports() == []
if offline:
    from src.serial.WeichenControlOffline import WeichenControlOffline
    weichen_control = WeichenControlOffline()
else:
    from src.serial.WeichenControl import WeichenControl
    weichen_control = WeichenControl()
