import os,time
from framework.logger import Logger
from selenium.common.exceptions import NoSuchElementException

logger = Logger("BasePage").getlog()
class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()

    def logout_element(self):
        logout=self.driver.find_element_by_xpath("//*[@href][@onclick='CommonHeadTop.logout()']")
        # self.driver.execute_script('$(arguments[0]).onClick()',logout)
        self.sleep(1)
        logout.click()

    def back(self):
        self.driver.back()
        logger.info("Browser click back!")

    def forward(self):
        self.driver.forward()
        logger.info("Browser click forward!")

    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser!")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        rq = time.strftime("%Y%n%d%H%M%S",time.localtime(time.time()))
        screen_name = file_path+rq+'.png'

        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Screenshot of success!")
        except NameError as e:
            logger.error("Failed to take screenshot!",format(e))
            self.get_windows_img()

            # 定位元素方法

    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
    submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    def find_elements(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_elements_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                elements = self.driver.find_elements_by_id(selector_value)
                logger.info("Had find the elements \' %s \' successful "
                            "by %s via value: %s " % (elements.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            elements = self.driver.find_elements_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            elements = self.driver.find_elements_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            elements = self.driver.find_elements_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            elements = self.driver.find_elements_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            elements = self.driver.find_elements_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                elements = self.driver.find_elements_by_xpath(selector_value)
                # logger.info("Had find the elements \' %s \' successful "
                #             "by %s via value: %s " % (elements.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            elements = self.driver.find_elements_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return elements
        # 输入

    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

            # 清除文本框

    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

            # 点击元素

    def click(self, selector):

        el = self.find_element(selector)
        try:
            el.click()

            # logger.info("The element  %s  was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

            # 或者网页标题

    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title


    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)