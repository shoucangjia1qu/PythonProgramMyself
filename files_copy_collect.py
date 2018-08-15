# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 15:24:08 2018

@author: ecupl
"""

import os, shutil

print(os.getcwd())
path = input("请输入需要整理的文件夹路径")
#os.chdir(path)
fileext = input("请输入需要整理的文件后缀，多个以英文逗号隔开（如：jpg,png,docx,xls等）").split(",")
pathfiles = os.walk(path)

exts = []
for i in fileext:
    exts.append(i.strip())
SaveDir = 'SaveDir'
n = 1
for dirname, subdir, files in pathfiles:
    basename = os.path.basename(dirname)
    if basename == SaveDir:
        continue
    #创建专属文件夹
    if not os.path.exists(path+"\\"+SaveDir):
        os.mkdir(path+"\\"+SaveDir)
    #搜索找到图片文件->改文件名->复制
    
    for file in files:
        ext = file.split('.')[-1]
        if ext in exts:
            old_name = dirname+"\\"+file
            new_name = path+"\\"+SaveDir+"\\"+"Pic%d"%n+"."+ext
            shutil.copy(old_name, new_name)
            print(old_name)
            n+=1









