from enum import Enum


class Gleisbelegung(Enum):
    FREI = 1
    FAHRSTRASSE = 2
    BESETZT = 3
    GESPRERRT = 4