"""
Parse syslog entry function
"""
import re

def parse_syslog_entry(entry):
    """
    Parse syslog function, it returns timestamp, hostname and message
    """
    pattern = r"^(\
    ?P<timestamp>\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}) (?P<hostname>\S+) (?P<message>.*)$"
    match = re.match(pattern, entry)
    if match:
        return match.groupdict()
    return None
