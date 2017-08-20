import {Component, OnInit} from '@angular/core';
import {Baustein, Gleis, Weiche, Richtung} from "../shared/Schiene";
import {GleisbauerService} from "../gleisbauer/gleisbauer.service";

import * as SerialPort from 'serialport';

@Component({
  selector: 'ad-ng-mod-schaltplan',
  templateUrl: './schaltplan.component.html',
  styleUrls: ['./schaltplan.component.css'],
  providers: [GleisbauerService]
})
export class SchaltplanComponent implements OnInit {

  schaltplan: Baustein[][] = [[]];

  constructor(private gleisbauerService: GleisbauerService) {
  }

  ngOnInit() {
    this.schaltplan = this.gleisbauerService.neu(15, 15).setzePosition(10, 10)
      .setzeBausteinAnAktuellePosition(new Gleis(Richtung.VERTICAL))
      .setzeBausteinUntenDaneben(new Gleis(Richtung.VON_OBEN_NACH_LINKS_UNTEN))
      .setzeBausteinLinksUntenDaneben(new Gleis(Richtung.VON_LINKS_NACH_RECHTS_OBEN))
      .setzeBausteinLinksDaneben(new Weiche(Richtung.VON_LINKS_NACH_RECHTS_UNTEN))
      .setzeBausteinLinksDaneben(new Weiche(Richtung.VON_RECHTS_NACH_LINKS_OBEN))
      .setzeBausteinLinksObenDaneben(new Gleis(Richtung.VON_LINKS_NACH_RECHTS_UNTEN))
      .setzeBausteinLinksDaneben(new Gleis(Richtung.HORIZONTAL))
      .setzeBausteinLinksDaneben(new Gleis(Richtung.HORIZONTAL))
      .setzeBausteinLinksDaneben(new Gleis(Richtung.VON_RECHTS_NACH_LINKS_UNTEN))
      .setzeBausteinLinksUntenDaneben(new Weiche(Richtung.VON_LINKS_UNTEN_NACH_RECHTS_OBEN))
      .setzeBausteinRechtsDaneben(new Gleis(Richtung.HORIZONTAL))
      .setzeBausteinRechtsDaneben(new Gleis(Richtung.HORIZONTAL))
      .setzeBausteinRechtsDaneben(new Gleis(Richtung.HORIZONTAL))
      .setzeBausteinRechtsDaneben(new Gleis(Richtung.HORIZONTAL))

      .end();
  }


  testSerialConnection() {
    console.log("testSerialConnection");


    //var SerialPort = require('serialport');
    //var port = new SerialPort('COM3', {baudRate: 19200});
    //let port = new SerialPort('');

    /*
    port.write('1', function(err) {
      if (err) {
        return console.log('Error on write: ', err.message);
      }
      console.log('message written');
    });

    // Open errors will be emitted as an error event
    port.on('error', function(err) {
      console.log('Error: ', err.message);
    })*/
    
  }

}
