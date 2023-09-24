#!/usr/bin/env python3
"""
class that inherits from Auth
"""
from typing import TypeVar
import re
import base64
from api.v1.auth.auth import Auth
from models.user import User


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

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """ returns the decoded value of a Base64 string """
        if not base64_authorization_header \
                or type(base64_authorization_header) is not str:
            return None
        try:
            return base64.b64decode(
                base64_authorization_header
            ).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """  returns the user email and password from the Base64 value """
        if decoded_base64_authorization_header is None \
                or type(decoded_base64_authorization_header) != str \
                or not re.search(':', decoded_base64_authorization_header):
            return None, None
        return tuple(re.split(':', decoded_base64_authorization_header))

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """ returns the User instance based on his email and password """
        if user_email is None or type(user_email) is not str \
                or user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            user = User.search({'email': user_email})
            if len(user) == 0 or not user[0].is_valid_password(user_pwd):
                return None
            return user[0]
        except KeyError:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads Auth and retrieves the User instance """
        auth_header = self.authorization_header(request)
        base64_auth_header = self.extract_base64_authorization_header(auth_header)  # noqa
        decoded_base64_authorization_header = self.decode_base64_authorization_header(base64_auth_header)  # noqa
        user_email, user_password = self.extract_user_credentials(decoded_base64_authorization_header)  # noqa
        return self.user_object_from_credentials(user_email, user_password)
