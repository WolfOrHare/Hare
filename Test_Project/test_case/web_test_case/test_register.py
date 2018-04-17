# -*- coding:utf-8 -*-
from page.register_page import RegisterPage
from page.index_page import IndexPage
from test_case.base import BaseSeleniumTestCase
from utilities import operation
import settings, time, unittest


class TestRegister(BaseSeleniumTestCase):
    # username = '一个音乐人WC'
    mobile = '13100102034'
    password = '123abc'
    nickname = '一个音乐人WC'

    def test_register_success(self):
        # 校验注册流程及注册成功后自动跳转到首页
        after_register_url = RegisterPage(self.selenium)\
            .register(self.mobile, self.password,self.nickname)\
            .get_current_page_url()
        time.sleep(1.5)


        # 断言获取的地址是否与配置一致
        self.assertEqual(after_register_url, settings.WEB_TEST_BASE_URL + '/index')

        # 校验注册成功后页面title
        after_register_title = RegisterPage(self.selenium).get_page_title()
        self.assertEqual(after_register_title, u'Test-Title')

        # 校验注册成功后首页用户昵称是否与填写的一致
        nickname = IndexPage(self.selenium).get_user_name()
        self.assertEqual(nickname, u'autotest...')

    def tearDown(self):
        super(TestRegister, self).tearDown()
        operation.delete_user(self.mobile)
