#!/usr/bin/python3

"""
Module to define the State class
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """
        State class inherits the Base class
        Attributes:
            id (int)
            name (string)
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")
