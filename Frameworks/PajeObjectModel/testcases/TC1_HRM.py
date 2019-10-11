import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
sys.path.append("C:\\Users\\Admin\\PycharmProjects\\POT1")
from Frameworks.PajeObjectModel.pageObjects.LoginPage import LoginPage
import time

class LoginTest(unittest.TestCase):
    baseURL= "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
    username= "Admin"
    password= "admin123"
    driver= webdriver.Chrome(executable_path="C:\\Users\\Admin\\PycharmProjects\\POT1\\Frameworks\\PajeObjectModel\\drivers\\chromedriver.exe")

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp=LoginPage(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.loginbutton()
        time.sleep(4)
        self.assertEqual("OrangeHRM",self.driver.title,"Title is mismatching")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()

if __name__== '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Admin\\PycharmProjects\\POT1\\Frameworks\\PajeObjectModel\\reports"))

