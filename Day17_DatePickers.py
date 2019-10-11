from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.phptravels.net/")
month="December 2019"
day="25"

driver.find_element_by_xpath("//*[@id='flights']/form/div[3]/div/input").click()
time.sleep(5)
while True:
    text=driver.find_element_by_xpath("//div[15]//div[1]//tr[1]//th[2]").text
    print(text)
    if(text==month):
        break
    else:
        driver.find_element_by_xpath("//div[15]//div[1]//tr[1]//th[3]").click()

driver.find_element_by_xpath("//table/tbody/tr/td[contains(text(),"+str(day)+")]").click()
