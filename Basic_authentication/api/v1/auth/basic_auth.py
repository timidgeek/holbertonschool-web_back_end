#!/usr/bin/env python3
"""
class that inherits from Auth
"""
from flask import request
from typing import List, TypeVar
import os
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
  """
  class that inherits from auth
  """
