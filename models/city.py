#!/usr/bin/python3
""" holds class City"""

from models.base_model import BaseModel, Base
from os import getenv

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

STORE_TYPE = 'db'

class City(BaseModel, Base):
    """Representation of city """
    if STORE_TYPE == 'db':
        __tablename__ = 'cities'
        name = Column(String(128),
                      nullable=False)
        state_id = Column(String(60),
                          ForeignKey('states.id'),
                          nullable=False)
        places = relationship("Place",
                              backref="cities",
                              cascade="all, delete-orphan")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
