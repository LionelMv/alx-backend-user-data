#!/usr/bin/env python3
"""
Basic Authentication implementation module.
"""
from .auth import Auth
from flask import request


class BasicAuth(Auth):
    """
    Class to implement Basic Authentication.
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        if authorization_header is None or type(authorization_header) != str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        else:
            return authorization_header.split("Basic ")[1]
