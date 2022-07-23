from unittest.mock import patch

from serial.tools.list_ports_common import ListPortInfo

from src.serial import SerialConnector


@patch('serial.tools.list_ports.comports')
def test_noports_is_offline(list_ports):
    list_ports.return_value = []
    assert SerialConnector.is_offline() is True


@patch('serial.tools.list_ports.comports')
def test_nur_jans_remotebootports_is_offline(list_ports):
    list_port_info = ListPortInfo('COM3')
    list_port_info.description = 'Intel(R) Active Management Technology - SOL (COM3)'
    list_port_info.hwid = 'PCI\\VEN_8086&DEV_06E3&SUBSYS_09C11028&REV_00\\3&11583659&0&B3'
    list_ports.return_value = [list_port_info]

    assert SerialConnector.is_offline() is True


@patch('serial.tools.list_ports.comports')
def test_unbekannterport_is_vorerst_online(list_ports):
    list_port_info = ListPortInfo('COM3')
    list_port_info.description = 'Für den Test vorerst valider Port'
    list_port_info.hwid = 'xyz'
    list_ports.return_value = [list_port_info]

    assert SerialConnector.is_offline() is False
