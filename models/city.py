#!/usr/bin/python3
"""This is the city class"""
import sqlalchemy
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = 'cities'
    storage = os.getenv("HBNB_TYPE_STORAGE")
    if storage == "db":
        state_id = Column(
            String(60),
            ForeignKey("states.id"),
            nullable=False)
        name = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""