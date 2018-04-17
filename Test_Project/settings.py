'''
nose
redis
selenium
pymysql
requests
'''
# -*- coding:utf-8 -*-
# env config
ENV = 'test'

# test url test config
WEB_TEST_BASE_URL = "https://passport.baidu.com/v2/?reg&tt=1523881491702&overseas=undefined&gid=6CFCF86-E7E7-4BE9-9A6F-68A2723CD84C&tpl=mn&u=https%3A%2F%2Fwww.baidu.com%2Findex.php%3Ftn%3Dmonline_3_dg"

# global waiting time config
WAIT_TIME = 10

# redis config
REDIS_HOST = ''
REDIS_PORT = ''



# mysql config

DB_HOST = '10.0.104.123'
DB_PORT = 3306
DB_USER = 'mysql'
DB_PASSWORD = 'mysql'
DB_NAME = 'fuqiang_bak'

# local debugging config
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
SNAPSHOT_DIRECTORY = os.path.join(BASE_DIR, 'logs')
print(SNAPSHOT_DIRECTORY)

SETTING_LOCAL_DIR = os.path.join(BASE_DIR, "settings_local.py")
print(SETTING_LOCAL_DIR)

# drive config

GECKODRIVER_PATH = BASE_DIR + '/drivers/'+'geckodriver'

if os.path.exists(SETTING_LOCAL_DIR):
    # execfile('SETTING_LOCAL_DIR')
    # exec(compile(open(SETTING_LOCAL_DIR).read()),SETTING_LOCAL_DIR,'exec')
    print("**注释**：Python3中execfile需要用exec循环获取文件中的内容")