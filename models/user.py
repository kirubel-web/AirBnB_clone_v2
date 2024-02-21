#!/usr/bin/python3
""" Inherits from BaseModel."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    Defines class User.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store users.
        email: (sqlalchemy String): The user's email address.
        places (sqlalchemy relationship): The User-Place relationship.
        reviews (sqlalchemy relationship): The User-Review relationship.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    last_name = Column(String(128))
    reviews = relationship("Review", backref="user", cascade="delete")
    places = relationship("Place", backref="user", cascade="delete")
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
