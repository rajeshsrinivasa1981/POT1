from selenium import webdriver
import time

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://money.rediff.com/gainers/bse/daily")

''' 
pager=driver.find_element_by_xpath("//*[@id='leftcontainer']/div[4]")
pager_groups = pager.find_elements_by_tag_name("a")
print(len(pager_groups))

groups=[]

for grouplink in pager_groups:
    print(grouplink.text)
    groups.append(grouplink.text)

for g in groups:
    print(g)
    driver.find_element_by_link_text(g).click()

    noOfRows = len(driver.find_elements_by_xpath("//*[@id='leftcontainer']/table/tbody/tr"))
    noOfColumns=len(driver.find_elements_by_xpath("//*[@id='leftcontainer']/table/thead/tr/th"))
    for r in range(1,noOfRows+1):
        for c in range(1,noOfColumns+1):
            value=driver.find_element_by_xpath("//div[@id='leftcontainer']/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
            print(value,"  ")
        print()

'''











