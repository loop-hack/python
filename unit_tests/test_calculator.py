'''from calculator1 import square

def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 square was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 square was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 square was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 square was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 square was not 0")

if __name__ == "__main__":
    main()
'''

"""as we can see above code fro testing has so many lines
that's why we gonna use pytest library that will do try except
printing for me and bcz of that our code will have less lines"""

#using pytest library which makes testing easier


'''from calculator1 import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
'''

""" in above code when something will be wrong 
lets say -2 is not 4 then then in terminal pytest only shows 
upto first error it does'nt test remaining and not provide list of every assertion that went wrong"""

#crreating seperate test so that pytest check cases each indivisualy


import pytest
from calculator1 import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):  #USE to mainatain error when user provide str instead of int
        square("cat")
