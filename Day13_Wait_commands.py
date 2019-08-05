from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

driver = webdriver.Chrome(ChromeDriverManager().install())
wait=WebDriverWait(driver,120,poll_frequency=10,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
#driver.implicitly_wait(10)
driver.maximize_window()


'''' 
driver.get("https://www.google.com/")
inputElement = driver.find_element_by_name("q")
inputElement.send_keys("Selenium")
inputElement.submit()
'''

driver.get("http://newtours.demoaut.com/")
wait.until(EC.title_is("Welcome: Mercury Tours"))

try:

    #username
    username = wait.until(EC.presence_of_element_located((By.NAME,"userName")))
    username.send_keys("mercury")

    #password
    password = wait.until(EC.presence_of_element_located((By.NAME,"password")))
    password.send_keys("mercury")


    #Login
    signin= wait.until(EC.element_to_be_clickable((By.NAME,"login")))
    signin.submit()

    #oneway
    oneway_rad = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value=oneway]')))
    oneway_rad.click()

except Exception:
    print("Element is not present on webpage.....")






























