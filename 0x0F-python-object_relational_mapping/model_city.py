#!/usr/bin/python3
"""
class definition of a City
"""


from model_state import Base
from sqlalchemy import (create_engine, Column, Integer,
        String, MetaData, ForeignKey)


class City(Base):
    """
    Class that define City data structure
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
