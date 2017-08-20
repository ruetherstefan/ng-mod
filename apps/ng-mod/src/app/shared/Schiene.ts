export interface Baustein {
  bildAdresse: String;
}

function gibBildordner() {
  return "../assets/img/";
}

export class Leer implements Baustein {
  bildAdresse: String;

  constructor() {
    this.bildAdresse = gibBildordner() + "leer.png"
  }

}

export class Gleis implements Baustein {
  bildAdresse: String;

  constructor(richtung: Richtung) {
    this.bildAdresse = this.gibBidZuRichtung(richtung);
  }

  gibBidZuRichtung(richtung: Richtung) {
    switch (richtung) {
      case Richtung.HORIZONTAL :
        return gibBildordner() + "gleis_horizontal.png";
      case Richtung.VERTICAL :
        return gibBildordner() + "gleis_vertical.png";

      case Richtung.VON_LINKS_NACH_RECHTS_OBEN :
        return gibBildordner() + "gleis_von_links_nach_rechts_oben.png";
      case Richtung.VON_LINKS_NACH_RECHTS_UNTEN :
        return gibBildordner() + "gleis_von_links_nach_rechts_unten.png";
      case Richtung.VON_OBEN_NACH_LINKS_UNTEN :
        return gibBildordner() + "gleis_von_oben_nach_links_unten.png";
      case Richtung.VON_OBEN_NACH_RECHTS_UNTEN :
        return gibBildordner() + "gleis_von_oben_nach_rechts_unten.png";
      case Richtung.VON_RECHTS_NACH_LINKS_OBEN :
        return gibBildordner() + "gleis_von_rechts_nach_links_oben.png";
      case Richtung.VON_RECHTS_NACH_LINKS_UNTEN :
        return gibBildordner() + "gleis_von_rechts_nach_links_unten.png";
      case Richtung.VON_UNTEN_NACH_LINKS_OBEN :
        return gibBildordner() + "gleis_von_unten_nach_links_oben.png";
      case Richtung.VON_UNTEN_NACH_RECHTS_OBEN :
        return gibBildordner() + "gleis_von_unten_nach_rechts_oben.png";

      default :
        throw Error();
    }
  }
}

export class Weiche implements Gleis {
  bildAdresse: String;

  constructor(richtung: Richtung) {
    this.bildAdresse = this.gibBidZuRichtung(richtung);
  }

  gibBidZuRichtung(richtung: Richtung) {
    switch (richtung) {
      case Richtung.VON_LINKS_NACH_RECHTS_OBEN :
        return gibBildordner() + "weiche_von_links_nach_rechts_oben.png";
      case Richtung.VON_LINKS_NACH_RECHTS_UNTEN :
        return gibBildordner() + "weiche_von_links_nach_rechts_unten.png";
      case Richtung.VON_RECHTS_NACH_LINKS_OBEN :
        return gibBildordner() + "weiche_von_rechts_nach_links_oben.png";
      case Richtung.VON_RECHTS_NACH_LINKS_UNTEN:
        return gibBildordner() + "weiche_von_rechts_nach_links_unten.png";

      case Richtung.VON_LINKS_OBEN_NACH_RECHTS_UNTEN :
        return gibBildordner() + "weiche_von_links_oben_nach_rechts_unten.png";
      case Richtung.VON_LINKS_UNTEN_NACH_RECHTS_OBEN :
        return gibBildordner() + "weiche_von_links_unten_nach_rechts_oben.png";
      case Richtung.VON_RECHTS_OBEN_NACH_LINKS_UNTEN :
        return gibBildordner() + "weiche_von_rechts_oben_nach_links_unten.png";
      case Richtung.VON_RECHTS_UNTEN_NACH_LINKS_OBEN:
        return gibBildordner() + "weiche_von_rechts_unten_nach_links_oben.png";

      default :
        throw Error();
    }
  }
}


export enum Richtung {
  HORIZONTAL,
  VERTICAL,

  VON_LINKS_NACH_RECHTS_OBEN,
  VON_LINKS_NACH_RECHTS_UNTEN,
  VON_RECHTS_NACH_LINKS_OBEN,
  VON_RECHTS_NACH_LINKS_UNTEN,
  VON_OBEN_NACH_LINKS_UNTEN,
  VON_OBEN_NACH_RECHTS_UNTEN,
  VON_UNTEN_NACH_LINKS_OBEN,
  VON_UNTEN_NACH_RECHTS_OBEN,

  VON_LINKS_UNTEN_NACH_RECHTS_OBEN,
  VON_LINKS_OBEN_NACH_RECHTS_UNTEN,
  VON_RECHTS_UNTEN_NACH_LINKS_OBEN,
  VON_RECHTS_OBEN_NACH_LINKS_UNTEN
}
