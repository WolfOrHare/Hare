# -*- coding:utf-8 -*-
'''
    闲！！试试数据库链接是否好用
'''
from utilities import conn_db
def add_date():

    if conn_db.execute("""select * from send_sms_code""") is not None:
        print("添加有记录调用更新")
        update_date()

    else:
        sql = """INSERT INTO send_sms_code (id,mobile,username,password) VALUES ('123456789','13752096930',123,123)"""
        conn_db.execute(sql)
        print('insert is ok---> %s' % conn_db.execute("""select * from send_sms_code"""))
        print("添加有记录调用删除")
        delete_date()



def update_date():
    sql = """update send_sms_code set id = 987654321"""
    if conn_db.execute("""select * from send_sms_code""") is not None:
        update = conn_db.execute(sql)
        print('update is ok---> %s ' % update)
        print("更新有记录调用删除")
        delete_date()
    else:
        print("更新无记录调用添加")
        add_date()

def delete_date():
    sql = """select * from send_sms_code where id = 987654321"""

    if conn_db.execute(sql) is not  None:
        conn_db.execute("""delete from  send_sms_code WHERE id = 987654321""")
        print('delete is ok---> %s' % conn_db.execute("""select * from send_sms_code"""))
    else:
        print("删除无记录调用更新")
        update_date()


delete_date()

