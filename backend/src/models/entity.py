# coding=utf-8
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr

import uuid

db = SQLAlchemy()

def _get_str_uuid_hex():
    return str(uuid.uuid4().hex)

class Entity():
    id = db.Column(db.String, primary_key=True, default=_get_str_uuid_hex) #UUID
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    @declared_attr
    def fk1(cls):
        last_updated_by = db.Column(db.Integer, db.ForeignKey('users.id'), index = True)

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
