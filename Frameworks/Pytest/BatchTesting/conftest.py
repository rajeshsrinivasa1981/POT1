import pytest

@pytest.fixture()
def setup():
    print("Launching the browser....")
    yield
    print("Closing the browser.....")