#!/usr/bin/python3
"""
State module.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """
    State class.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        """
        Getter method for cities if the storage engine is not DBStorage.
        Returns the list of City objects linked to the current State.
        """
        if models.storage_type != 'db':
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]
