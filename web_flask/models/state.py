#!/usr/bin/python3
"""
State Module for HBNB project
"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', backref='state', cascade='all, delete, delete-orphan'
    )

    if models.storage_t != 'db':
        @property
        def cities(self):
            """Getter for cities"""
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
