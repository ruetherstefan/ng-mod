/* tslint:disable:no-unused-variable */
import {async, ComponentFixture, TestBed} from '@angular/core/testing';
import {By} from '@angular/platform-browser';
import {DebugElement} from '@angular/core';

import {BasteleckeComponent} from './bastelecke.component';

describe('BasteleckeComponent', () => {
  let component: BasteleckeComponent;
  let fixture: ComponentFixture<BasteleckeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [BasteleckeComponent]
    })
      .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BasteleckeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
