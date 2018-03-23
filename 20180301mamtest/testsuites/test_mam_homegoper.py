import unittest
from objectfunction.login import LoginMAM
from objectpage.mam_home_page import MAMHomePage
from objectfunction.personal import Personal


class hompage1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login = LoginMAM(cls)
        cls.login.initSetup()
        cls.login.loginValid()
        cls.driver = cls.login.driver
    @classmethod
    def tearDownClass(cls):
       cls.driver.quit()



    def test_hp1(self):
        hompage = MAMHomePage(self.driver)
        hompage.personal_click()
    def test_per1(self):
        personal = Personal(self.driver)
        personal.CatalogAssignTask()



if __name__ == "__main__":
    unittest.main