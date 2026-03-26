import pytest
from seasons import Minutes

def test_valid_input():
    m = Minutes.minutes("2000-10-03")
    assert isinstance(m, Minutes)
    assert str(m).endswith("minutes")
    assert m.minutes > 0

def test_invalid_input():
    with pytest.raises(SystemExit):
        Minutes.minutes("2000/10/03")
