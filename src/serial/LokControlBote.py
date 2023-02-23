from copy import copy
from unittest.mock import Mock

from src.model.zug.Lok import Lok
from src.serial import SerialConnector
from src.serial.LokControl import LokControl


class LokControlBote:
    letzte_signale: {str: Lok} = {}

    def __init__(self):
        self.lok_control: LokControl = LokControl()
        if SerialConnector.is_offline():
            self.lok_control = Mock(spec=LokControl)

    def lok_fahre(self, lok: Lok):
        self.lok_control.lok_fahre(lok)
        print("LokFahre", lok.adresse, lok.speed, lok.forwaerts)

    def lok_fahre__dopplungsreduziert(self, lok: Lok):
        if lok.adresse not in LokControlBote.letzte_signale or \
                not lok == LokControlBote.letzte_signale[lok.adresse]:
            self.lok_fahre(lok)
            LokControlBote.letzte_signale[lok.adresse] = copy(lok)
