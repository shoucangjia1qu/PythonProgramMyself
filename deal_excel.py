# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 20:43:23 2019

@author: ecupl
"""

import xlrd
import os

os.chdir("D:\\mywork\\test")
#1、打开文件
work = xlrd.open_workbook("exltest.xlsx")

#2、查看sheetname，并选择sheet
table = work.sheets()[0]                            #方法1：选取特定的sheet

sheet_names = work.sheet_names()
table = work.sheet_by_name(sheet_names[0])          #方法2：按照sheet名字选
table = work.sheet_by_index(1)                      #方法3：按照sheet索引顺序选

#3、查看表内容
table.nrows
table.ncols

