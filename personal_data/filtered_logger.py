#!/usr/bin/env python3
"""
function that returns an obfuscated log message

arguments:
    `fields`
        a list of strings representing all fields to obfuscate
    `redaction`
        a string representing by what the field will be obfuscated
    `message`
        a string representing the log line
    `separator`
        a string representing by which character is separating all
        fields in the log line (message)
"""
import os
import mysql.connector
import re
import logging
from typing import List


# Function Definitions
def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connects to a MySQL database using environment variables for credentials.
    Returns a MySQLConnection object.
    """
    # Get database credentials from environment variables
    db_username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    # Create a database connection
    try:
        connection = mysql.connector.connect(
            user=db_username,
            password=db_password,
            host=db_host,
            database=db_name
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    function that uses a regex to replace occurences of certain
    field values
    """
    sep = separator
    pattern = f'({sep}|^)({"|".join(map(re.escape, fields))})=([^{sep}]*)'
    return re.sub(pattern, rf'\1\2={redaction}', message)


def get_logger() -> logging.Logger:
    """
    Returns:
        logging.Logger: _description_
    """
    # create logger named "user_data"
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)  # set logging level to INFO

    # create a StreamHandler with RedactingFormatter as formatter
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    # add StreamHandler to the logger
    logger.addHandler(stream_handler)

    # disable message propagation to other loggers
    logger.propagate = False

    return logger


# list of fields considered as PII
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


# Class Definitions
class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Args:
            record (logging.LogRecord): _description_

        Returns:
            str: _description_
        """
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            message, self.SEPARATOR)
