import unittest


class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        print("This is setUp method")

    @classmethod
    def tearDown(self) -> None:
        print("This is tearDown method")

    def test_search(self):
        print("This is actual test for search method")

    def test_advancedsearch(self):
        print("This is actual test for advanced search method")

    def test_prepaidrecharge(self):
        print("This is actual test for prepaid recharge method")

    def test_postpaidpayment(self):
        print("This is actual test for postpaid payment method")


if __name__=="__main__":
    unittest.main()
