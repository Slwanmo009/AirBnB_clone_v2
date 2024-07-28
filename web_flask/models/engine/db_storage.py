#!/usr/bin/python3
"""
Module for DBStorage class
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


class DBStorage:
    """
    Interacts with the MySQL database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Create the engine (self.__engine)
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB'),
            pool_pre_ping=True))

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries the current database session (self.__session)
        """
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(User, Place, State, City, Amenity, Review).all()

        obj_dict = {}
        for obj in objs:
            key = obj.__class__.__name__ + '.' + obj.id
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """
        Adds the object to the current database session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes from the current database session (self.__session) obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database (feature of SQLAlchemy) and
        creates the current database session (self.__session) from the
        engine (self.__engine)
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Call remove() method on the private session attribute (self.__session)
        """
        self.__session.remove()
