#!/usr/bin/python3
"""DBStorage Module"""
import os

import models
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')


class DBStorage:
    """DBSTorage class definitions"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialization of the class"""

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:\
            3306/{}".format(
            HBNB_MYSQL_USER,
            HBNB_MYSQL_PWD,
            HBNB_MYSQL_HOST,
            HBNB_MYSQL_DB
        ), pool_pre_ping=True)

        env = os.getenv("HBNB_ENV")
        if (env == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Get all objects by class name"""

        results = {}
        if cls:
            for row in self.__session.query(cls).all():
                key = "{}.{}".format(cls.__name__, row.id)
                row.to_dict()
                results.update({key: row})
        else:
            for table in [User, State, City, Amenity, Place, Review]:
                for row in self.__session.query(table).all():
                    key = "{}.{}".format(table.__name__, row.id)
                    row.to_dict()
                    results.update({key: row})
        return (results)

    def new(self, obj):
        """Add the object to the current database session"""

        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""

        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload the session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Scope = scoped_session(Session)
        self.__session = Scope()
