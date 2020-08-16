import { ActivatedRoute } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { Decision } from '../decision.models';
import {TreesApiService} from '../trees-api.service';

@Component({
  selector: 'app-tree-overview',
  templateUrl: './tree-overview.component.html',
  styleUrls: ['./tree-overview.component.scss']
})
export class TreeOverviewComponent implements OnInit {
  decision: Decision;

  constructor(
    private route: ActivatedRoute,
    private treeService: TreesApiService
  ) { }

  ngOnInit(): void {
    this.getDecision();
  }

  getDecision(): void {
    const id = this.route.snapshot.paramMap.get('id');
    this.treeService.getDecision(id)
      .subscribe(decision => this.decision = decision);
  }

}
