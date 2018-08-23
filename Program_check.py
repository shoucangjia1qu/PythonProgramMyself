
"""
Created on Thu Aug 23 10:01:50 2018

@author: ecupl
"""

import tkinter as tk
import pymysql

#连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='********',
    db='bank1',
    charset='utf8'
)
cursor = connect.cursor()

#设置变量
tablenames=['businesscheck.私行业务发展','vbusinesscheck.至尊业务发展','relationshipcheck.客户维护能力',
            'investcheck.投资理财能力','allmark.整体能力']
cursor.execute("select distinct 2ndbank from allmark;")
banklist = cursor.fetchall()

#设置登录系统



























