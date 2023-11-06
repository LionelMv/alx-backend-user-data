#!/usr/bin/env python3
"""
Module manages API authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Defines which routes don't need authentication.
        Returns True if path is not in excluded paths, else False.
        """
        if path is None:
            return True

        if not excluded_paths:
            return True

        if not path.endswith("/"):
            path += "/"

        for excluded_path in excluded_paths:
            if path != excluded_path:
                return True

        return False

    def authorization_header(self, request=None) -> str:
        """"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """"""
        return None
