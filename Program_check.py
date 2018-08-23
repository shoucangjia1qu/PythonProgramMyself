# -*- coding: utf-8 -*-
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














#布局主界面界面
def choosetype():
    global tablename
    tablename = choicetype.get()




#tkinter总布局
mainwin = tk.Tk()
mainwin.geometry("1080x720")
mainwin.title("评价查询系统")

choicetype = tk.StringVar()         #表类型选择变量

#设置标题
labeltitle = tk.Label(mainwin, text="评价查询系统\n", fg="red", font=("微软雅黑",16))
labeltitle.pack()

#设置主容器
mainframe = tk.Frame(mainwin)
mainframe.pack()

##设置支行标签(0,0)
labelbank = tk.Label(mainframe, fg='blue',text='请选择支行',font=("微软雅黑",14))
labelbank.grid(row=0,column=0,sticky=tk.S)

##设置支行子容器(1,0)
framebank = tk.Frame(mainframe)
framebank.grid(row=1,column=0,pady=25)
###设置支行列表
list_bank = tk.Listbox(framebank,font=("微软雅黑",14),height=17)
for bank in banklist:
    list_bank.insert(tk.END,bank[0])
list_bank.pack(side=tk.LEFT)
###设置支行滚动栏
roll_bank = tk.Scrollbar(framebank)
roll_bank.pack(side=tk.RIGHT,fill=tk.Y)
list_bank['yscrollcommand'] = roll_bank.set
roll_bank['command'] = list_bank.yview

##设置评价标签容器(0,1)
labeltype = tk.LabelFrame(mainframe, fg='blue',text='评价选项',font=("微软雅黑",10))
labeltype.grid(row=0,column=1,sticky=tk.N,padx=30)
###设置评价类型选项
n=1
for t in tablenames:
    rbtemtype = tk.Radiobutton(labeltype, text=t.split(".")[-1], font=("微软雅黑",14), 
                               variable=choicetype, value=t.split(".")[0], command=choosetype)
    rbtemtype.grid(row=1, column=n)
    if (n==1):
        rbtemtype.select()
    n+=1

##设置展示板(1,1)


    
    
    

mainwin.mainloop()














