from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

source_element=driver.find_element_by_xpath("//*[@id='box6']")
target_element=driver.find_element_by_xpath("//*[@id='box103']")
actions=ActionChains(driver)
actions.drag_and_drop(source_element,target_element).perform()

