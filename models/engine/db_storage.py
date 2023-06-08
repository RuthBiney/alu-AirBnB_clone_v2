#!/usr/bin/python3
"""This is the DB storage class for AirBnB"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import Table


class DBStorage:
    """This class serializes instances to a SQL statements and
    deserializes SQL models to instances
    Attributes:
        __engine: mySql
        __session: instance session
    """
    __engine = None
    __session = None

    def __init__(self):
        """ initialize the connection with the DB
        """
        env = os.getenv('HBNB_ENV')
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        dialect = 'mysql'
        driver = 'mysqldb'
        config = '{}+{}://{}:{}@{}/{}'.format(
            dialect,
            driver,
            user,
            passwd,
            host,
            db
        )
        self.__engine = create_engine(config, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ select all the objects from a class or all the classes
        Args:
            cls: class name
        """
        objList = {}
        clsList = ["State", "City", "User", "Place", "Review"]
        if cls:
            data = self.__session.query(eval(cls)).all()
            for obj in data:
                name = type(obj).__name__
                id = obj.id
                key = "{}.{}".format(name, id)
                objList[key] = obj

        else:
            for clss in clsList:
                data = self.__session.query(eval(clss)).all()

                for obj in data:
                    name = type(obj).__name__
                    id = obj.id
                    key = "{}.{}".format(name, id)
                    objList[key] = obj

        return objList

    def new(self, obj):
        """ add a new record to the current session for the DB
        Args:
            obj: given object
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ update the database with the new records
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the DB of the current session
        Args:
            obj: given object
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create the session and tables for the db
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ call remove method
        """
        self.__session.close()