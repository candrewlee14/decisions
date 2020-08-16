import { Component, OnInit, Input } from '@angular/core';
import { Tree } from './tree.model';

@Component({
  selector: 'app-tree',
  templateUrl: './tree.component.html',
  styleUrls: ['./tree.component.scss']
})
export class TreeComponent implements OnInit {
  @Input() tree: Tree;

  constructor() { }

  ngOnInit(): void {
  }

}
