from unittest.mock import Mock

from src.model.BesetztModul import BesetztModul
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.serial.Signal88ControlBote import Signal88ControlBote


def test_mock_wenn_offline():
    assert isinstance(Signal88ControlBote().signal_88_control, Mock)


def test_update_module__keine_aenderung():
    bote: Signal88ControlBote = Signal88ControlBote()
    bote.signal_88_control.lese_signale = Mock(return_value=[False, False])

    besetzt_module: [BesetztModul] = [BesetztModul(BesetztModulAdresse.H1)]
    assert [False, False] == bote.update_module(besetzt_module)
