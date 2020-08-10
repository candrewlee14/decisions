# coding=utf-8
from __main__ import db
from datetime import datetime
from sqlalchemy import create_engine, db.Column, db.String, db.Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

Base = declarative_base()
def _get_str_uuid_hex():
    return str(uuid.uuid4().hex)

class Entity():
    id = db.Column(db.String, primary_key=True, default=_get_str_uuid_hex) #UUID
    created_at = db.Column(db,DateTime)
    updated_at = db.Column(db.DateTime)
    last_updated_by = db.Column(db.String)

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
