#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        method that saves the user to the database
        """
        # create new user instance
        new_user = User(email=email,
                        hashed_password=hashed_password)

        # add new user to session, and commit to db
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        method that takes in arbitrary keyword arguments
        and returns the first row found in the users table
        as filtered by the method's input arguments
        """
        # check if valid response given
        if not kwargs:
            raise InvalidRequestError

        # bind and filter
        user = self._session.query(User).filter_by(**kwargs).first()
    
        # check if exists
        if user is None:
            raise NoResultFound
    
        return user
