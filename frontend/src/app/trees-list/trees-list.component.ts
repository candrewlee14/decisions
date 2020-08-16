import { Component, OnInit, OnDestroy } from '@angular/core';
import { TreeComponent} from '../trees/tree.component';
import { TreesApiService } from '../trees-api.service';
import { Subscription } from 'rxjs';
import { Tree } from '../trees/tree.model';

@Component({
  selector: 'app-trees-list',
  templateUrl: './trees-list.component.html',
  styleUrls: ['./trees-list.component.scss']
})
export class TreesListComponent implements OnInit, OnDestroy {
  treesListSubs: Subscription;
  treesList: Tree[];

  constructor(private treesApi: TreesApiService) { }

  ngOnInit(): void {
    this.treesListSubs = this.treesApi
      .getPublicTrees()
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
