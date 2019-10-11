from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

import pytest
from selenium import webdriver

class TestFlightLogin():
    @pytest.mark.parametrize('user, password',[('mercury','mercury'),('mer','mercury'),('mercury','mer')])
    def test_login(self,user,password):
        self.driver=webdriver.Chrome(executable_path="C:/Drivers/chromedriver_win32/chromedriver.exe")
        self.driver.get("http://newtours.demoaut.com/")
        self.driver.find_element_by_name("userName").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("login").click()
        assert self.driver.title=="Find a Flight: Mercury Tours:"
        self.driver.quit()

''' 
@pytest.mark.parametrize('user,pasword',[('Admin','admin123'),('Admin','Admin123'),('admin','admin123')])
def test_login_chrome(self,user,pasword):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.implicitly_wait(5)
    self.driver.maximize_window()
    self.driver.get("https://opensource-demo.orangehrmlive.com")
    assert self.driver.title == "OrangeHRM"

    self.driver.find_element_by_name("txtUsername").send_keys(user)
    self.driver.find_element_by_name("txtPassword").send_keys(pasword)
    self.driver.find_element_by_name("Submit").click()
    time.sleep(5)
    assert self.driver.title == "OrangeHRM"
    self.driver.close()
'''

