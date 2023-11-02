#!/usr/bin/env python3
"""This  module contains user data management"""
import re
from typing import List
import logging


PII_FIELDS = ('name', 'password', 'phone', 'ssn', 'email')


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
        # message = re.sub(fr"{field}=[\w/]*{separator}", replace, message)
        message = re.sub(fr"{field}=.*?{separator}", replace, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """this function filters values in incoming log records using
         filter_datum function"""
        message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION, message,
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """this method returns a user data logger"""
    log = logging.getLogger('user_data')
    log.setLevel(logging.INFO)
    log.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    log.addHandler(stream_handler)
    return log