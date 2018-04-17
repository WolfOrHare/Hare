# -*- coding:utf-8 -*-
from page.base_page import BasePage
from utilities import operation


class RegisterPage(BasePage):
    #
    url = '/register'

    # def input_new_username(self,username):
    #     # 输入新用户名
    #     element = self.find_element_by_id('TANGRAM__PSP_3__userName')
    #     element.clear()
    #     element.send_keys(username)
    #     return self

    def input_new_mobile(self,mobile):
        # 输入新注册手机号
        element = self.find_element_by_id('TANGRAM__PSP_3__phone')
        element.clear()
        element.send_keys(mobile)
        return self

    def click_send_sms_captcha_bt(self):
        # 点击获取短信验证码
        if self.element_to_be_click_able_by_id('TANGRAM__PSP_3__verifyCode'):
            self.find_element_by_id('TANGRAM__PSP_3__verifyCodeSend').click()
            return self

    def judgement_confirm_Verify_CodeImg(self):
        # 获取短信验证码前，安全验证，验证码识别还没玩明白，先返回个空，做样子
        #
        # 调用图片识别api
        # for 获取验证码图片
        # # if 验证码清晰
        #       self.element_to_be_click_able_by_id('TANGRAM__PSP_3__confirmVerifyCodeImg')
        #           break
        # #else：
        #   self.element_to_be_click_able_by_id('TANGRAM__PSP_3__confirmVerifyCodeChange')
        return self

    def judgement_confirm_Verify_Code(self,code):
        element = self.find_element_by_id('TANGRAM__PSP_3__confirmVerifyCode')
        element.clear()
        element.send_keys(code)

        return self

    def judgement_sms_captcha_frame(self):
        # 此处涉及到css如何得到的问题，F12控制台左侧小鼠标选中对应的元素，规则中所显示的内容即为对应的css名称
        # 如下'.tang-pass-reg'，获取所有tang-pass-reg元素样式
        # 获取短信验证码
        self.visibility_of_element_by_css('.tang-pass-reg')
        return self

    def click_send_sms_captcha_affirm(self):
        # 点击获取短信验证码弹框上的确定按钮
        self.find_element_by_css('.tang-pass-pop-confirmWidget').click()
        return self

    def input_sms_captcha(self,mobile):
        # 输入短信验证码，获取数据库中生成的验证码
        # 没数据库，没图片识别的逻辑的情况下，百度的注册测试，只能到这里了

        sms_captcha = operation.get_sms_captcha(mobile)
        # 获取数据库中对应手机号所产生的最新验证码

        element = self.find_element_by_id('TANGRAM__PSP_3__verifyCode')
        element.clear()
        element.send_keys(sms_captcha)
        # 输入验证码

        return self

    def input_new_password(self,password):
        # 输入注册时密码
        element = self.find_element_by_id('r_pwd')
        element.clear()
        element.send_keys(password)
        return self

    def click_submit_register(self):
        # 点击注册按钮
        if self.element_to_be_click_able_by_id('TANGRAM__PSP_3__submit'):
            self.find_element_by_id('TANGRAM__PSP_3__submit').click()
            return self

    def judgement_input_nickname_frame(self):
        # 校验弹出输入用户昵称框
        self.visibility_of_element_by_css('.c-name')
        return self

    def input_nickname(self,nickname):
        # 输入用户昵称
        element = self.find_element_by_id('TANGRAM__PSP_3__userName')
        element.clear()
        element.send_keys(nickname)
        return self

    def click_nickname_bt(self):
        # 点击输入昵称框确定按钮
        if self.element_to_be_click_able_by_css('.c-n-btn'):
            self.find_element_by_css('.c-n-btn').click()
            return self

    def register(self,mobile,password,nickname):
    # 注册流程

        # 输入手机号
        self.input_new_mobile(mobile).click_send_sms_captcha_bt()
        # 如果安全验证成功做进入，获取短信验证码填写用户昵称逻辑
        if self.judgement_sms_captcha_frame():
            # 获取短信验证码


            self.judgement_confirm_Verify_CodeImg()
            # code = self.judgement_confirm_Verify_CodeImg()
            # # 针对百度注册，安全验证未实现，需要图片识别逻辑,需要返回一个code作为输入条件
            # #
            # self.judgement_confirm_Verify_Code(code)

            self.click_send_sms_captcha_affirm()
            # 安全验证输入成功后，点击确认

            self.input_nickname(nickname)
            # 输入用户名

            self.input_sms_captcha(mobile)
            self.input_new_password(password).click_submit_register()

            # if self.judgement_input_nickname_frame():
            # # 用户名可用筛查逻辑
            #     self.input_nickname(nickname).click_nickname_bt()
        return self