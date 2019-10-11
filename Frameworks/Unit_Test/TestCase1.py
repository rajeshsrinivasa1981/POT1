import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class SearchEngines(unittest.TestCase):
    def test_Google(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.google.com/")
        print("Title of page:"+self.driver.title)

    def test_Bing(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.bing.com/")
        print("Title of page:"+self.driver.title)

if __name__=="__main__":
    unittest.main()
