"""
Test function for parse_syslog.py
"""
import pytest
from parse_syslog import parse_syslog_entry

@pytest.fixture(name="entry")
def fixture_entry():
    """
    pytest fixture
    """
    return "Apr 22 12:34:56 hostname Your syslog message here"

def test_parse_syslog_entry(entry):
    """
    Test function for parse_syslog.py
    """
    assert parse_syslog_entry(entry)["timestamp"] == "Apr 22 12:34:56"
    assert parse_syslog_entry(entry)["hostname"] == "hostname"
    assert parse_syslog_entry(entry)["message"] == "Your syslog message here"
