#!/usr/bin/python3

"""
Module to define the City class
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """
        City class inherits the Base class
        Attributes:
            id (int)
            name (string)
            state_id (int)
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
