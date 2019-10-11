import pytest

class TestCase1:

    def test_LoginByEmail(self):
        print("This is login by email test");
        assert True == True

    def test_LoginByFacebook(self):
        print("This is login by facebook test");
        assert True == True

    def test_LoginByTwitter(self):
        print("This is login by twitter test");
        assert True == True

    @pytest.mark.skip
    def test_signupByEmail(self):
        print("This is signup by email test")
        assert True == True

    def test_signupByFacebook(self):
        print("This is signup by facebook test")
        assert True == True

    def test_signbytwitter(self):
        print("This is signup by twitter test")
        assert True == True