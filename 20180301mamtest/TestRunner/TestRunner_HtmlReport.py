from tools import HTMLTestRunner
import unittest,os,time

dir = os.path.dirname(os.path.abspath('.'))+"/report_htm/"
now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time()))

html_name = dir + now + 'report.html'

fp = open(html_name,'wb')

suite = unittest.TestLoader().discover("testsuites")
if __name__ == '__main__':
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='test',description="qwe")
    runner.run(suite)
    fp.close()