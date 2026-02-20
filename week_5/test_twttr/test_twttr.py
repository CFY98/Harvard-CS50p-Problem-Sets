import pytest
from twttr import shorten

def test_correct():
    assert shorten("Twitter") == "Twttr"

def test_no_vowel():
    assert shorten("HP") == "HP"

def test_capitals():
    assert shorten("TWITTER") == "TWTTR"

def test_number():
    assert shorten("123") == "123"

def test_punctiation():
    assert shorten("Twitter.123") == "Twttr.123"

