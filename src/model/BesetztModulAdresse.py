from enum import Enum, auto


class BesetztModulAdresse(Enum):
    B001_HAUPT_AUSFAHRT_LINKS = auto()
    B002_HAUPT_AUSFAHRT_RECHTS_G1_SCHATTEN = auto()
    B003_HAUPT_AUSFAHRT_RECHTS_G2_UND_G3_GUETER = auto()

    B011_HAUPT_G1_HALTE_LINKS = auto()
    B012_HAUPT_G1_MITTE = auto()
    B013_HAUPT_G1_HALTE_RECHTS = auto()

    B021_HAUPT_G2_HALTE_LINKS = auto()
    B022_HAUPT_G2_MITTE = auto()
    B023_HAUPT_G2_HALTE_RECHTS = auto()

    B031_HAUPT_G3_HALTE_LINKS = auto()
    B032_HAUPT_G3_MITTE = auto()
    B033_HAUPT_G3_HALTE_RECHTS = auto()

    NOCH_NICHT_BESTIMMT = auto()
