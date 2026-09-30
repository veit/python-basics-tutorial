import re

from hypothesis import given
from hypothesis.strategies import emails


def parse_email(email):
    result = re.match(r"(?P<username>\w+).(?P<domain>[\w\.]+)", email).groups()
    return result


@given(emails())
def test_parse_email(email):
    result = parse_email(email)
    # print(result)
    assert len(result) == 2
    assert "." in result[1]
