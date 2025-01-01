from hello1 import hello

def test_default():
    assert hello() == "Hello, World!"

def test_argument():
    assert hello("David") == "Hello, David"

def test_list():
    for name in ["Hermione","Harry","Ron"]:
        assert hello(name) == f"Hello, {name}"