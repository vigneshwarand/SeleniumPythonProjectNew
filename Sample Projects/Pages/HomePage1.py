class HomePage1():
    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_id = "welcome"
        self.logout_link_linkText = "Logout"


    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()