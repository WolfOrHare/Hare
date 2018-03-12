from objectpage.mam_personal_page import PersonalPage
from selenium.webdriver.support.ui import Select
from framework.logger import Logger
logger = Logger(logger="Personal").getlog()
class Personal(object):
    def __init__(self,driver):
        self.driver = driver

    def CatalogAssignTask(self):
        personalpage = PersonalPage(self.driver)
        # 个人中心，编目分配点击事件
        try:
            personalpage.catalog_assign_click()

            # 清空并通过修改时间，下拉列表进行查询

            personalpage.time_in_clear()
            personalpage.time_end_clear()
            personalpage.time_in_type("1000-03-06")
            personalpage.time_end_type("2018-03-06")
            personalpage.search_tsk_click()

            # 设置当前页面任务显示条数
            personalpage.sleep(10)
            personalpage.set_pageRp()

            personalpage.tsk_name_type("test111")
            # 触发查询事件
            # 因为任务处理太快可能导致查询到的任务总条数不准确，所以睡2s
            personalpage.search_tsk_click()
            personalpage.sleep(2)

            # 获取总任务量
            personalpage.total_number_element()
            personalpage.sleep(3)
            # 这里获取了界面中查询到的内容，需要写个判断，确定是否进行诸如导入等操作
            personalpage.check_box_text_element()

            personalpage.check_box_click()
            personalpage.sleep(2)
            # personalpage.exportExcel_btn_click()
            # personalpage.sleep(2)

            # 单旋钮定位结果是空，有错误
            # for i in personalpage.exportExcel_radio_elements():
            #     print(personalpage.exportExcel_radio_elements())
            #     i.click()
            # personalpage.exportExcel_ls_btnok_click()
            # personalpage.sleep(2)
            personalpage.asign_btn_click()
            personalpage.sleep(2)
            personalpage.asign_cata_user_click()
            #=============纯模仿人为手工操作===============
            personalpage.sleep(2)
            personalpage.asign_cata_user_type('mam')

        # personalpage.asign_2cata_user_click()
        # personalpage.sleep(2)
        # personalpage.asign_2cata_user_type('mam')
        #
        # personalpage.asign_autor_user_click()
        # personalpage.sleep(2)
        # personalpage.asign_autor_user_type('mam')
        #
        # personalpage.asign_2autor_user_click()
        # personalpage.sleep(2)
        # personalpage.asign_2autor_user_type('mam')
        except:
            logger.error("catalog_assign_click fail")