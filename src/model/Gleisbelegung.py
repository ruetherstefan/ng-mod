from enum import Enum, auto


class Gleisbelegung(Enum):
    FREI = auto()
    FAHRSTRASSE = auto()
    BESETZT = auto()
    GESPRERRT = auto()
