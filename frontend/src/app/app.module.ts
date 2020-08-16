import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';

import {MessagesComponent} from './messages/messages.component';
import {AppComponent} from './app.component';
import {TreesApiService} from './trees-api.service';
import {TreeComponent} from './trees/tree.component';
import { TreesListComponent } from './trees-list/trees-list.component';
import {TreeOverviewComponent} from './tree-overview/tree-overview.component';
import { FilterPipe } from './filter.pipe';
import { FormsModule } from '@angular/forms';


@NgModule({
  declarations: [
    AppComponent,
    TreeComponent,
    TreesListComponent,
    TreeOverviewComponent,
    MessagesComponent,
    FilterPipe,
  ],
  imports: [
    AppRoutingModule,
    BrowserModule,
    HttpClientModule,
    FormsModule,
  ],
  providers: [TreesApiService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
