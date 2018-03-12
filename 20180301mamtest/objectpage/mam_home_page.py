from framework.base_page import BasePage

class MAMHomePage(BasePage):

    '''
        1、首页中，资源分类id：condition-tree-link，下拉列表如何获取
    '''
    personal_center="xpath=>//*[@id='mymam_link']"
    manager_center="xpath=>//*[@id='mam_manager_link']"
    resource_manager = "xpath=>//*[@id='resource_manager_link']"
    advanced_search = "xpath=>*[@id='adv_search']"

    def personal_click(self):
        self.click(self.personal_center)
        self.sleep(2)

    def manager_click(self):
        self.click(self.manager_center)
        self.sleep(2)

    def resource_manager_click(self):
        self.click(self.resource_manager)
        self.sleep(2)

    def advanced_search_click(self):
        self.click(self.advanced_search)
        self.sleep(2)
