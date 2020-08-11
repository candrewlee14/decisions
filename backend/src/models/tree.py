# coding=utf-8
from marshmallow import Schema, fields
from .entity import Entity, db, datetime
from .user import User

class Tree(Entity, db.Model):
    __tablename__ = 'trees'
    title = db.Column(db.String)
    description = db.Column(db.String)
    created_by = db.Column(db.ForeignKey("users.id"), index = True)
    is_private = db.Column(db.Boolean)

    def __init__(self, title, description, created_by, is_private):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.created_by = created_by
        self.is_private = is_private

class TreeSchema(Schema):
    id = fields.Str() #UUID
    title = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    created_by = fields
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
    is_private = fields.Bool()
