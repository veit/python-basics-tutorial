from datetime import datetime
from unittest.mock import Mock

# Define two test days
monday = datetime(year=2021, month=10, day=11)
saturday = datetime(year=2021, month=10, day=16)

def is_workingday():
    today = datetime.today()
    return (0 <= today.weekday() < 5)

datetime = Mock()

# Mock .today() to return Tuesday
datetime.today.return_value = monday
# Test Tuesday is a weekday
assert is_workingday()
# Mock .today() to return Saturday
datetime.today.return_value = saturday
# Test Saturday is not a weekday
assert not is_workingday()
