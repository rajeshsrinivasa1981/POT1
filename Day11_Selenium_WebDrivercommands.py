"""
Run tests through chrome browser
Run tests through firefox browser
Run test through edge browser

Open and URL
Get the Title of the URL
Get the current URL
Navigation commands - forward, back
Condition commands - is_enabled, is_displayed, is_selected

#Chrome Browser Launch
driver = webdriver.Chrome(executable_path="C:/Users/RS042424/Downloads/Drivers/chromedriver_win32/chromedriver.exe")

#Launching Firefox Browser
driver = webdriver.Firefox(executable_path="C:/Users/RS042424/Downloads/Drivers/geckodriver-v0.24.0-win64/geckodriver.exe")

#Launching Edge Browser - https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
driver = webdriver.Edge(executable_path="C:/Users/RS042424/Downloads/Drivers/MicrosoftWebDriver.exe")
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.udemy.com/")
print(driver.title) #prints the title of the page


driver.get("http://demo.automationtesting.in/")
print(driver.title)


driver.back()
print(driver.current_url) #prints the current URL of the page

driver.forward()
print(driver.current_url)


v1=driver.find_element_by_id("email").is_displayed()
print(v1)
v2=driver.find_element_by_id("email").is_enabled()
print(v2)


v3=driver.find_element_by_xpath("//*[@id='enterimg']").is_enabled()
print(v3)

driver.find_element_by_xpath("//*[@id='enterimg']").click()

v4=driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[5]/div/label[1]/input").is_enabled()
print(v4)
driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[5]/div/label[1]/input").click()
v5=driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[5]/div/label[1]/input").is_enabled()
print(v5)

driver.close() #closes the current browser/page
driver.quit() #closes all the open pages and browser














