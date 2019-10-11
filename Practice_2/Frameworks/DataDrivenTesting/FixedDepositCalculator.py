from Practice_2.Frameworks.DataDrivenTesting import XlUttils
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

path="C:\Learning\Selenium\DDT\caldata.xlsx"

rows=XlUttils.getrowcount(path,"Sheet1")

for r in range(2,rows+1):
    principal=XlUttils.readdata(path,"Sheet1",r,1)
    rateofinterest = XlUttils.readdata(path, "Sheet1", r, 2)
    period = XlUttils.readdata(path, "Sheet1", r, 3)
    duration=XlUttils.readdata(path,"Sheet1",r,4)
    frequency = XlUttils.readdata(path, "Sheet1", r, 5)
    exp_mvalue = XlUttils.readdata(path, "Sheet1", r, 6)

    #passing values to elements in application
    driver.find_element_by_id("principal").send_keys(principal)
    driver.find_element_by_id("interest").send_keys(rateofinterest)
    driver.find_element_by_id("tenure").send_keys(period)

    durdrpdown=Select(driver.find_element_by_id("tenurePeriod"))
    durdrpdown.select_by_visible_text(duration)

    frqdrpdwon=Select(driver.find_element_by_id("frequency"))
    frqdrpdwon.select_by_visible_text(frequency)

    driver.find_element_by_xpath("//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    time.sleep(3)

    act_mvalue=driver.find_element_by_xpath("//*[@id='resp_matval']/strong").text
    print(act_mvalue)
    XlUttils.writedata(path,"Sheet1",r,7,act_mvalue)

    if (float(exp_mvalue)==float(act_mvalue)):
        print("Test Passed")
        XlUttils.writedata(path,"Sheet1",r,8,"Passed")
    else:
        print("Test Failed")
        XlUttils.writedata(path,"Sheet1",r,8,"Failed")

    driver.find_element_by_xpath("//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(5)



