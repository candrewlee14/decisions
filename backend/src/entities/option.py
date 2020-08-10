# coding=utf-8
from marshmallow import Schema, fields
from sqlalchemy import db.Column, db.String, Float, db.Integer, db.ForeignKey
from .entity import Entity, Base, db


class Option(Entity, Base):
    __tablename__ = 'options'

    title = db.Column(db.String)
    description = db.Column(db.String)
    tree_id = db.Column(db.Integer, db.ForeignKey("trees.id"), nullable=False, index=True)

    def __init__(self, title, description, tree_id, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description
        self.tree_id = tree_id

class OptionSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    tree_id = fields.Number()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
