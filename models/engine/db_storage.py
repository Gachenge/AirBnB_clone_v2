#!/usr/bin/python3
"""connect to mysql"""
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session

classes = {"Amenity": Amenity, "City": City, "Place": Place, "Review": Review,
           "State": State, "User": User}

class DBStorage:
    """Database storage
    __engine: sqlalchemy engine
    __session: sqlalchemy session
    """

    __engine = None
    __session = None

    def __init__(self):
        """initialise the database storage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """items in current session"""
        if not self.__session:
            self.reload()
        objs = {}
        if isinstance(cls, str):
            cls = classes.get(cls, None)
        if cls:
            for obj in self.__session.query(cls):
                objs[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for cls in classes.values():
                for obj in self.__session.query(cls):
                    objs[obj.__class__.__name__ + '.' + obj.id] = obj
        return (objs)

    def new(self, obj):
        """add a new obj to the database"""
        self.__session.add(obj)

    def save(self):
        """save the changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database (feature of SQLAlchemy) """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """close the current session"""
        self.__session.close()
