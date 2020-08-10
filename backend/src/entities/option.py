# coding=utf-8
from dataclasses import dataclass, field
from marshmallow import Schema, fields
from .entity import Entity, db

@dataclass
class Option(Entity, db.Model):
    title = db.Column(db.String)
    description = db.Column(db.String)
    tree_id = db.Column(db.Integer, db.ForeignKey("trees.id"), nullable=False, index=True)

class OptionSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    tree_id = fields.Number()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
