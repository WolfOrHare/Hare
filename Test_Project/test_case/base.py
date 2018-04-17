# -*- coding:utf-8 -*-
import logging
from unittest import TestCase
from selenium import webdriver
import settings

logger = logging.getLogger(__name__)


class BaseSeleniumTestCase(TestCase):
    # 获取浏览器driver驱动
    def get_web_driver(self):
        driver = webdriver.Firefox(executable_path=settings.GECKODRIVER_PATH)
            # if settings.ENV == "test" else webdriver.PhantomJS()
        driver.maximize_window()
        return driver

    def setUp(self):
        self.selenium = self.get_web_driver()

    def tearDown(self):
        self.selenium.quit()
