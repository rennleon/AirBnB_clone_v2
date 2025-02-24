#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

if models.is_db == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """ Base model class """
    if models.is_db == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow())
        updated_at = Column(DateTime, default=datetime.utcnow())

    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            fmt = '%Y-%m-%dT%H:%M:%S.%f'

            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())
            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = datetime.now()
            else:
                kwargs['updated_at'] = datetime\
                                        .strptime(kwargs['updated_at'], fmt)
            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.now()
            else:
                kwargs['created_at'] = datetime\
                                        .strptime(kwargs['created_at'], fmt)
            if '__class__' in kwargs:
                del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        # n_dict = self.__dict__.copy()
        # if "created_at" in n_dict:
        #     n_dict["created_at"] = n_dict["created_at"].strftime(dtm)
        # if "updated_at" in n_dict:
        #     n_dict["updated_at"] = n_dict["updated_at"].strftime(dtm)
        # n_dict["__class__"] = self.__class__.__name__
        # if "_sa_instance_state" in n_dict:
        #     del n_dict["_sa_instance_state"]
        # return n_dict
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
