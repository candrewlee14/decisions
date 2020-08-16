# coding=utf-8
from marshmallow import Schema, fields
from .entity import Entity,  db

class Node(Entity, db.Model):
    __tablename__ = 'nodes'

    title = db.Column(db.String)
    description = db.Column(db.String)
    tree_id = db.Column(db.String, db.ForeignKey("trees.id"), nullable=False, index=True)
    parent_id = db.Column(db.String, db.ForeignKey("nodes.id"), nullable=True, index=True)
    depth = db.Column(db.Integer)

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
    depth = fields.Int()
    parent_id = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
