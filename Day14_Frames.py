from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
driver.switch_to_frame("packageListFrame")
driver.find_element_by_link_text("com.thoughtworks.selenium").click()

driver.switch_to_default_content()

driver.switch_to_frame("packageFrame")
driver.find_element_by_xpath("//span[contains(text(),'CommandProcessor')]").click()

driver.switch_to_default_content()

driver.switch_to_frame("classFrame")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/ul[1]/li[5]/a[1]").click()

driver.close()
driver.quit()





