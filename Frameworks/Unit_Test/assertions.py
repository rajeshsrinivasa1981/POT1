import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Test(unittest.TestCase):
    def testName(self):
        self.driver= None #webdriver.Chrome(ChromeDriverManager().install())
        """ 
        self.driver.get("https://www.google.com/")
        Title=self.driver.title
        
        self.assertEqual("Google",Title,"Same title as expected")
        self.assertNotEqual("Google12",Title,"Title is not matching")
        """
        self.assertIsNone(self.driver)

        list={"python","selenium","java"}
        self.assertIn("python",list)

        self.assertGreater(100,90)
        self.assertGreaterEqual(100,100)

if __name__=="__main__":
    unittest.main()