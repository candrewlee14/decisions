import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {TreesListComponent} from './trees-list/trees-list.component';
import { TreeOverviewComponent } from './tree-overview/tree-overview.component';

const routes: Routes = [
  { path: '', redirectTo: '/', pathMatch: 'full' },
  { path: 'decisions', component: TreesListComponent },
  { path: 'decision/:id', component: TreeOverviewComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
