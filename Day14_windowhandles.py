from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//button[@class='btn btn-info']").click()

handles=driver.window_handles
print(len(handles))

# for handle in handles:
#     # driver.switch_to_window(handle)
    # print(driver.title)
    # if driver.title=="Sakinalium | Home":
    #     driver.close()
