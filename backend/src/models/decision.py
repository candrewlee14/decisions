# coding=utf-8
from marshmallow import Schema, fields
from dataclasses import dataclass, field
from typing import List
import uuid

from .tree import Tree
from .option import Option, OptionSchema
from .node import Node
from .option_value import OptionValue, OptionValueSchema
from .entity import _get_str_uuid_hex

@dataclass
class FrameworkTreeNode:
    """Node for tree that holds all the weights and values of categories and subcategories in a decision option"""
    title: str
    description: str
    children: List['FrameworkTreeNode'] #forward reference because this is self-referential
    node_id: str = field(default_factory=_get_str_uuid_hex)

class FrameworkTreeNodeSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    children = fields.List(fields.Nested('FrameworkTreeNodeSchema'))
    node_id = fields.Str()

@dataclass
class FrameworkTree:
    title: str
    description: str
    root: FrameworkTreeNode
    option_id: str = field(default_factory=_get_str_uuid_hex)

class FrameworkTreeSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    root = fields.Nested(FrameworkTreeNodeSchema)
    option_id = fields.Str()

@dataclass
class Decision:
    title: str
    description: str
    creator_id: int
    options: List[Option]
    option_values: List[OptionValue]
    #option_tree without weights/values
    framework_tree: FrameworkTree
    tree_id: str = field(default_factory=_get_str_uuid_hex)
    
    def normalize(self):
        tree = Tree(self.title, self.description, self.creator)
        nodes = self.get_all_nodes()
        return tree, nodes

    def get_all_nodes(self):
        #[child, depth, parent]
        q = [(self.framework_tree, 0, None)]
        while len(q) > 0:
            node_and_depth = q.pop(0)
            for child in node_and_depth[0].children:
                q.append((child, node_and_depth[1] + 1, node_and_depth[0]))
        return [Node(
            node_and_depth[0].title,
            node_and_depth[0].description,
            self.tree_id,
            node_and_depth[2].node_id,
            node_and_depth[1],
            self.creator
            ) for node_and_depth in q]

class DecisionSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    creator_id = fields.Integer()
    options = fields.List(fields.Nested(OptionSchema))
    option_values = fields.List(fields.Nested(OptionValueSchema))
    framework_tree = fields.Nested(FrameworkTreeSchema)
    tree_id = fields.Str()
