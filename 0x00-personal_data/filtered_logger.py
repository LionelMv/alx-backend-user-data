#!/usr/bin/env python3
"""This  module contains user data management"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscate specified fields in a log message.

    Args:
    fields (List[str]): A list of strings representing fields to obfuscate.
    redaction (str): A string representing the replacement
        for obfuscated fields.
    message (str): A string representing the log line to be obfuscated.
    separator (str): A string representing the character that separates
        fields in the log message.

    Returns:
    str: The obfuscated log message.
    """
    # pattern = '|'.join(fields)
    # print(pattern)
    # return re.sub(f'({pattern})=[^;]+', f'\\1={redaction}', message)

    for field in fields:
        replace = f"{field}={redaction}{separator}"
        message = re.sub(fr"{field}=[\w/]*;", replace, message)
    return message
