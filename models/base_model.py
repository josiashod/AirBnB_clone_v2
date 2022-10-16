#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import os
import uuid
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, PrimaryKeyConstraint, DateTime

import models

Base = declarative_base()
HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")


class BaseModel:
    """A base class for all hbnb models"""

    # if HBNB_TYPE_STORAGE == "db":
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DateTime(timezone=True), nullable=False,
                        default=datetime.utcnow())
    # else:
    #     id = ""
    #     created_at = datetime.utcnow()
    #     updated_at = datetime.utcnow()

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
            if '__class__' in kwargs.keys():
                del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        if '_sa_instance_state' in self.__dict__:
            del self.__dict__['_sa_instance_state']
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}

        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})

        if type(self.created_at) != str and self.created_at:
            dictionary['created_at'] = self.created_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%f')

        if type(self.updated_at) != str and self.updated_at:
            dictionary['updated_at'] = self.updated_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%f')
        if '_sa_instance_state' in self.__dict__:
            del dictionary['_sa_instance_state']

        return dictionary

    def delete(self):
        """Deletes the current instance from storage"""
        models.storage.delete(self)
