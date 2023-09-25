#!/usr/bin/env python3
"""
user authentication file
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        registers users in the database using self._db
        """
        # check if user email already exists
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")

        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))


def _hash_password(password: str) -> bytes:
    """
    password hashed with `bcrypt.hashpw`
    """
    # generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # ensure the result is in bytes
    if isinstance(hashed_password, bytes):
        return hashed_password

    # convert to bytes
    return hashed_password.encode('utf-8')
