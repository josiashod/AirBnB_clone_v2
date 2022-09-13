#!/usr/bin/python3
""" City Module for HBNB project """
import os
from models.base_model import Base, BaseModel
from models.state import State
from sqlalchemy import Column, String, ForeignKey

HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey(State.id))
    name = Column(String(128))
