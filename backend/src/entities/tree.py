# coding=utf-8
from marshmallow import Schema, fields
from .entity import Entity, db


class Tree(Entity, db.Model):
    __tablename__ = 'trees'
    title = db.Column(db.String)
    description = db.Column(db.String)

    def __init__(self, title, description, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description

class TreeSchema(Schema):
    id = fields.Str() #UUID
    title = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
