#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModol, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey,  Float


class Review(BaseModel, Base):
    """
    This is the class for Review:
    place_id
    user_id
    text
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
