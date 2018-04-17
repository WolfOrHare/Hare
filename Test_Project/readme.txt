##2018-04-13##
##### Python3.5 ##### 说明 ###########
1、把下面包和版本信息保存到test.txt中
可以运行 pip install -r test.txt,自动安装所需要的包
# 包==版本号#

nose==1.3.7
redis==2.10.6
selenium==3.11.0
PyMySQL==0.8.0
requests==2.18.4

2、Python3.5源码中需要修改：无法直接import urlparse
    # python3.4之后中urlparse并入urllib模块
    python3.5/site-packages/db/__init__.py
    python3.5/site-packages/db/drivers.py

3、Python3中execfile需要用exec循环获取文件中的内容
# execfile('SETTING_LOCAL_DIR')
# exec(compile(open(SETTING_LOCAL_DIR).read()),SETTING_LOCAL_DIR,'exec')

4、百度注册获取验证码前，有安全验证的问题，需要解决，看图像识别看是否有解。（待修复）
5、