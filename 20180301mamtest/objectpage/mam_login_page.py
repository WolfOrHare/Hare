from framework.base_page import BasePage

class LoginPage(BasePage):

    input_user = "xpath=>//*[@id='username']"
    input_password = "name=>password"
    submit_btn="xpath=>//*/button[@type='submit']"
    # self.driver.find_element_by_xpath("//*[@id='username']").send_keys("mam")
    # self.driver.find_element_by_class_name("name=>password").send_keys("qwe123!@#2018")
    # self.driver.find_element_by_xpath("xpath=>//*/button[@type='submit']").click()


    def login_click(self):
        self.click(self.submit_btn)

    def type_user(self,text):
        self.type(self.input_user,text)

    def type_password(self,text):
        self.type(self.input_password,text)

    def login_sleep(self,seconds):
        self.sleep(seconds)