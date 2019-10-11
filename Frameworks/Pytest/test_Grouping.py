import pytest

class TestCase3():

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginbyemail(self):
        print("This is login test by email")
        assert True == True

    @pytest.mark.regression
    def test_loginbyFacebook(self):
        print("This is login by Facebook")
        assert True == True

    @pytest.mark.regression
    def test_loginnbyTwitter(self):
        print("This is login by Twitter")
        assert True == True

    @pytest.mark.sanity
    def test_signupbyemail(self):
        print("This is signup by email")

    @pytest.mark.sanity
    def test_signupbyFacebook(self):
        print("This is signup by Facebook")
        assert True==True

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_signupbyTwitter(self):
        print("This is signup by Twitter")
        assert True==True




