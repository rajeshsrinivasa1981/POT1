import pytest

class TestCase1:

    @pytest.fixture()
    def setup(self):
        print("Once before every test method")
        yield
        print("Once after every test method")

    def testMethod1(self,setup):
        print("This is test method 1")

    def testMehod2(self, setup):
            print("This is test method 2")

    def testMehod2(self, setup):
            print("This is test method 2")

    def testMehod2(self, setup):
            print("This is test method 2")

    def testMehod2(self, setup):
            print("This is test method 2")
