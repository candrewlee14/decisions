
export class Node {
    public created_at: Date;
    public description: string;
    public id: string;
    public last_updated_by: string;
    public parent_id: string;
    public title: string;
    public tree_id: string;
    public updated_at: Date;
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
}
