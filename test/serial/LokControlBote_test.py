from unittest.mock import Mock

from src.serial.LokControlBote import LokControlBote


def test_mock_wenn_offline():
    assert isinstance(LokControlBote().lok_control, Mock)
