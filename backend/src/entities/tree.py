# coding=utf-8
from marshmallow import Schema, fields
from sqlalchemy import db.Column, db.String, Float, db.Integer, db.ForeignKey
from .entity import Entity, Base, Session


class Tree(Entity, Base):
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
