#!/usr/bin/env python3
"""Defines the User class."""
from hashlib import md5
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represents a user for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table users.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store users.
        email: (sqlalchemy String): The user's email address.
        password (sqlalchemy String): The user's password.
        first_name (sqlalchemy String): The user's first name.
        last_name (sqlalchemy String): The user's last name.
        places (sqlalchemy relationship): The User-Place relationship.
        reviews (sqlalchemy relationship): The User-Review relationship.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")

    def __setattr__(self, name, value):
        """Encodes passwords using MD5 before setting an attribute."""
        if name == "password":
            value = value.encode("utf-8")
            value = md5(value).hexdigest()
        object.__setattr__(self, name, value)
