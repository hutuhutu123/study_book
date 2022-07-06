# -*- coding: utf-8 -*-
import psycopg2
# 获得连接
conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="localhost", port="5432")
# 获得游标对象，一个游标对象可以对数据库进行执行操作
cursor = conn.cursor()
# sql语句 建表
sql = """CREATE TABLE student (
id serial4 PRIMARY KEY, 
num int4,
name varchar(25));"""
# 执行语句
cursor.execute(sql)
print("student table created successfully")
# 事物提交
conn.commit()
# 关闭数据库连接
conn.close()