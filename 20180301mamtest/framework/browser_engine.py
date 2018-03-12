import os,time,unittest,configparser
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))
    dirver_path = dir + '/tools/chromedriver'

    def __init__(self,driver):
        self.driver = driver

    def open_browser(self,driver):
        config = configparser.ConfigParser()
        conf_file = os.path.dirname(os.path.abspath('.')) +'/config/config.ini'
        config.read(conf_file)

        browser = config.get("TypeBrowser","BrowserName")
        # logger.info("Setting config browser is %s" % browser)
        url = config.get("ServerUrl",'URL')
        # logger.info("Setting config URL is %s" % url)

        if browser == "Chrome":
            driver = webdriver.Chrome(executable_path=self.dirver_path)
            logger.info("Seccess Open Chrome! %s" % browser)
        elif browser =="IE":
            logger.info("Can not set browser %s" % browser)
        elif browser == "Firefox":
            logger.info("Can not set browser %s" % browser)

        driver.get(url)
        logger.info("Open %s Seccess!" % url)

        driver.maximize_window()
        #从新设置窗口，原因是界面中退出按钮没有在全屏后展示出来，导致元素被遮挡无法进行click
        driver.set_window_size(1920,1080)
        driver.implicitly_wait(8)
        logger.info("Implicitly wait 8 seconds！")

        return driver
