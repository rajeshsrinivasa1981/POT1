from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

''' 
slider=driver.find_element_by_xpath("//*[@class='ui-slider-handle ui-corner-all ui-state-default']")
driver.execute_script("arguments[0].scrollIntoView();",slider)
actions=ActionChains(driver)
actions.move_to_element(slider).drag_and_drop_by_offset(slider,300,0).perform()
'''
resizable=driver.find_element_by_xpath("//*[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
driver.execute_script("arguments[0].scrollIntoView();",resizable)

actions=ActionChains(driver)
actions.move_to_element(resizable).drag_and_drop_by_offset(resizable,100,150).perform()
