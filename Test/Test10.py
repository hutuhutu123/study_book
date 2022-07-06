# coding=utf-8
'''
使用 mogrify(operation[, parameters])
能够显示执行语句的参数绑定结果，返回的是字符串形式；
'''
import psycopg2
# 获得连接
conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="localhost", port="5432")
# 获得游标对象，一个游标对象可以对数据库进行执行操作
cursor = conn.cursor()
# sql语句 建表
sql ="""INSERT INTO student (num, name) VALUES (%s, %s)"""
params = (102, '知识追寻者')
# 执行语句
result = cursor.mogrify(sql,params)
print(result.decode('UTF-8'))
cursor.execute(sql,params)
# 事物提交
conn.commit()
# 关闭数据库连接
conn.close()