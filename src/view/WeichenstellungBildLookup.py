from src.view.Baustein import Baustein
from src.baustein.Gleisbelegung import Gleisbelegung

from enum import Enum

from src.util.Bilder import Bilder


class Markierungsart(Enum):
    LINKS_MITTE = 1
    LINKS_OBEN = 2
    LINKS_UNTEN = 3
    RECHTS_MITTE = 4
    RECHTS_OBEN = 5
    RECHTS_UNTEN = 6
    MITTE_HORIZONTAL = 7
    MITTE_VERTIKAL = 8


class WeichenstellungBildLookup:
    def lookup(markierungsart, weichenbelegung):
        return Bilder().get_image(Baustein.bilder_ordner + "Markierungen/"
                                  + WeichenstellungBildLookup.get_bildmodiefier_weichenbelegung(weichenbelegung)
                                  + WeichenstellungBildLookup.get_bildname_zu_markierung(markierungsart))

    @staticmethod
    def get_bildname_zu_markierung(markierungsart):
        bildername_zu_markierungsart = {Markierungsart.LINKS_MITTE : 'WeicheLinksMitte.png',
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
        elif weichenbelegung == Gleisbelegung.BLOCKIERT:
            return "Blockiert"
        else: raise ValueError(weichenbelegung + " ist keine bekannte Weichenstellung")
