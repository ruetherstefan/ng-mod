from enum import Enum, auto


class SpeedModifier(Enum):
    STRECKE_GERADE = auto()
    STRECKE_ABWAERTS = auto()
    STRECKE_AUFWAERTS = auto()

    BAHNHOF_FAHRT = auto()
    BAHNHOF_STOP = auto()
    BAHNHOF_DURCHFAHRT = auto()
