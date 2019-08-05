from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#Input boxes
driver.find_element_by_id("RESULT_TextField-1").send_keys("Rajesh")
driver.find_element_by_id("RESULT_TextField-2").send_keys("Srinivasa")
driver.find_element_by_id("RESULT_TextField-3").send_keys("9845958919")
driver.find_element_by_id("RESULT_TextField-4").send_keys("India")
driver.find_element_by_id("RESULT_TextField-5").send_keys("Bangalore")
driver.find_element_by_id("RESULT_TextField-6").send_keys("rajesh.srinivasa@gmail.com")

#Radio buttons
radiobutton= driver.find_element_by_xpath("//label[contains(text(),'Male')]")
print(radiobutton.is_selected())
radiobutton.click()

#Dropdown button

drp=Select(driver.find_element_by_id("RESULT_RadioButton-9"))

#counting the number of options present in dropdown -

print(len(drp.options))

all_options=drp.options

for options in all_options:
    print(options.text)

drp.select_by_value("Radio-1")

#check boxes

all_checkboxes = driver.find_elements_by_xpath("//input[@name='RESULT_CheckBox-8']//following::label[1]")
for label in all_checkboxes:
    print(label.text)
    if label.text in ["Wednesday","Thursday","Friday"]:
        label.click()








