# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 17:16:49 2018

@author: ecupl
"""

import os, shutil, docx

path = input("请输入搜索路径：")
keyword = input("请输入搜索词，多个以逗号隔开：").split(",")
os.chdir(path)
wordlist = []
for i in keyword:
    wordlist.append(i.strip())
finddir = 'FindDir'
filetrees = os.walk(path)



for dirname,subdir,files in filetrees:
    #创建文件夹
    if not os.path.exists(finddir):
        os.mkdir(finddir)
    #搜到目标文件夹自动跳过
    basename = os.path.basename(dirname)
    if basename == finddir:
        continue
    #首先找到所有文本文件，包括doc,docx,txt
    allfiles = []
    for file in files:
        ext = file.split(".")[-1]
        if ext=='doc' or ext=='docx' or ext=='txt':
            allfiles.append(dirname+"\\"+file)
    #按照文本类型打开文件，并搜索关键词
    for f in allfiles:
        pathname,filename = os.path.split(f)
        fext = filename.split('.')[-1]
        m = 0
        #对txt文件搜索
        try:
            if fext=='txt':
                try:
                    with open(f,'r') as ftxt:
                        rows = ftxt.readlines()
                except:
                    with open(f,'r',encoding='utf-8') as ftxt:
                        rows = ftxt.readlines()
                for word in wordlist:
                    n=1
                    for row in rows:
                        if word in row:
                            print(f)
                            print('【{}】在第{}行：“{}”'.format(word,n,row.strip()))
                            print('------------------------------------------')
                            m+=1
                        n+=1
            #对word文件搜索
            elif fext=='docx':
                #打开word
                doc=docx.Document(f)
                for word in wordlist:
                    n=1
                    for p in doc.paragraphs:
                        if word in p.text.strip():
                            print(f)
                            print('【{}】在第{}段：“{}”'.format(word,n,p.text.strip()))
                            print('------------------------------------------')
                            m+=1
                        n+=1
        except:
            print('{}无法打开'.format(f))
            print('------------------------------------------')
        #判断是否有符合要求文件，并复制
        if m>0:
            shutil.copy(f,path+'/'+finddir+'/'+filename)
input("按任意键退出")


















