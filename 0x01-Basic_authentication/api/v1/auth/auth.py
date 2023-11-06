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

        if excluded_paths is None or not excluded_paths:
            return True

        if not path.endswith("/"):
            path += "/"

        for excluded_path in excluded_paths:
            if path == excluded_path or path.startswith(excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Validates all requests to secure the API.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Checks if current user is forbidden to request services or not.
        """
        return None
