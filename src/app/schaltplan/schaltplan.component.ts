import {Component, OnInit} from '@angular/core';
import {Baustein, Gleis, Richtung} from "../shared/Schiene";
import {GleisbauerService} from "../gleisbauer/gleisbauer.service";

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
    this.schaltplan = this.gleisbauerService.neu(30, 30).setzePosition(10, 10)
      .setzeBausteinAnAktuellePosition(new Gleis(Richtung.VERTICAL))
      .setzeBausteinUntenDaneben(new Gleis(Richtung.VON_OBEN_NACH_LINKS_UNTEN))
      .end();
  }

}
