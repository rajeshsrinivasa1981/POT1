import unittest

class SignUpTest(unittest.TestCase):
    def test_signupByEmail(self):
        print("This is signup by email test")
        self.assertTrue(True)

    def test_signupByFacebook(self):
        print("This is signup by facebook test")
        self.assertTrue(True)

    def test_signbytwitter(self):
        print("This is signup by twitter test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()