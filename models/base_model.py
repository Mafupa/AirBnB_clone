#!/usr/bin/python3
"""Base Model Class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base Model"""
    def __init__(self, *args, **kwargs):
        """init function"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """save function"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """to dict function"""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """representation function"""
        clname = self.__class__.__name__
        return f"[{clname}] ({self.id}) {self.__dict__}"
