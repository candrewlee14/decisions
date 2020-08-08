# coding=utf-8

from sqlalchemy import Column, String, Float, Integer, ForeignKey

from .entity import Entity, Base


class Option(Entity, Base):
    __tablename__ = 'options'

    title = Column(String)
    description = Column(String)
    tree_id = Column(Integer, ForeignKey("trees.id"), nullable=False)

    def __init__(self, title, description, tree_id, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description
        self.tree_id = tree_id
