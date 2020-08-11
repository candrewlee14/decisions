import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import {TreesApiService} from './trees/trees-api.service';
import {Tree} from './trees/tree.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  treesListSubs: Subscription;
  treesList: Tree[];

  constructor(private treesApi: TreesApiService) {
  }

  ngOnInit(): void {
    this.treesListSubs = this.treesApi
      .getTrees()
      .subscribe(res => {
          this.treesList = res;
        },
        console.error
      );
  }

  ngOnDestroy(): void {
    this.treesListSubs.unsubscribe();
  }
}
