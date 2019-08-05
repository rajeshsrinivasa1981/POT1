from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

''' 
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element_by_xpath("//button[contains(text(),'Click Me')]").click()
driver.switch_to_alert().accept()
msg=driver.find_element_by_id("demo").text
if msg=="You pressed OK!":
    print("Test passed for OK button")
else:
    print("Test Failed for ok button")

driver.find_element_by_xpath("//button[contains(text(),'Click Me')]").click()
driver.switch_to_alert().dismiss()
msg=driver.find_element_by_id("demo").text
if msg=="You pressed Cancel!":
    print("Test passed for Cancel button")
else:
    print("Test Failed for Cancel button")

driver.close()
driver.quit()
'''

driver.get("http://demo.automationtesting.in/Alerts.html")
driver.find_element_by_xpath("//a[@href='#Textbox']").click()
driver.find_element_by_xpath("//button[@class='btn btn-info']").click()
alert=driver.switch_to_alert()
time.sleep(5)
alert.send_keys("rajesh")
alert.accept()

msg=driver.find_element_by_xpath("//*[@id='demo1']").text
if msg=="Hello rajesh How are you today":
    print("Test passed")
else:
    print("Test failed")

driver.close()
driver.quit()




