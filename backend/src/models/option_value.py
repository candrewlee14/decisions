# coding=utf-8
from marshmallow import Schema, fields
from dataclasses import dataclass, field
from .entity import Entity, db

@dataclass
class OptionValue(Entity, db.Model):   
    __tablename__ = 'option_values'
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.String, db.ForeignKey("nodes.id"), nullable=False, index=True)
    option_id = db.Column(db.String, db.ForeignKey("options.id"), nullable=False, index=True)
    weight = db.Column(db.Float)
    value = db.Column(db.Float)

class OptionValueSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    node_id = fields.Str()
    option_id = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
