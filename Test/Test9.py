# coding=utf-8
'''
使用cursor.query 可以查看执行的sql语句，方便排查；
'''
# -*- coding: utf-8 -*-
import psycopg2
# 获得连接
conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="localhost", port="5432")
# 获得游标对象，一个游标对象可以对数据库进行执行操作
cursor = conn.cursor()
# sql语句 建表
sql ="""select * from student"""

# try:
#     # 执行语句
#     cursor.execute(sql,)
#     que = cursor.query
#     print(que)
# except psycopg2.Error as e:
#     print(e)

# 执行语句
# 使用cursor.rowcount 可以获得表中所有行总数；
# cursor.execute(sql)
# count = cursor.rowcount
# print(count)

# 执行语句
# 使用cursor.rownumber 可以显示当前查询sql获得数据的行号，每抓取一次光标的索引就会加1；
cursor.execute(sql)
row_1 = cursor.fetchone()
print(cursor.rownumber)
row_2 = cursor.fetchone()
print(cursor.rownumber)

# 事物提交
conn.commit()
# 关闭数据库连接
cursor.close()
conn.close()