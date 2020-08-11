import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';

import {AppComponent} from './app.component';
import {TreesApiService} from './trees/trees-api.service';
import {TreeComponent} from './trees/tree.component';

@NgModule({
  declarations: [
    AppComponent,
    TreeComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
  ],
  providers: [TreesApiService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
