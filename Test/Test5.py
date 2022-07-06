# coding=utf-8
'''
带参查询读者应该谨记sql 与 参数 分离
参数的末尾必须加上逗号
如果知道返回的数据就一条使用fetchone()方法，如果无特殊要求，否则建议使用fetchall()方法
'''
# -*- coding: utf-8 -*-
import psycopg2
# 获得连接
conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="localhost", port="5432")
# 获得游标对象，一个游标对象可以对数据库进行执行操作
cursor = conn.cursor()
# sql语句 建表
sql ="""SELECT * FROM student where id = %s;"""
params = (3,)
# 执行语句
cursor.execute(sql,params)
# 抓取
rows = cursor.fetchall()
print(rows)
# 事物提交
conn.commit()
# 关闭数据库连接
cursor.close()
conn.close()