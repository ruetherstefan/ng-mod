/* tslint:disable:no-unused-variable */

import {TestBed, async, inject} from '@angular/core/testing';
import {GleisbauerService} from './gleisbauer.service';
import {Baustein, Leer} from '../shared/Schiene';

describe('GleisbauerService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [GleisbauerService]
    });
  });

  it('should ...', inject([GleisbauerService], (service: GleisbauerService) => {
    expect(service).toBeTruthy();
  }));


  it('should start', inject([GleisbauerService], (gleisbauerService: GleisbauerService) => {
    let gleise: Baustein[][] = gleisbauerService.neu(2, 3).end();
    expect([[new Leer(), new Leer()],
      [new Leer(), new Leer()],
      [new Leer(), new Leer()]]).toEqual(gleise);
  }));

});
