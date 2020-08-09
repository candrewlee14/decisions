# coding=utf-8
from marshmallow import Schema, fields
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from .entity import Entity, Base


class Node(Entity, Base):
    __tablename__ = 'nodes'

    title = Column(String)
    description = Column(String)
    tree_id = Column(String, ForeignKey("trees.id"), nullable=False)
    parent_id = Column(String, ForeignKey("nodes.id"), nullable=True)
    depth = Column(Integer)

    def __init__(self, title, description, tree_id, parent_id, depth, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description
        self.tree_id = tree_id
        self.parent_id = parent_id
        self.depth = depth

class NodeSchema(Schema):
    id = fields.Str() #UUID
    title = fields.Str()
    description = fields.Str()
    tree_id = fields.Str()
    parent_id = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
