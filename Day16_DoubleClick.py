from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()

driver.get("https://api.jquery.com/dblclick/")

driver.switch_to_frame(0)
ele=driver.find_element_by_xpath("/html/body/div")
driver.execute_script("arguments[0].scrollIntoView();",ele)

actions=ActionChains(driver)

for i in range(1,5):
    actions.double_click(ele).perform()
    time.sleep(5)

