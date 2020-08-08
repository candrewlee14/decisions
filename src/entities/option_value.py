# coding=utf-8
from marshmallow import Schema, fields
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from .entity import Entity, Base


class OptionValue(Entity, Base):
    __tablename__ = 'option_values'

    node_id = Column(Integer, ForeignKey("nodes.id"), nullable=False)
    option_id = Column(Integer, ForeignKey("trees.id"), nullable=False)
    weight = Column(Float)
    value = Column(Float)

    def __init__(self, node_id, option_id, weight, value, created_by):
        Entity.__init__(self, created_by)
        self.node_id = node_id
        self.option_id = option_id
        self.weight = weight
        self.value = value

class OptionValueSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    node_id = fields.Number()
    option_id = fields.Number()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
