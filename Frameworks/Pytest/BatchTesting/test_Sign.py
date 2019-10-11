import pytest

class TestSignup():

    def test_signupbyemail(self,setup):
        print("This is signup by email")

    def test_signupbyFacebook(self,setup):
        print("This is signup by Facebook")
        assert True == True

    def test_signupbyTwitter(self,setup):
        print("This is signup by Twitter")
        assert True == True
