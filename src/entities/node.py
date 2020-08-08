# coding=utf-8

from sqlalchemy import Column, String, Float, Integer, ForeignKey

from .entity import Entity, Base


class Node(Entity, Base):
    __tablename__ = 'nodes'

    title = Column(String)
    description = Column(String)
    tree_id = Column(Integer, ForeignKey("trees.id"), nullable=False)
    parent_id = Column(Integer, ForeignKey("nodes.id"), nullable=True)

    def __init__(self, title, description, tree_id, parent_id, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description
        self.tree_id = tree_id
        self.parent_id = parent_id
