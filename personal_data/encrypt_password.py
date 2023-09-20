#!/usr/bin/env python3
"""Implement a hash_password function that expects one
  string argument name password and returns a salted, hashed password,
  which is a byte string."""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    function that takes in a password str and returns
      a salted hashed password
    """
    # Generate a random salt for each user
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Return the salted and hashed password as a byte string
    return hashed_password
