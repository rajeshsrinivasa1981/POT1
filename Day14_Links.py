from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

''' 
driver.get("http://newtours.demoaut.com/")

links=driver.find_elements_by_tag_name("a")
print("Number of links present are",len(links))

LinkTexts=[]

for link in links:
    print (link.text)
    LinkTexts.append(link.text)

for linktext in LinkTexts:
    driver.find_element_by_link_text(linktext).click()
    driver.back()
'''

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.find_element_by_link_text("Software Testing Tutorials").click()
driver.back()
driver.find_element_by_partial_link_text("Tools Training").click()
driver.back()

driver.close()
driver.quit()




