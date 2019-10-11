import unittest

def setUpModule():
    print("This is setUp module method")

def tearDownModule():
    print("This is tearDown module method")

class AppTesting(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("This is setUp Class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("This is tearDown Class")

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
    @unittest.skip
    def test_prepaidrecharge(self):
        print("This is actual test for prepaid recharge method")
    @unittest.skipIf(1==1,"just wanted to skip this test")
    def test_postpaidpayment(self):
        print("This is actual test for postpaid payment method")


if __name__=="__main__":
    unittest.main()
