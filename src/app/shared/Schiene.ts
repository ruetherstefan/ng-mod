export interface Baustein {
  bildAdresse: String;
}

export class Leer implements Baustein {
  bildAdresse: '../assets/img/leer.png'
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

function gibBildordner() {
  return "../assets/img/";
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
  VON_LINKS_NACH_RECHTS_OBEN

}
