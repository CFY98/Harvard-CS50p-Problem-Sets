from bank import value

def test_startswith_hello():
    assert value("hello") == 0
    assert value("hello world") == 0
    assert value("HELLO WORLD") == 0

def test_startswith_h():
    assert value("happy") == 20
    assert value("HAPPY") == 20

def test_other():
    assert value("world") == 100
    assert value("123") == 100
    assert value("...HELLO") == 100
