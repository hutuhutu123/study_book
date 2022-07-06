# -*- coding: utf-8 -*-
import psycopg2
# 获得连接
conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="localhost", port="5432")
# 获得游标对象，一个游标对象可以对数据库进行执行操作
cursor = conn.cursor()

# sql语句 建表 第一种防止sql注入的插入数据方式（具有占位符的预编译sql），重要程度不言而喻；美中不足是字符串类型必须带上单引号；
# sql ="INSERT INTO student (num, name) \
#                     VALUES (%s, '%s')" % \
#                     (100, 'zszxz')
# cursor.execute(sql)

# sql语句 第二种插入数据 下面参数与sql语句分离插入的姿势更简便，也是防止sql注入问题；强烈推荐；
# sql ="""INSERT INTO student (num, name) VALUES (%s, %s)"""
# params = (101, 'zszxz')
# 执行语句
# cursor.execute(sql,params)

# sql语句 建表 第三种支持字典映射关系插入，使用字典方式的插入数据是根据字典的key进行匹配占位符，强烈推荐
sql ="""INSERT INTO student (num, name) VALUES (%(num)s, %(name)s)"""
params = {'num':102, 'name':'zszxz'}
# 执行语句
cursor.execute(sql,params)

print("successfully")
# 事物提交
conn.commit()
# 关闭数据库连接
conn.close()