from src.baustein.Baustein import Baustein

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
        return Bilder().get_image(Baustein.bilder_ordner + "Markierungen/WeicheRechtsMitte.png")

    #self.markierung_links_mitte = get_image(Baustein.bilder_ordner + "Markierungen/WeicheLinksMitte.png")
        #self.markierung_links_oben = get_image(Baustein.bilder_ordner + "Markierungen/WeicheLinksOben.png")
        #self.markierung_links_unten = get_image(Baustein.bilder_ordner + "Markierungen/WeicheLinksUnten.png")
        #self.markierung_rechts_mitte = get_image(Baustein.bilder_ordner + "Markierungen/WeicheRechtsMitte.png")
        #self.markierung_rechts_oben = get_image(Baustein.bilder_ordner + "Markierungen/WeicheRechtsOben.png")
        #self.markierung_rechts_unten = get_image(Baustein.bilder_ordner + "Markierungen/WeicheRechtsUnten.png")