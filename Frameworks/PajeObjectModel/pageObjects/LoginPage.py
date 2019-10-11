class LoginPage():
    #Locators of all the elements
    txtbox_username_id="txtUsername"
    txtbox_password_id="txtPassword"
    btn_login_id="btnLogin"
    Homemenu_link_id="welcome"
    Logout_link_xpath="//*[@id='welcome-menu']/ul/li[2]/a"

    #actions on elements
    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,username):
        self.driver.find_element_by_id(self.txtbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.txtbox_password_id).send_keys(password)

    def loginbutton(self):
        self.driver.find_element_by_id(self.btn_login_id).click()

    def welcomelink(self):
        self.driver.find_element_by_id(self.Homemenu_link_id).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.Logout_link_xpath).click()





