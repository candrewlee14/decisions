import { Identifiers } from '@angular/compiler';

export class Node {
    public created_at: Date;
    public description: string;
    public id: string;
    public last_updated_by: string;
    public parent_id: string;
    public title: string;
    public tree_id: string;
    public updated_at: Date;
    public depth: number;
    public children?: Node[];
    expandIcon: string;
    visible: boolean;
}

export class OptionValue {
    public created_at: Date;
    public id: number;
    public last_updated_by: string;
    public node_id: string;
    public option_id: string;
    public updated_at: Date;
    public value: number;
    public weight: number;
}

export class Option {
    public created_at: Date;
    public description: string;
    public id: string;
    public last_updated_by: string;
    public title: string;
    public tree_id: string;
    public updated_at: Date;
}

export class Tree {
    public created_at: Date;
    public created_by: string;
    public description: string;
    public id: string;
    public is_private: boolean;
    public last_updated_by: string;
    public title: string;
    public updated_at: Date;
}

export class Decision {
    public nodes: Node[];
    public option_values: OptionValue[];
    public options: Option[];
    public tree: Tree;
    public decision_tree: Node;
    
}

export function setTreeStructure(decision: Decision): void {
    //create a node dictionary with their ids as key
    var nodeDict = {};
    decision.nodes.forEach(node => {
        node.children = [];
        node.visible = true;
        node.expandIcon = '[+]';
        nodeDict[node.id] = node;
        if (!node.parent_id){
            decision.decision_tree = nodeDict[node.id];
        }
        else {
            nodeDict[node.parent_id].children.push(nodeDict[node.id]);
        }
    });
}
