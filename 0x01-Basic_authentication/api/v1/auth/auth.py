#!/usr/bin/env python3
"""
"""
from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """"""
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
