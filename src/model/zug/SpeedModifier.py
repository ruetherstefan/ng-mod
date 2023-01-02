from enum import Enum


class SpeedModifier(Enum):
    STRECKE_GERADE = 1
    STRECKE_ABWAERTS = 2
    STRECKE_AUFWAERTS = 3

    BAHNHOF_FAHRT = 4
    BAHNHOF_STOP = 5
    BAHNHOF_DURCHFAHRT = 6
