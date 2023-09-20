#!/usr/bin/env python3
"""
class that inherits from Auth
"""
from flask import request
from typing import List, TypeVar
import os
import re
import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    class that inherits from auth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if not authorization_header \
                or not isinstance(authorization_header, str) \
                or not re.search("^Basic ", authorization_header):
            return None
        return re.sub("^Basic ", "", authorization_header)
