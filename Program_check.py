# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:01:50 2018

@author: ecupl
"""

import tkinter as tk
import pandas as pd
import numpy as np
import pymysql
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg

#连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root1234',
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














#设置动作函数
def choosetype():                   #获取表名
    global tablename
    tablename = choicetype.get()
    try:
        resultframe.destroy()
        getmark(tablename,bankname)
        textmake(markname,mark)
    except:
        print("null")

def choosebank(event):              #获取支行名
    global bankname
    resultframe.destroy()
    bankname = list_bank.get(list_bank.curselection())
    getmark(tablename,bankname)
    textmake(markname,mark)
    
def play():
    global markname,mark
    try:
        resultframe.destroy()
        getmark(tablename,bankname)
        textmake(markname,mark)
    except:
        print("null")


def getmark(tablename,bankname):
    global markname,mark,pretablename,df
    if tablename!="allmark":
        if pretablename!=tablename:
            if tablename=="businesscheck":
                sql='''select business_mark as 总得分, 2ndbank as 支行,cus_now as 私行客户数,cus_mark as 客户得分,
                               aum_now as 私行AUM,aum_mark as AUM得分,aum_now/allaum_now as 私行资产占比,
                               allaumratio_mark as 资产占比得分 from {} where business_date='2018-06-30';'''.format(tablename)
            elif tablename=="vbusinesscheck":
                sql='''select vbusiness_mark as 总得分, 2ndbank as 支行,vcus_now as 至尊客户数,vcus_mark as 客户得分,
                               vaum_now as 至尊AUM,vaum_mark as AUM得分,vmeet as 至尊约见率,
                               vmeet_mark as 约见得分 from {} where vbusiness_date='2018-06-30';'''.format(tablename)
            elif tablename=="relationshipcheck":
                sql='''select relationship_mark as 总得分,2ndbank as 支行,allpts_now as 全量产品覆盖度,basepts_now as 基础产品覆盖度,
                               vcard as 私行卡持有率,relationship_mark1 as 产品覆盖得分,  relationship_mark2 as 达标保有得分,
                               relationship_mark3 as 商机应用得分,  relationship_mark4 as 金管家得分, relationship_mark5 as 档案维护得分
                               from {} where relationship_date='2018-06-30';'''.format(tablename)
            elif tablename=="investcheck":
                sql='''select invest_mark as 总得分,2ndbank as 支行,cash_aum_now/cash_aum_begin as 存款保有,
                               invest_mark1 as 投资理财配置得分,ftrust_investrate as 家族信托配置率,ccbsafe_rate as 建信高端完成率,
                               invest_mark2 as 重点产品得分,invest_mark3 as 贡献度得分 from {} where invest_date='2018-06-30';'''.format(tablename)
            df=pd.read_sql(sql,connect)
            markname=list(df.columns)
            pretablename=tablename
        arr=df[df['支行']==bankname].values
        mark =list(tuple(map(tuple,arr))[0])
    else:
        if pretablename!=tablename:
            sql='''select check_type, check_mark, 2ndbank as 支行 from {} where check_date='2018-06-30';'''.format(tablename)
            df=pd.read_sql(sql,connect)
            pretablename=tablename
        arr=df[df['支行']==bankname]
        markname=['支行','私行业务得分','至尊业务得分','投资理财得分','客户关系维护得分']
        mark=[bankname,tuple(arr.check_mark)[0],tuple(arr.check_mark)[1],tuple(arr.check_mark)[2],tuple(arr.check_mark)[3]]



def textmake(markname,mark):
    global resultframe
    if tablename != 'allmark':
        ##设置展示板标签容器(1,1)
        resultframe=tk.Frame(mainframe)
        resultframe.grid(row=1,column=1,sticky=tk.NW,pady=30)
        #设置默认标签框架
        labeltext = tk.LabelFrame(resultframe,text='评价内容',font=("微软雅黑",10),width=730,height=420)
        labeltext.grid(sticky=tk.NW)
        labeltext.grid_propagate(0)
        ###设置得分项和具体得分
        for y1 in range(3):
            for x1 in range(6):
                m=6*y1+x1
                if m==0:
                    labelre=tk.Label(labeltext,text="{}: {}".format(markname[m],mark[m]),fg="red",font=("微软雅黑",20))
                    labelre.grid(row=x1, column=y1, padx=30, pady=20, sticky=tk.W)
                elif m<len(mark):
                    if y1==0:
                        labelre=tk.Label(labeltext,text="{}: {}".format(markname[m],mark[m]),font=("微软雅黑",14))
                        labelre.grid(row=x1, column=y1, padx=30, pady=15, sticky=tk.W)
                    else:
                        labelre=tk.Label(labeltext,text="{}: {}".format(markname[m],mark[m]),font=("微软雅黑",14))
                        labelre.grid(row=x1+1, column=y1, padx=30, pady=15, sticky=tk.W)
    else:
        ##设置展示板标签容器(1,1)
        resultframe=tk.Frame(mainframe)
        resultframe.grid(row=1,column=1,sticky=tk.NW,pady=30)
        #设置默认标签框架
        labeltext = tk.LabelFrame(resultframe,text='评价内容',font=("微软雅黑",10),width=300,height=420,relief=tk.FLAT)
        labeltext.grid(row=0,column=0,sticky=tk.NW)
        labeltext.grid_propagate(0)
        for y1 in range(3):
            for x1 in range(6):
                m=6*y1+x1
                if m==0:
                    labelre=tk.Label(labeltext,text="{}: {}".format(markname[m],mark[m]),fg="red",font=("微软雅黑",20))
                    labelre.grid(row=x1, column=y1, padx=30, pady=20,sticky=tk.W)
                elif m<len(mark):
                    if y1==0:
                        labelre=tk.Label(labeltext,text="{}: {}".format(markname[m],mark[m]),font=("微软雅黑",14))
                        labelre.grid(row=x1, column=y1, padx=30, pady=15, sticky=tk.W)
                    else:
                        labelre=tk.Label(labeltext,text="{}: {}".format(markname[m],mark[m]),font=("微软雅黑",14))
                        labelre.grid(row=x1+1, column=y1, padx=30, pady=15, sticky=tk.W)
        #调用画布控件
        getpicture()

def getpicture():
    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 显示中文
    fig=plt.figure(figsize=(3.5,3.5), dpi=100,facecolor='#F0F0F0',)
    labels = markname[1:] # 标签
    dataLenth = 4  # 数据长度
    data_radar = mark[1:] # 数据
    angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)  # 分割圆周长
    data_radar = np.concatenate((data_radar, [data_radar[0]]))  # 闭合
    angles = np.concatenate((angles, [angles[0]]))  # 闭合
    plt.polar(angles, data_radar, 'bo-', linewidth=1)  # 做极坐标系
    plt.thetagrids(angles * 180/np.pi, labels)  # 做标签
    plt.fill(angles, data_radar, facecolor='r', alpha=0.25)# 填充
    plt.ylim(30, 130)
    canvas =FigureCanvasTkAgg(fig, master=resultframe)
    canvas.show()
    canvas.get_tk_widget().grid(row=0,column=1,pady=30)
    




####################主程序#######################    
    
#tkinter窗口设置
mainwin = tk.Tk()
mainwin.geometry("1080x720")
mainwin.title("评价查询系统")
choicetype = tk.StringVar()         #表类型选择变量


#一、设置标题
labeltitle = tk.Label(mainwin, text="评价查询系统", fg="red", font=("微软雅黑",16))
labeltitle.pack(pady=20)


#二、设置主容器
mainframe = tk.Frame(mainwin)
mainframe.pack()

##设置支行标签(0,0)
labelbank = tk.Label(mainframe, fg='blue',text='请选择支行',font=("微软雅黑",14))
labelbank.grid(row=0,column=0,sticky=tk.S,padx=30)
##--------------------------------------------------------------------------------------##

##设置支行子容器(1,0)
framebank = tk.Frame(mainframe)
framebank.grid(row=1,column=0,pady=25,padx=30)

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
labeltype.grid(row=0,column=1,sticky=tk.NW,columnspan=2)

###设置评价类型选项
n=1
for t in tablenames:
    rbtemtype = tk.Radiobutton(labeltype, text=t.split(".")[-1], font=("微软雅黑",14), 
                               variable=choicetype, value=t.split(".")[0], command=choosetype)
    rbtemtype.grid(row=1, column=n)
    if (n==1):
        rbtemtype.select()
        tablename = t.split(".")[0]
        pretablename = ""
    n+=1
##--------------------------------------------------------------------------------------##
##设置展示板标签容器(1,1)
resultframe=tk.Frame(mainframe)
resultframe.grid(row=1,column=1,sticky=tk.NW,pady=30)
#设置默认标签框架
labeltext = tk.LabelFrame(resultframe,text='评价内容',font=("微软雅黑",10),width=730,height=420)
labeltext.grid(sticky=tk.NW)
labeltext.grid_propagate(0)


#二、设置特殊按钮


button1 = tk.Button(mainwin, text="查询", width=8, command=play)
button1.pack()    




mainwin.mainloop()














