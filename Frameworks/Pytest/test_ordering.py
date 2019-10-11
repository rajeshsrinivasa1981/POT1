import pytest

@pytest.mark.run(order=5)
def test_One():
    print("this is method One")

@pytest.mark.run(order=4)
def test_Two():
    print("this is method Two")

@pytest.mark.run(order=2)
def test_Three():
    print("this is method Three")
@pytest.mark.run(order=3)
def test_Four():
    print("this is method Four")

@pytest.mark.run(order=1)
def test_Five():
    print("this is method Five")
