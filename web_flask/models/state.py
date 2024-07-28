#!/usr/bin/python3
"""
Module for State class
"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """
    State class
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """
        Getter attribute cities that returns the list of City objects
        from storage linked to the current State
        """
        if models.storage_t != 'db':
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]
        return self.cities
