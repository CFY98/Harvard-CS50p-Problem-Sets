from um import count
import pytest

def test_ums():
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1
    assert count(" um ") == 1
    assert count("yum") == 0
    assert count("UM") == 1
