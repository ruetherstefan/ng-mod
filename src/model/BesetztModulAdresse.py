from enum import Enum, auto


class BesetztModulAdresse(Enum):
    B001_HAUPT_AUSFAHRT_LINKS = auto()
    B011_HAUPT_G1_HALTE_LINKS = auto()
    B012_HAUPT_G1_MITTE = auto()
    B013_HAUPT_G1_HALTE_RECHTS = auto()
    H5 = auto()
    H6 = auto()
    NOCH_NICHT_BESTIMMT = auto()
