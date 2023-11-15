#!/usr/bin/env python3
"""
Basic Authentication implementation module.
"""
import base64
from .auth import Auth
from flask import request
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    Class to implement Basic Authentication.
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorzation header for
        a Basic Authentication.
        """
        if authorization_header is None or type(authorization_header) != str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        else:
            return authorization_header.split("Basic ")[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Returns the decoded value of a Base64 string.
        """
        if base64_authorization_header is None or \
                type(base64_authorization_header) != str:
            return None

        try:
            return base64.b64decode(
                base64_authorization_header).decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Returns the username and the password from
        the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None or\
            type(decoded_base64_authorization_header) != str or\
                ":" not in decoded_base64_authorization_header:
            return None, None
        user_credentials = decoded_base64_authorization_header.split(":", 1)
        return user_credentials[0], user_credentials[1]

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None

        try:
            users = User.search({'email': user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None
