# coding=utf-8

from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

engine = create_engine("sqlite:///db/decisions.db")
Session = sessionmaker(bind=engine)

Base = declarative_base()
def _get_str_uuid_hex():
    return str(uuid.uuid4().hex)

class Entity():
    id = Column(String, primary_key=True, default=_get_str_uuid_hex) #UUID
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
