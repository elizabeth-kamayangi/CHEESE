import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declaractive import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()

class Restaurant(Base):
    _tablename_ = 'Restaurant'
    c
engine=create_engine('sqlite:///restaurant menu.db')
Base.metadata.create_all(engine)

