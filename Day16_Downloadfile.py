from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chromeoptions=Options()
chromeoptions.add_experimental_option("prefs",{"download.default_directory":"C:\Downloads"})

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),chrome_options=chromeoptions)
driver.maximize_window()

driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.find_element_by_id("textbox").send_keys("testing text file....")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()


driver.find_element_by_id("pdfbox").send_keys("testing pdf file....")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()



