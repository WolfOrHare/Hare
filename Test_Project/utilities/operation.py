# -*- coding:utf-8 -*-
from utilities import conn_db

def get_sms_captcha(mobile):
    # 获取短信验证码
    sms_captcha = conn_db.execute('select code from send_sms_code where mobile=%s order by id desc',params=(mobile))
    return sms_captcha['code']

def delete_user(mobile):
    # 删除用户
    conn_db.execute('delete from user where mobile=%s',params=(mobile))