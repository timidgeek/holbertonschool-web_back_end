#!/usr/bin/env python3
"""
class that inherits from Auth
"""
from flask import request
from typing import List, TypeVar
import os
import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    class that inherits from auth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        returns the Base64 part of the Authorization header for a Basic Authentication
        """
        # Return None if authorization_header is None or not a string
        if authorization_header is None or not isinstance(
           authorization_header, str):
            return None

        # Check if authorization_header starts with 'Basic ' (with a space
        # at the end)
        if not authorization_header.startswith('Basic '):
            return None

        # Extract and return the Base64 part after 'Basic '
        base64_part = authorization_header[len('Basic '):].strip()
        return base64_part
