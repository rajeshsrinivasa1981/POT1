'''
Locators
====================
id
name
Link:
    Link text
    partial link text
CSS Selector :
    tagname and id
    tagname and class,
    tagname and attribute
    tagname, class and attribute

XPath:
Absolute XPath or Full Path
Relative XPath or Partial path
Dynamic XPath
'''



'''

#Locator by ID - 
driver.find_element_by_id("value of id")

#Locatory by Name - 
driver.find_element_by_name("value of name")

#Locatory by Linktext - 
driver.find_element_by_linktext("complete link text")

#Locator by PartialLinkText - 
driver.find_element_by_partiallinktext("partial link text")

#CSS Selector by ID 
driver.find_element_CSSSelector("tagname#id")

#CSS Selector by class
driver.find_element_CSSSelector("tagname.classname")

#CSS Selector by attribute
driver.find_element_CSSSelector("tagname[attribute=value])

#CSS Selector by tagname, class and attribute
driver.find_element_CSSSelector("tagname.classname[attibute=value])

#Xpath (Absolute or Full XPath) 

driver.find_element_by_xpath("/html/body/div/table/")

#Xpath (Relative or partial xpath) 

driver.find_element_by_xpath("//tagname[@attribute='value']")

#Contains 
driver.find_element_by_xpath("//tagname[contains(@attribute,'value')]")

#Contains with text 
driver.find_element_by_xpath("//tagname[contains(text(),'text')]")


OR - 

//tagname[@attribute1='value' OR @attribute2='value']

AND 

//tagname[@attribute1='value' AND @attribute2='value']


Starts with - 

//tagname[starts-with(text(),'Message')]

text - 

//tagname[text()='Message']

preceeding - 

//tagname[@attribute='value']//preceeding::input[3]

following - 

//tagname[@attribute='value']//following::input[3]







'''






#Locator by ID

from selenium import webdriver

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()

''' 
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("rajesh.srinivasa") #Locator by ID
driver.find_element_by_name("pass").send_keys("rajesh") #Locator by NAME
driver.find_element_by_link_text("Forgotten account?").click()
driver.find_element_by_css_selector("input#identify_email").send_keys("rajesh.srinivasa@gmail.com")
driver.find_element_by_xpath("//span[@class='uiButtonText']").click()
'''

''' 
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_xpath("//input[@name='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//input[@name='Submit']").click()
driver.find_element_by_partial_link_text("Welcome").click()
driver.find_element_by_link_text("Logout").click()
'''













