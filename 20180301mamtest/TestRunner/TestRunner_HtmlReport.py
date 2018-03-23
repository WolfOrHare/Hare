#由于开发环境问题，我修改了HTMLTestRunner并与自己的工程打包在一起
from tools import HTMLTestRunner
import unittest,os,time

dir = os.path.dirname(os.path.abspath('.'))+"/report_htm/"
now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time()))

html_name = dir + now + 'report.html'

fp = open(html_name,'wb')
#装载测试用例
suite = unittest.TestLoader().discover("testsuites")
if __name__ == '__main__':
    #生成测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='test',description="qwe")
    runner.run(suite)
    #关闭被打开的html文件
    fp.close()