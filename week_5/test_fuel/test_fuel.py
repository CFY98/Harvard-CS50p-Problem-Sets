import pytest
from fuel import gauge, convert

def test_convert():
    assert convert("5/6") == 83
    assert convert("99/100") == 99
    assert convert("0/100") == 0
    assert convert("1/100") == 1

    with pytest.raises(ZeroDivisionError):
            convert("2/0")
    for invalid in ["cat/dog", "3/2", "-1/3"]:
        with pytest.raises(ValueError):
            convert(invalid)

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"


