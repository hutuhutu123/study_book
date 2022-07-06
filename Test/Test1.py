# -*- coding: utf-8 -*-
import psycopg2
# 获得连接
conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="localhost", port="5432")
# 获得游标对象
cursor = conn.cursor()
# sql语句
sql = "SELECT VERSION()"
# 执行语句
cursor.execute(sql)
# 获取单条数据.
data = cursor.fetchone()
# 打印
print("database version : %s " % data)
# 事物提交
conn.commit()
# 关闭数据库连接
conn.close()