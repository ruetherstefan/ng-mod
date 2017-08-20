import {Injectable} from '@angular/core';
import {Baustein, Leer} from '../shared/Schiene';

@Injectable()
export class GleisbauerService {

  private gleise: Baustein[][] = []; // [y][x]
  private aktuellePosition: Position;

  constructor() {
  }


  neu(breite: number, hoehe: number): GleisbauerService {
    for (let y = 0; y < hoehe; y++) {
      this.gleise[y] = [];
      for (let x = 0; x < breite; x++) {
        this.gleise[y][x] = new Leer()
      }
    }
    this.aktuellePosition = {x: 0, y: 0}

    return this
  }

  setzeBausteinAnAktuellePosition(baustein: Baustein) {
    this.gleise[this.aktuellePosition.y][this.aktuellePosition.x] = baustein;
    return this;
  }

  setzeBausteinRechtsDaneben(baustein: Baustein) {
    this.aktuellePosition.x += 1
    this.setzeBausteinAnAktuellePosition(baustein)
    return this;
  }

  setzeBausteinLinksDaneben(baustein: Baustein) {
    this.aktuellePosition.x -= 1
    this.setzeBausteinAnAktuellePosition(baustein)
    return this;
  }

  setzeBausteinObenDaneben(baustein: Baustein) {
    this.aktuellePosition.y -= 1
    this.setzeBausteinAnAktuellePosition(baustein)
    return this;
  }

  setzeBausteinUntenDaneben(baustein: Baustein) {
    this.aktuellePosition.y += 1
    this.setzeBausteinAnAktuellePosition(baustein)
    return this;
  }

  setzeBausteinRechtsObenDaneben(baustein: Baustein) {
    this.aktuellePosition.x += 1
    this.aktuellePosition.y -= 1
    this.setzeBausteinAnAktuellePosition(baustein)
    return this;
  }

  setzeBausteinLinksObenDaneben(baustein: Baustein) {
    this.aktuellePosition.x -= 1
    this.aktuellePosition.y -= 1
    this.setzeBausteinAnAktuellePosition(baustein)
    return this;
  }

  setzeBausteinRechtsUntenDaneben(baustein: Baustein) {
    this.aktuellePosition.x += 1
    this.aktuellePosition.y += 1
    this.setzeBausteinAnAktuellePosition(baustein)
    return this;
  }

  setzeBausteinLinksUntenDaneben(baustein: Baustein) {
    this.aktuellePosition.x -= 1
    this.aktuellePosition.y += 1
    this.setzeBausteinAnAktuellePosition(baustein)
    return this;
  }

  setzePosition(x: number, y: number) {
    this.aktuellePosition = {x: x - 1, y: y - 1}
    return this;
  }

  gibPosition(): Position {
    return {x: this.aktuellePosition.x + 1, y: this.aktuellePosition.y + 1};
  }

  end(): Baustein[][] {
    return this.gleise
  }

}

export interface Position {
  x: number,
  y: number
}

