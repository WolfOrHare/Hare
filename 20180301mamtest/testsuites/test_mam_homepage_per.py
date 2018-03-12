import selenium
import unittest
from objectfunction.login import LoginMAM
from objectpage.mam_personal_page import PersonalPage
from objectpage.mam_home_page import MAMHomePage

class test_123(unittest.TestCase):

    def setUp(self):
       self.login = LoginMAM(self)
       self.login.initSetup()
       self.login.loginValid()
       self.driver = self.login.driver

    def test_per(self):
        hpage = MAMHomePage(self.driver)
        hpage_el = hpage.find_element("xpath=>//*[@id='mymam_link']")
        hpage_el.click()


if __name__ == '__main__':
    unittest.main