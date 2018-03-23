# coding=utf-8
'''
Created on 2016-7-26
@author: Jennifer
Project:整合自动发邮件功能，执行测试用例生成最新测试报告，取最新的测试报告，发送最新测试报告
问题，邮件始终不能显示html：将电脑时间改为北京时间即可
'''
import unittest
from tools.HTMLTestRunner import HTMLTestRunner
from framework.email_engine import ReportEmail
import time
import os

# 定义：取最新测试报告
def new_file(test_dir):
    # 列举test_dir目录下的所有文件，结果以列表形式返回。
    lists = os.listdir(test_dir)
    # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    # 最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn: os.path.getmtime(test_dir + fn))
    # 获取最新文件的绝对路径
    file_path = os.path.join(test_dir, lists[-1])
    return file_path


if __name__ == '__main__':
    print('=====AutoTest Start======')
    # 1.执行测试用例，生成最新的测试用例
    # 指定测试用例为当前文件夹下的test_case目录
    # 如果用/可以不用r
    #    test_dir='./test_case'
    # Windows的cmd执行：python "D:\system files\workspace\selenium\test_project\runtest_htmltestrunner_autosendemail.py"
    # 不用绝对路径会报：ImportError: Start directory is not importable: './test_case'
    # test_dir = 'D:\\system files\\workspace\\selenium\\test_project\\test_case'

    test_dir = os.path.dirname(os.path.abspath('.'))+'/testsuites/'
    # 测试报告的路径
    # test_report_dir = 'D:\\pythontest\\testresult'
    test_report_dir = os.path.dirname(os.path.abspath('.'))+'/html_report/'

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    now = time.strftime('%Y-%m-%d_%H_%M_%S_')
    filename = test_report_dir + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    # 需屏蔽fp中的中文文字说明。否则在windows下执行会报：UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 553: ordinal not in range(128)
    runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
    runner.run(discover)
    #
    fp.close()

    email_engine = ReportEmail()
    # 取最新测试报告
    new_report = new_file(test_report_dir)
    # 调试用的
    #    print new_report

    email_user = ''
    email_password = ''
    sendTo = ['yangwang@dayang-itech.com', 'XXX@126.com', 'XXX@doov.com.cn']
    # 发送邮件，发送最新测试报告html
    email_engine.send_email(new_report,email_user,email_password,sendTo)
    print('====AutoTest Over======')