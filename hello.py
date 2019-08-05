from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com/flights#flt=/m/09c17..2019-08-18*./m/09c17.2019-08-22;c:INR;e:1;ls:1w;sd:0;t:h")
driver.implicitly_wait(10)

driver.find_element_by_xpath("//div[@class='flt-input gws-flights-form__input-container gws-flights__flex-box gws-flights-form__airport-input gws-flights-form__swapper-right']").click()
driver.find_element_by_xpath("//div[@class='fsapp-nearby-button']").click()
driver.find_element_by_xpath("//span[contains(text(),'Chennai International Airport')]").click()



