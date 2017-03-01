import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import {SchaltplanComponent} from './schaltplan/schaltplan.component';
import {BasteleckeComponent} from './bastelecke/bastelecke.component';

@NgModule({
  declarations: [
    AppComponent,
    SchaltplanComponent,
    BasteleckeComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
