from selenium import webdriver
import time

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://money.rediff.com/gainers/bse/daily")

''' 
#Approach 1 scrolling by pixel
driver.execute_script("window.scrollBy(0,3000)","")

#Approach 2 scrolling till the end

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
'''

#Approach 3 scrolling till the element is visible
img=driver.find_element_by_xpath("//img[contains(@class,'red_on_net_img')]")
driver.execute_script("arguments[0].scrollIntoView();",img)






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











