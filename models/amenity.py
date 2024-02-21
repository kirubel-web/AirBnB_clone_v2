#!/usr/bin/python3
""" Defines the Amenity class."""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """
    Represents class State.
    Attributes:
        __tablename__ (str): The name of the MySQL table to store amenities.
        name (str): The name of the amenity object.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """
    __tablename__ = "amenities"
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=True)
    name = Column(String(128), nullable=False)
