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
      default :
        throw Error();
    }
  }
}


export enum Richtung {
  HORIZONTAL,
  VERTICAL,

  VON_LINKS_NACH_RECHTS_OBEN,
  VON_OBEN_NACH_LINKS_UNTEN
}
