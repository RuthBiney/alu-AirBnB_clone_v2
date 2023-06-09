#!/usr/bin/python3
""" State Module for HBNB project """
import sqlalchemy
import os
from models.base_model import BaseModel, Base
import models
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    storage = os.getenv("HBNB_TYPE_STORAGE")
    if storage == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="delete", backref="state")
    else:
        @property
        def cities(self):
            city_list = []
            data = models.storage.all(City)
            for key, city in data.items():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list