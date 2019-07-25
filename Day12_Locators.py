'''
Locators
====================
id
name
Link:
    Link text
    partial link text
CSS Selector :
    tagname and id
    tagname and class,
    tagname and attribute
    tagname, class and attribute

XPath:
Absolute XPath or Full Path
Relative XPath or Partial path
Dynamic XPath
'''


#Locator by ID

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()

''' 
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("rajesh.srinivasa") #Locator by ID
driver.find_element_by_name("pass").send_keys("rajesh") #Locator by NAME
driver.find_element_by_link_text("Forgotten account?").click()
driver.find_element_by_css_selector("input#identify_email").send_keys("rajesh.srinivasa@gmail.com")
driver.find_element_by_xpath("//span[@class='uiButtonText']").click()
'''

''' 
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_xpath("//input[@name='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//input[@name='Submit']").click()
driver.find_element_by_partial_link_text("Welcome").click()
driver.find_element_by_link_text("Logout").click()
'''













