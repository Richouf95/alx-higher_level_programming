#!/usr/bin/python3
"""
class definition of a State and an instance Base = declarative_base()
"""


from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base(metadata=MetaData())


class State(Base):
    """
    Class that define State data structure
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
