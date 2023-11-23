#!/usr/bin/python3
""" State Module for Airbnb project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """ This is the class for state
    Attrs:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                            backref="state")
    @property
    def cities(self):
        var = models.storage.all()
        listall = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                listall.append(var[key])
        for elem in listall:
            if (elem.state_id == self.id):
                    result.append(elem)
        return(result)
