#!/usr/bin/env python3
"""
new authentication mechanism that will:

  - validate if everything inherits correctly
    without any overloading
  - validate the “switch” by using environment
    variables

"""
from typing import TypeVar
import re
import base64
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """
    session auth class that inherits from auth
    """
