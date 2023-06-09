#!/usr/bin/python3
""" City Module for HBNB project """
import sqlalchemy
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """ The city class, contains state ID and name 
     Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ ='cities'
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
