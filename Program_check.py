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














#设置函数
def choosetype():                   #获取表名
    global tablename
    tablename = choicetype.get()
    try:
        getmark(tablename,bankname)
    except:
        print("null")

def choosebank(event):              #获取支行名
    global bankname
    bankname = list_bank.get(list_bank.curselection())
    try:
        getmark(tablename,bankname)
    except:
        print("null")
    
def getmark(tablename,bankname):
    global markname,mark
    if tablename=="businesscheck":
        sql='''select business_mark as 总得分,cus_now as 私行客户数,cus_mark as 客户得分,
                       aum_now as 私行AUM,aum_mark as AUM得分,aum_now/allaum_now as 私行资产占比,
                       allaumratio_mark as 资产占比得分 from businesscheck where 2ndbank='{}' and business_date='2018-06-30';'''.format(bankname)
        markname=('总得分','私行客户数','客户得分','私行AUM','AUM得分','私行资产占比','资产占比得分')
    cursor.execute(sql)
    mark = cursor.fetchall()[0]
    result.set(mark)

def play():
    global markname,mark
    try:
        getmark(tablename,bankname)
    except:
        print("null")


#tkinter窗口设置
mainwin = tk.Tk()
mainwin.geometry("1080x720")
mainwin.title("评价查询系统")
choicetype = tk.StringVar()         #表类型选择变量
result = tk.StringVar()

#一、设置标题
labeltitle = tk.Label(mainwin, text="评价查询系统", fg="red", font=("微软雅黑",16))
labeltitle.pack(pady=20)


#二、设置主容器
mainframe = tk.Frame(mainwin)
mainframe.pack()
##设置支行标签(0,0)
labelbank = tk.Label(mainframe, fg='blue',text='请选择支行',font=("微软雅黑",14))
labelbank.grid(row=0,column=0,sticky=tk.S)
##--------------------------------------------------------------------------------------##

##设置支行子容器(1,0)
framebank = tk.Frame(mainframe)
framebank.grid(row=1,column=0,pady=25)

###设置支行列表
list_bank = tk.Listbox(framebank,font=("微软雅黑",14),height=17)
for bank in banklist:
    list_bank.insert(tk.END,bank[0])
list_bank.bind('<ButtonRelease-1>',choosebank)
list_bank.pack(side=tk.LEFT)

###设置支行滚动栏
roll_bank = tk.Scrollbar(framebank)
roll_bank.pack(side=tk.RIGHT,fill=tk.Y)
list_bank['yscrollcommand'] = roll_bank.set
roll_bank['command'] = list_bank.yview
##--------------------------------------------------------------------------------------##

##设置评价标签容器(0,1)
labeltype = tk.LabelFrame(mainframe,text='评价选项',font=("微软雅黑",10),padx=15)
labeltype.grid(row=0,column=1,sticky=tk.N,padx=30)

###设置评价类型选项
n=1
for t in tablenames:
    rbtemtype = tk.Radiobutton(labeltype, text=t.split(".")[-1], font=("微软雅黑",14), 
                               variable=choicetype, value=t.split(".")[0], command=choosetype)
    rbtemtype.grid(row=1, column=n)
    if (n==1):
        rbtemtype.select()
        tablename = t.split(".")[0]
    n+=1
##--------------------------------------------------------------------------------------##
    
##设置展示板标签容器(1,1)
labeltext = tk.LabelFrame(mainframe,text='评价内容',font=("微软雅黑",10),width=730,height=420)
labeltext.grid(row=1,column=1,sticky=tk.NW,padx=30,pady=30)
labeltext.grid_propagate(0)
###设置得分项和具体得分

labelre=tk.Label(labeltext,textvariable=result,fg="red",font=("微软雅黑",20))
labelre.grid(row=0, column=0, padx=50, pady=20)

#for y1 in range(2):
#    for x1 in range(6):
#        try:
#            m=6*y1+x1
#            if m==0:
#                labelre=tk.Label(labeltext,text="{}: %.3f".format(markname[m])%mark[m],fg="red",font=("微软雅黑",20))
#                labelre.grid(row=x1, column=y1, padx=50, pady=20)
#            elif m<len(mark):
#                if y1==0:
#                    labelre=tk.Label(labeltext,text="{}: %.3f".format(markname[m])%mark[m],font=("微软雅黑",14))
#                    labelre.grid(row=x1, column=y1, padx=50, pady=15, sticky=tk.W)
#                else:
#                    labelre=tk.Label(labeltext,text="{}: %.3f".format(markname[m])%mark[m],font=("微软雅黑",14))
#                    labelre.grid(row=x1+1, column=y1, padx=50, pady=15, sticky=tk.W)
#        except:
#            print('no')

button1 = tk.Button(mainwin, text="查询", width=8, command=play)
button1.pack()    

mainwin.mainloop()














