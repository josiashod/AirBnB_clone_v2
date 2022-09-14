#!/usr/bin/python3
""" State Module for HBNB project """
import os
import models
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City

HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if HBNB_TYPE_STORAGE == "db":
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            """cities list"""

            results = []
            for j, i in models.storage.all(models.city.City).items():
                if (i.state_id == self.id):
                    results.append(i)
            return results
