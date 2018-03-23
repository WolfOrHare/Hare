from objectpage.mam_home_page import MAMHomePage
from objectpage.mam_login_page import LoginPage
from objectfunction import login
import unittest
from framework.browser_engine import BrowserEngine


class Home(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserEngine(cls)
        cls.driver = cls.browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 个人中心页面测试实例
    def test_personel_manager(self):
        #调用登陆模块，输入用户名／密码，完成登陆操作
        self.loginpage = LoginPage(self.driver)
        self.driver.find_element_by_xpath("//*[@id='username']").send_keys("mam")
        self.driver.find_element_by_xpath("//*[@type='password']").send_keys("qwe123!@#2018")
        self.driver.find_element_by_xpath("//*/button[@type='submit']").click()
        self.loginpage.sleep(1)

        try:
            assert "首页" in self.loginpage.get_page_title()
        except Exception as e:
            print("Test Fail！", format(e))

        self.homepage = MAMHomePage(self.driver)
        # self.driver.find_element_by_xpath("//*[@id='mymam_link']").click()
        self.homepage.personal_click()
        self.homepage.sleep(1)
        try:
            assert "个人中心" in self.homepage.get_page_title()

        except Exception as e:
            print("Test Fail！",format(e))
        self.driver.find_element_by_xpath("//*[@id='mam_manager_link']").click()


        try:
            assert "管理中心" in self.homepage.get_page_title()

        except Exception as e:
            print("Test Fail！", format(e))



if __name__ == '__main__':
    unittest.main