from code import *

def test_add():
    assert add(2, 3) == 5
    assert add(2, 3) != 6

def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(2, 3) != 1

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(2, 3) != 7

def test_divide():
    assert divide(2, 3) == 0.6666666666666666
    assert divide(2, 3) != 0.6666666666666667


test_add()
test_subtract()
test_multiply()
test_divide()