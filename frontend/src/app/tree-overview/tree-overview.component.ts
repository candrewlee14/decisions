import { ActivatedRoute } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { Decision, setTreeStructure} from '../decision.models';
import {TreesApiService} from '../trees-api.service';
import { Node } from '../decision.models';


@Component({
  selector: 'app-tree-overview',
  templateUrl: './tree-overview.component.html',
  styleUrls: ['./tree-overview.component.scss']
})
export class TreeOverviewComponent implements OnInit {
  decision: Decision;
  list: Array<Node>;

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
      .subscribe(decision => {
        this.decision = (decision as Decision);
        setTreeStructure(this.decision);
        this.list = [this.decision.decision_tree];
      });
  }

  toggleChildren(node: Node): void {
    // to do
    node.visible = !node.visible;
    if (node.expandIcon === '[+]'){
      node.expandIcon = '[-]';
    }
    else {
      node.expandIcon = '[+]';
    }
  }

}
