from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.execute_script("window.scrollBy(0,300)","")


tenuredrplist=Select(driver.find_element_by_id("tenurePeriod"))
print(len(tenuredrplist.options))
tenuredrplist.select_by_visible_text("day(s)")


frqdrplist=Select(driver.find_element_by_id("frequency"))
print(len(frqdrplist.options))
frqdrplist.select_by_visible_text("Compounded Monthly")