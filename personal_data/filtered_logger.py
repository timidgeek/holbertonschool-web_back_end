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
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    function that uses a regex to replace occurences of certain
    field values
    """
    sep = separator
    pattern = f'({sep}|^)({"|".join(map(re.escape, fields))})=([^{sep}]*)'
    return re.sub(pattern, rf'\1\2={redaction}', message)
