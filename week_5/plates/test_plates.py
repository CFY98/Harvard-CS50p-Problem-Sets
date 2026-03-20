from plates import is_valid

# Min 2 characters, max 6.
def test_valid_length():
    assert is_valid("hello") == True
    assert is_valid("he") == True
    assert is_valid("abcdefg") == False

def test_no_numbers():
    assert is_valid("ABCDEF") == True

def test_no_letters():
    assert is_valid("123456") == False
    assert is_valid("123") == False

def test_cannot_have_zero():
    assert is_valid("012345") == False
    assert is_valid("hell0") == False

# Needs to start with two alphabetical characters.
def test_startwith_2_letters():
    assert is_valid("C50") == False
    assert is_valid("c50") == False
    assert is_valid("CS50") == True
    assert is_valid("cs50") == True

# Numbers valid after the second character
def test_numbers_after_2_letters():
    assert is_valid("h3ll0") == False
    assert is_valid("he112") == True
    assert is_valid("he11o") == False

def test_no_punctuation():
    assert is_valid("!CS50") == False
    assert is_valid("cs50!") == False

