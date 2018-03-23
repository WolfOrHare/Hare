import selenium
import unittest
from objectfunction.login import LoginMAM
from objectpage.mam_personal_page import PersonalPage
from objectpage.mam_home_page import MAMHomePage

#这里的代码是有问题的，只是为了解决driver无法在不同页面传递所写的验证代码。
#可以通过简历objectfunction来实现，功能性操作的模拟。这样也不会存在页面跳转后driver丢失的情况
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