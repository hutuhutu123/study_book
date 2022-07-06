# -*- coding: utf-8 -*-
import psycopg2

# 获得连接
conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="localhost", port="5432")
# 获得游标对象，一个游标对象可以对数据库进行执行操作
cursor = conn.cursor()
# sql语句 建表
sql = """update student set name = %s where id = %s  """
params = ('知识追寻者', 3,)
# 执行语句
cursor.execute(sql, params)
# 事物提交
conn.commit()
# 关闭数据库连接
cursor.close()
conn.close()
