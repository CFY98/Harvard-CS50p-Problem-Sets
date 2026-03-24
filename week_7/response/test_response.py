from response import validate
import pytest

def test_validate():
    assert validate("malan@harvard.edu") == "Valid"
    assert validate("cfy98@github.com") == "Valid"
    assert validate("malan@@harvard.edu") == "Invalid"
    assert validate("malan@harvard..edu") == "Invalid"

