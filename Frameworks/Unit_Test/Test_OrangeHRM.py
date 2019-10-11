import unittest
import HtmlTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class OrageTestHRM(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()

    def test_homepage(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM",self.driver.title,"Home page title is mismatching")

    def test_loginpage(self):
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        time.sleep(3)

    def test_loginpagetitle(self):
        self.assertEqual("OrangeHRM",self.driver.title,"Login page tile is mismatching")

    def test_logout(self):
        self.driver.find_element_by_xpath("//*[@id='welcome']").click()
        self.driver.find_element_by_xpath("//*[@id='welcome-menu']/ul/li[2]/a").click()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Admin\\PycharmProjects\\POT1\\Frameworks\\Unit_Test\\Reports'))



