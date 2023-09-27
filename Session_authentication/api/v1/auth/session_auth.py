#!/usr/bin/env python3
"""
new authentication mechanism that will:

  - validate if everything inherits correctly
    without any overloading
  - validate the “switch” by using environment
    variables

"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """
    session auth class that inherits from auth
    """
    # empty dict class attr
    user_id_by_session_id = dict()

    def create_session(self, user_id: str = None) -> str:
        """
        creates a new session
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        # generate random session_id with uuid4()
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id = {session_id: user_id}
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns `user_id` based on a `session_id`
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
