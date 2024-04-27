#!/usr/bin/env python3
"""
Interacts with authentication database.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
        The returned bytes is a salted hash of the input password
        hashed with bcrypt.hashpw.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
