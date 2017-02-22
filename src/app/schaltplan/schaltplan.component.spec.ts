/* tslint:disable:no-unused-variable */
import {async, ComponentFixture, TestBed} from '@angular/core/testing';
import {By} from '@angular/platform-browser';
import {DebugElement} from '@angular/core';

import {SchaltplanComponent} from './schaltplan.component';
import {Baustein} from "../shared/Schiene";

describe('SchaltplanComponent', () => {
  let component: SchaltplanComponent;
  let fixture: ComponentFixture<SchaltplanComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [SchaltplanComponent]
    })
      .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SchaltplanComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should show singe grid', () => {
    component.schaltplan = [[neueHorSchiene()]];

    fixture.detectChanges();

    let img = fixture.debugElement.query(By.css('#schaltplanDiv')).query(By.css('img'));
    expect(img.nativeElement).toBeTruthy();
  });

  it('should show grid horizontal in dynamischer Größe', () => {
    component.schaltplan = [[neueHorSchiene()], [neueHorSchiene()]];

    fixture.detectChanges();

    let reihen_tags = fixture.debugElement.query(By.css('#schaltplanDiv')).queryAll(By.css('tr'));
    expect(reihen_tags[0].query(By.css('td')).query(By.css('img')).nativeElement).toBeTruthy();
    expect(reihen_tags[1].query(By.css('td')).query(By.css('img')).nativeElement).toBeTruthy();
    expect(2 === reihen_tags.length).toBeTruthy();
  });

  it('should show grid vertical in dynamischer Größe', () => {
    component.schaltplan = [[neueHorSchiene(), neueHorSchiene()]];

    fixture.detectChanges();

    let vertical_tags = fixture.debugElement.query(By.css('#schaltplanDiv')).queryAll(By.css('td'));
    expect(vertical_tags[0].query(By.css('img')).nativeElement).toBeTruthy();
    expect(vertical_tags[1].query(By.css('img')).nativeElement).toBeTruthy();
    expect(2 === vertical_tags.length).toBeTruthy();
  });

  it('should show 4er grid', () => {
    component.schaltplan = [[neueHorSchiene(), neueHorSchiene()], [neueHorSchiene(), neueHorSchiene()]];

    fixture.detectChanges();

    let bilder_tags = fixture.debugElement.query(By.css('#schaltplanDiv')).queryAll(By.css('img'));
    expect(4 === bilder_tags.length).toBeTruthy();
  });

  it('should show gefordertes Bild', () => {
    let schiene: Baustein = {'bildAdresse': "../assets/img/weiche_von_links_nach_rechts_oben.png"};
    component.schaltplan = [[neueHorSchiene()]];

    fixture.detectChanges();

    let img = fixture.debugElement.query(By.css('#schaltplanDiv')).query(By.css('img'));
    expect(img.nativeElement.src.search("weiche_von_links_nach_rechts_oben.png")).toBeTruthy();
  });

  function neueHorSchiene(): Baustein {
    return {'bildAdresse': "../assets/img/gleis_horizontal.png"};
  }
}
