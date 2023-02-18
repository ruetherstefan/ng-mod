from enum import Enum, auto

from src.model.Gleisbelegung import Gleisbelegung
from src.util.Bilder import Bilder


class Markierungsart(Enum):
    LINKS_MITTE = auto()
    LINKS_OBEN = auto()
    LINKS_UNTEN = auto()
    RECHTS_MITTE = auto()
    RECHTS_OBEN = auto()
    RECHTS_UNTEN = auto()
    MITTE_HORIZONTAL = auto()
    MITTE_VERTIKAL = auto()


class WeichenstellungBildLookup:

    @staticmethod
    def lookup(markierungsart, weichenbelegung):
        return Bilder().get_image("Markierungen/"
                                  + WeichenstellungBildLookup.get_bildmodiefier_weichenbelegung(weichenbelegung)
                                  + WeichenstellungBildLookup.get_bildname_zu_markierung(markierungsart))

    @staticmethod
    def get_bildname_zu_markierung(markierungsart):
        bildername_zu_markierungsart = {Markierungsart.LINKS_MITTE: 'WeicheLinksMitte.png',
                                        Markierungsart.LINKS_OBEN: 'WeicheLinksOben.png',
                                        Markierungsart.LINKS_UNTEN: 'WeicheLinksUnten.png',
                                        Markierungsart.RECHTS_MITTE: 'WeicheRechtsMitte.png',
                                        Markierungsart.RECHTS_OBEN: 'WeicheRechtsOben.png',
                                        Markierungsart.RECHTS_UNTEN: 'WeicheRechtsUnten.png'}

        return bildername_zu_markierungsart[markierungsart]

    @staticmethod
    def get_bildmodiefier_weichenbelegung(weichenbelegung):
        if weichenbelegung == Gleisbelegung.FREI:
            return ""
        elif weichenbelegung == Gleisbelegung.FAHRSTRASSE:
            return "Fahrstrasse"
        elif weichenbelegung == Gleisbelegung.GESPRERRT:
            return "Blockiert"  # TODO Anpassen an neue Gleisbelegungen Gesperrt und Besetzt
        else:
            raise ValueError(weichenbelegung + " ist keine bekannte Weichenstellung")
