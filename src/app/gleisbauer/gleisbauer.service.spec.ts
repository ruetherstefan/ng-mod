/* tslint:disable:no-unused-variable */

import {TestBed, async, inject} from '@angular/core/testing';
import {GleisbauerService} from './gleisbauer.service';
import {Baustein, Leer, Gleis, Richtung} from '../shared/Schiene';

describe('GleisbauerService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [GleisbauerService]
    });
  });

  it('should ...', inject([GleisbauerService], (service: GleisbauerService) => {
    expect(service).toBeTruthy();
  }));


  it('should start', inject([GleisbauerService], (service: GleisbauerService) => {
    let gleise: Baustein[][] = service.neu(2, 3).end();
    expect([[new Leer(), new Leer()],
      [new Leer(), new Leer()],
      [new Leer(), new Leer()]]).toEqual(gleise);
  }));

  it('should start Position at 0,0', inject([GleisbauerService], (service: GleisbauerService) => {
    let gleise: Baustein[][] = service.neu(2, 1)
      .setzeBausteinAnAktuellePosition(new Gleis(Richtung.HORIZONTAL))
      .end();
    expect([[new Gleis(Richtung.HORIZONTAL), new Leer()]]).toEqual(gleise);
  }));

  it('should position ändern', inject([GleisbauerService], (service: GleisbauerService) => {
    let gleise: Baustein[][] = service.neu(2, 1)
      .setzePosition(2, 1)
      .setzeBausteinAnAktuellePosition(new Gleis(Richtung.HORIZONTAL))
      .end();
    expect([[new Leer(), new Gleis(Richtung.HORIZONTAL)]]).toEqual(gleise);
  }));

  it('should ein Gleis Rechts daneben setzten', inject([GleisbauerService], (service: GleisbauerService) => {
    let gleise: Baustein[][] = service.neu(2, 1)
      .setzePosition(1, 1)
      .setzeBausteinRechtsDaneben(new Gleis(Richtung.HORIZONTAL))
      .end();
    expect([[new Leer(), new Gleis(Richtung.HORIZONTAL)]]).toEqual(gleise);
    expect(service.gibPosition()).toEqual({x: 2, y: 1});
  }));

  it('should ein Gleis Links daneben setzten', inject([GleisbauerService], (service: GleisbauerService) => {
    let gleise: Baustein[][] = service.neu(2, 2)
      .setzePosition(2, 2)
      .setzeBausteinLinksDaneben(new Gleis(Richtung.HORIZONTAL))
      .end();
    expect([[new Leer(), new Leer()],
      [new Gleis(Richtung.HORIZONTAL), new Leer()]]).toEqual(gleise);
    expect(service.gibPosition()).toEqual({x: 1, y: 2});
  }));

  it('should ein Gleis Oben daneben setzten', inject([GleisbauerService], (service: GleisbauerService) => {
    let gleise: Baustein[][] = service.neu(2, 2)
      .setzePosition(2, 2)
      .setzeBausteinObenDaneben(new Gleis(Richtung.HORIZONTAL))
      .end();
    expect([[new Leer(), new Gleis(Richtung.HORIZONTAL)],
      [new Leer(), new Leer()]]).toEqual(gleise);
    expect(service.gibPosition()).toEqual({x: 2, y: 1});
  }));

  it('should ein Gleis Unten daneben setzten', inject([GleisbauerService], (service: GleisbauerService) => {
    let gleise: Baustein[][] = service.neu(2, 2)
      .setzePosition(1, 1)
      .setzeBausteinUntenDaneben(new Gleis(Richtung.HORIZONTAL))
      .end();
    expect([[new Leer(), new Leer()],
      [new Gleis(Richtung.HORIZONTAL), new Leer()]]).toEqual(gleise);
    expect(service.gibPosition()).toEqual({x: 1, y: 2});
  }));

  it('should ein Gleis Rechts-Unten daneben setzten', inject([GleisbauerService], (service: GleisbauerService) => {
    let gleise: Baustein[][] = service.neu(2, 2)
      .setzePosition(1, 1)
      .setzeBausteinRechtsUntenDaneben(new Gleis(Richtung.HORIZONTAL))
      .end();
    expect([[new Leer(), new Leer()],
      [new Leer(), new Gleis(Richtung.HORIZONTAL)]]).toEqual(gleise);
    expect(service.gibPosition()).toEqual({x: 2, y: 2});
  }));

  it('should ein Gleis Links-Unten daneben setzten', inject([GleisbauerService], (service: GleisbauerService) => {
    let gleise: Baustein[][] = service.neu(2, 2)
      .setzePosition(2, 1)
      .setzeBausteinLinksUntenDaneben(new Gleis(Richtung.HORIZONTAL))
      .end();
    expect([[new Leer(), new Leer()],
      [new Gleis(Richtung.HORIZONTAL), new Leer()]]).toEqual(gleise);
    expect(service.gibPosition()).toEqual({x: 1, y: 2});
  }));

  it('should ein Gleis Rechts-Oben daneben setzten', inject([GleisbauerService], (service: GleisbauerService) => {
    let gleise: Baustein[][] = service.neu(2, 2)
      .setzePosition(1, 2)
      .setzeBausteinRechtsObenDaneben(new Gleis(Richtung.HORIZONTAL))
      .end();
    expect([[new Leer(), new Gleis(Richtung.HORIZONTAL)],
      [new Leer(), new Leer()]]).toEqual(gleise);
    expect(service.gibPosition()).toEqual({x: 2, y: 1});
  }));

  it('should ein Gleis Links-Oben daneben setzten', inject([GleisbauerService], (service: GleisbauerService) => {
    let gleise: Baustein[][] = service.neu(2, 2)
      .setzePosition(2, 2)
      .setzeBausteinLinksObenDaneben(new Gleis(Richtung.HORIZONTAL))
      .end();
    expect([[new Gleis(Richtung.HORIZONTAL), new Leer()],
      [new Leer(), new Leer()]]).toEqual(gleise);
    expect(service.gibPosition()).toEqual({x: 1, y: 1});
  }));

});
