# -*- coding:utf-8 -*-
import pymysql.cursors,settings

# try connection.commit()提交事务
# except connection.rollback()回滚事务

def execute(sql, params=None, is_fetchone=True):
    # Connect to the database
    connection = pymysql.connect(host=settings.DB_HOST,
                                 port=settings.DB_PORT,
                                 user=settings.DB_USER,
                                 password=settings.DB_PASSWORD,
                                 db=settings.DB_NAME,
                                 autocommit=True,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            if is_fetchone:
                return cursor.fetchone()
            else:
                return cursor.fetchall()
        connection.commit()
    except:
        connection.rollback()

    finally:
        connection.close()