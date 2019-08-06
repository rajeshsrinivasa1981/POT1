from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()

''' 
driver.get("https://www.google.com/")
button=driver.find_element_by_name("btnK")
actions.move_to_element(button).perform()
'''


driver.get("https://www.actitime.com/features")
features = driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[2]/a")
actions = ActionChains(driver)
actions.move_to_element(features).click().perform() #MouseHover
time.sleep(5)




