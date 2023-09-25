#!/usr/bin/env python3
"""
user authentication file
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    password hashed with hashed with `bcrypt.hashpw`
    """
    # generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # ensure the result is in bytes
    if isinstance(hashed_password, bytes):
        return hashed_password

    # convert to bytes
    return hashed_password.encode('utf-8')
