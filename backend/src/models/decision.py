# coding=utf-8
from marshmallow import Schema, fields
from dataclasses import dataclass, field
from typing import List
import uuid

from .tree import Tree, TreeSchema
from .option import Option, OptionSchema
from .node import Node, NodeSchema
from .option_value import OptionValue, OptionValueSchema
from .entity import _get_str_uuid_hex

@dataclass
class Decision:
    tree: Tree
    nodes: List[Node] 
    options: List[Option]
    option_values: List[OptionValue]
    def __init__(self):
        pass

class DecisionSchema(Schema):
    tree = fields.Nested(TreeSchema)
    nodes = fields.List(fields.Nested(NodeSchema))
    options = fields.List(fields.Nested(OptionSchema))
    option_values = fields.List(fields.Nested(OptionValueSchema))
