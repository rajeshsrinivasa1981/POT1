import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentindollor(self):
        print("This is Payment in dollor test")
        self.assertTrue(True)

    def test_paymentinrupees(self):
        print("This is Paymenet in rupees test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()