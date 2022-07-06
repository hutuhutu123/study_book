# -*- coding: utf-8 -*-
'''
处理 sql 的异常非常重要，知识追寻者这边使用psycopg2的 Error 进行异常捕获，能捕获到sql执行时期的所有异常；
下面代码中表test是库中不存的表，执行sql后会报异常，经过异常捕获后非常美观，不影响程序运行；
'''
import psycopg2
# 获得连接
conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="localhost", port="5432")
# 获得游标对象，一个游标对象可以对数据库进行执行操作
cursor = conn.cursor()
# sql语句 建表
sql ="""select * from test"""
params = (3,)
try:
    # 执行语句
    cursor.execute(sql,params)
except psycopg2.Error as e:
    print(e)
# 事物提交
conn.commit()
# 关闭数据库连接
cursor.close()
conn.close()