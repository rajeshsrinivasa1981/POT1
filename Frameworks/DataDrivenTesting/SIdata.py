from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Frameworks.DataDrivenTesting import XlUtlis
import time

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.easycalculation.com/simple-interest.php")

path="C:\Selenium\SIdata.xlsx"
rows= XlUtlis.getrowcount(path, "Sheet1")

for r in range(2,rows+1):
    Principle= XlUtlis.readdatafile(path, "Sheet1", r, 1)
    ROI= XlUtlis.readdatafile(path, "Sheet1", r, 2)
    Time= XlUtlis.readdatafile(path, "Sheet1", r, 3)
    ExpSI= XlUtlis.readdatafile(path, "Sheet1", r, 4)
    print(ExpSI)

    driver.find_element_by_name("res1").send_keys(Principle)
    driver.find_element_by_name("res2").send_keys(ROI)
    driver.find_element_by_name("res3").send_keys(Time)
    ActSI=driver.find_element_by_name("res4").get_attribute('value')
    time.sleep(3)
    print(ActSI)
    if(ExpSI==ActSI):
        print("Test Passed")
        XlUtlis.writedatafile(path, "Sheet1", r, 5, "Passed")
    else:
        print("Test Failed")
        XlUtlis.writedatafile(path, "Sheet1", r, 5, "Failed")

    driver.find_element_by_xpath("//*[@id='dispCalcConts']/input[2]").click()
    time.sleep(5)