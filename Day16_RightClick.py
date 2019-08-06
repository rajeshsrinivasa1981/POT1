from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

button=driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
actions=ActionChains(driver)
actions.context_click(button).perform()

#Copy:
driver.find_element_by_xpath("/html/body/ul/li[3]/span").click()

driver.switch_to_alert().accept()
