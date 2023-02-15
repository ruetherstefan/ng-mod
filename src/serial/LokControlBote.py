from unittest.mock import Mock

from src.serial import SerialConnector
from src.serial.LokControl import LokControl


class LokControlBote:
    def __init__(self):
        self.lok_control: LokControl = LokControl()
        if SerialConnector.is_offline():
            self.lok_control = Mock(spec=LokControl)

    def lok_fahre(self, lok):
        self.lok_control.lok_fahre(lok)
