from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeDriverManager

import time

class TestLogin:

    def test_login_chrome(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        assert self.driver.title == "OrangeHRM"

        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        time.sleep(5)
        assert self.driver.title == "OrangeHRM"
        self.driver.close()

    def test_login_firefox(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        assert self.driver.title == "OrangeHRM"

        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        time.sleep(5)
        assert self.driver.title == "OrangeHRM"
        self.driver.close()

    def test_login_Edge(self):
        self.driver = webdriver.Edge(executable_path=EdgeDriverManager().install())
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        assert self.driver.title == "OrangeHRM"

        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        time.sleep(5)
        assert self.driver.title == "OrangeHRM"
        self.driver.close()