#!/usr/bin/env python3
"""Defines the BaseModel class."""
import models
from datetime import datetime
from os import getenv
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

Base = declarative_base()


class BaseModel:
    """Defines the BaseModel class.

    Attributes:
        id (sqlalchemy String): The BaseModel id.
        created_at (sqlalchemy DateTime): The datetime at creation.
        updated_at (sqlalchemy DateTime): The datetime of last update.
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, remove_password=True):
        """Return a dictionary representation of the BaseModel instance.

        Includes the key/value pair __class__ representing the class name
        of the object. Does not store passwords unless instructed.
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = str(type(self).__name__)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state", None)
        if remove_password is True:
            dictionary.pop("password", None)
        return dictionary

    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)
