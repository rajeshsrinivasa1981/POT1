from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://demo.automationtesting.in/Register.html")


#Languages

driver.find_element_by_xpath("//div[@id='msdd']").click()

langs=driver.find_elements_by_xpath("//*[@id='basicBootstrapForm']/div[7]/div/multi-select/div[2]/ul/li/a")
print(len(langs))

for language in langs:
    print (language.text)

langs.pop(3).click()
langs.pop(4).click()

#Skills

skills=Select(driver.find_element_by_xpath("//select[@id='Skills']"))
print(len(skills.options))

skills.select_by_index(4)

#Country -

driver.find_element_by_xpath("//span[@class='select2-selection select2-selection--single']").click()
driver.find_element_by_xpath("//input[@class='select2-search__field']").send_keys("India")
time.sleep(5)
driver.find_element_by_xpath("//input[@class='select2-search__field']").send_keys(Keys.RETURN)





