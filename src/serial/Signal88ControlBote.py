from unittest.mock import Mock

from src.model.BesetztModul import BesetztModul
from src.serial import SerialConnector
from src.serial.Signal88Control import Signal88Control


class Signal88ControlBote:
    def __init__(self):
        self.signal_88_control = Signal88Control()
        if SerialConnector.is_offline():
            self.signal_88_control = Mock(spec=Signal88Control)

    def update_module(self, besetzt_module: [BesetztModul]):
        return self.signal_88_control.lese_signale(1)
