#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    if HBNB_TYPE_STORAGE == "db":
        name = Column(String(128))
        cities = relationship("City", backref="state")
    else:
        name = ""
