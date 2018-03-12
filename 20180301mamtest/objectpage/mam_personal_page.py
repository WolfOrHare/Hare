from framework.base_page import BasePage
from selenium.webdriver.support.ui import Select
import selenium


class PersonalPage(BasePage):
    # 编目分配页面，输入检索条件进行检索，其中包括字符串，时间，下拉菜单的处理
    # 编目分配页签
    tab_catalog_assign = "id=>AssignTaskListView"
    # 任务名称
    tsk_assign_name = "xpath=>//*[@id='AssignTaskListView']/div/div/div/input[@id='name']"
    # 查询按钮
    search_tsk = "xpath=>//*[@id='queryBtn']"
    # 时间选择控件
    time_in = "id=>createdbegin"
    time_end = "id=>createdend"
    # 下拉菜单：来源 ['请选择','导入','自动创建','上载','索贝导入','DYMAM','索贝缩编']
    source = "id=>source-input"
    # 下拉菜单：改稿标识
    restartFlag = "id=>restartFlag-input"

    # 下拉菜单：单页任务条数 [5,10,15,20,30,50,100,200]
    pageRp = "id=>pageRp"
    # 总条数
    total_number = "id=>findtext"

    # 选中任务
    check_box = "xpath=>//*/table[@id='CatalogTask']/tbody/tr/td[1]/input[@type='checkbox']"
    check_box_text = "xpath=>//*/table[@id='CatalogTask']/tbody/tr[1]/td[3]/a/span"
    # 导出任务列表菜单
    exportExcel_btn = "id=>exportExcel"
    exportExcel_ls_radio = "xpath=>//*/div[@class='ui-dialog ui-widget ui-widget-content ui-corner-all ui-draggable ui-resizable']/form[@class='form-vertical ui-dialog-content ui-widget-content']/label[@class='radio']/input[@type='radio']"
    exportExcel_ls_btnok = "xpath=>//*/div[@class='ui-dialog ui-widget ui-widget-content ui-corner-all ui-draggable ui-resizable']/div[10]/div/button[1]"
    exportExcel_ls_btnno = "xpath=>//*/div[@class='ui-dialog ui-widget ui-widget-content ui-corner-all ui-draggable ui-resizable']/div[10]/div/button[2]"

    # 刷新
    refresh_btn = "id=>refresh"

    # 分配提示框
    asign_btn = "id=>asign"

    # 分配到角色
    asign_cata_actor = "xpath=>//*[@id='assign-dialog']/table/tbody/tr[2]/td[2]/input[@type='radio']"
    asign_autor_actor = "xpath=>//*[@id='assign-dialog']/table/tbody/tr[3]/td[2]/input[@type='radio']"
    asign_2cta_actor = "xpath=>//*[@id='assign-dialog']/table/tbody/tr[4]/td[2]/input[@type='radio']"
    asign_2autor_actor = "xpath=>//*[@id='assign-dialog']/table/tbody/tr[5]/td[2]/input[@type='radio']"
    # 分配到人
    asign_cata_user = "xpath=>//*[@id='assign-dialog']/table/tbody/tr[2]/td[3]/input[@type='radio']"
    asign_autor_user = "xpath=>//*[@id='assign-dialog']/table/tbody/tr[3]/td[3]/input[@type='radio']"
    asign_2cata_user = "xpath=>//*[@id='assign-dialog']/table/tbody/tr[4]/td[3]/input[@type='radio']"
    asign_2autor_user = "xpath=>//*[@id='assign-dialog']/table/tbody/tr[5]/td[3]/input[@type='radio']"
    # 分配目标
    assign_cata_user_id = "xpath=>//*/div[@id='s2id_autogen1']"
    asign_cata_user_tage = "xpath=>//*[@id='s2id_autogen2_search']"
    asign_cata_user_tage_text = "xpath=>//*/div[@id='select2-drop']/ul[@id='select2-results-2']/li/div[@id='select2-result-label-38']"

    asign_autor_user_id = "xpath=>//*/div[@id='s2id_autogen62']"
    asign_autor_user_tage = "xpath=>//*[@id='s2id_autogen62_search']"

    asign_2cata_user_id = "id=>s2id_autogen94"
    asign_2cata_user_tage = "id=>s2id_autogen94_search"

    asign_2autor_user_id = "id=>s2id_autogen125"
    asign_2autor_user_tage = "id=>s2id_autogen125_search"

    # 分配确认取消按钮
    asign_btn_ok = "id=>//*[@id='assign-dialog']/div/button[1]"
    asign_btn_no = "id=>//*[@id='assign-dialog']/div/button[2]"

    #
    totalDuration_btn = "id=>totalDuration"
    totalDuration_title = "id=>ui-dialog-title-4"
    totalDuration_content = "name=>ui-dialog-content ui-widget-content"
    #
    hisTask_btn = "id=>hisTask"

    # 翻页，向后，如果大余2可以点击向后翻页

    # 翻页，向前，如果大余1，可以点击向前翻页

    # click assign
    def catalog_assign_click(self):
        self.click(self.tab_catalog_assign)
        self.sleep(3)

    def tsk_name_type(self, text):
        self.type(self.tsk_assign_name,text)

    # clear time
    def time_in_clear(self):
        self.clear(self.time_in)

    def time_end_clear(self):
        self.clear(self.time_end)

    # set type
    def time_in_type(self, text):
        self.type(self.time_in, text)

    def time_end_type(self, text):
        self.type(self.time_end, text)

    def set_source(self):
        Select(self.find_element(self.source)).select_by_index(1)

    # set page number
    def set_pageRp(self):
        Select(self.find_element(self.pageRp)).select_by_index(0)
        self.sleep(2)
    # set tsk name search
    # def catalog_assign_search(self, text):
    #     self.type(self.tsk_assign_name, text)

    # set total number,
    def total_number_element(self):
        self.find_element(self.total_number).text

    def check_box_click(self):
        self.click(self.check_box)

    def check_box_text_element(self):
        self.find_element(self.check_box_text).text

    def exportExcel_btn_click(self):
        self.click(self.exportExcel_btn)

    def exportExcel_radio_elements(self):
        self.find_elements(self.exportExcel_ls_radio)

    def exportExcel_ls_btnok_click(self):
        self.click(self.exportExcel_ls_btnok)

    def exportExcel_ls_btnno_click(self):
        self.click(self.exportExcel_ls_btnno)

    def refresh_click(self):
        self.click(self.refresh_btn)

    def asign_btn_click(self):
        self.click(self.asign_btn)

    def asign_cata_user_click(self):
        self.click(self.asign_cata_user)

    def asign_autor_user_click(self):
        self.click(self.asign_autor_user)

    def asign_2cata_user_click(self):

        self.click(self.asign_2cata_user)

    def asign_2autor_user_click(self):
        self.click(self.asign_2autor_user)

    def asign_cata_user_type(self,text):
        self.click(self.assign_cata_user_id)
        self.sleep(2)
        self.type(self.asign_cata_user_tage,text)

        self.click(self.asign_cata_user_tage_text)


    def asign_autor_user_type(self,text):
        self.click(self.asign_autor_user_id)
        self.sleep(2)
        self.type(self.asign_autor_user_tage,text)

    def asign_2cata_user_type(self,text):
        self.click(self.asign_2cata_user_tage)
        self.sleep(2)
        self.type(self.asign_2cata_user_tage,text)

    def asign_2autor_user_type(self,text):
        self.click(self.asign_2autor_user_tage)
        self.sleep(2)
        self.type(self.asign_2autor_user_tage,text)

    def asign_btn_ok_click(self):
        self.click(self.asign_btn_ok)

    def asign_btn_no_click(self):
        self.click(self.asign_btn_no)

    def totalDuration_btn_click(self):
        self.click(self.totalDuration_btn)

    def totalDuration_title_element(self):
        self.find_element(self.totalDuration_title).text

    def totalDuration_content_element(self):
        self.find_element(self.totalDuration_content).text

    # set search
    def search_tsk_click(self):
        self.click(self.search_tsk)

    #
    def hisTask_btn_click(self):
        self.click(self.hisTask_btn)
