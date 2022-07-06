# -*- coding: utf-8 -*-
import psycopg2
# 获得连接
conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="localhost", port="5432")
# 获得游标对象，一个游标对象可以对数据库进行执行操作
cursor = conn.cursor()
# sql语句 建表
sql ="""SELECT * FROM student;"""
# 执行语句
cursor.execute(sql)
# 抓取

# 使用fetchone()方法可以抓取一条数据, 返回的是元组；
# row = cursor.fetchone()
# print(row)

# 使用fetchmany([size=cursor.arraysize])方法可以抓取多条数据；
# rows = cursor.fetchmany(1)
# print(rows)

# 使用 fetchall() 方法会抓取所有数据；
rows = cursor.fetchall()
print (rows)

# 事物提交
conn.commit()
# 关闭数据库连接
cursor.close()
conn.close()