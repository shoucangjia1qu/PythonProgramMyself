# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:13:27 2018

@author: ecupl
"""
 
from selenium import webdriver
import os,time
os.chdir(r"D:/mywork/test")
from urllib.request import urlopen, quote
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://mybank.icbc.com.cn/icbc/newperbank/perbank3/frame/frame_index.jsp"
browser = webdriver.Chrome()
browser.get(url)
time.sleep(30)
browser.find_element_by_xpath('//*[@id="moreproducts"]').click()
curr_html = browser.page_source

name = 0
profit = 0
money = 0
data = 0
buytime = 0

bs = BeautifulSoup(curr_html,"html.parser")
tables = bs.select('#licai')
contents = tables[0].find_all("li")
for row in contents:
    fs = row.find_all('div')
    name=(fs[0].text.strip())
    profit=(fs[3].text.strip().split()[0])
    money=(fs[4].text.strip().split())
    data=(fs[5].text.strip().split())
    buytime=(fs[6].text.strip())
    if os.path.exists("icbc.txt"):
        with open("icbc.txt","r") as f:
            icbc = f.read()
        with open("icbc.txt","w") as f:
            try:
                f.write(icbc+"\n"+name+","+profit+","+str(money[0])+":"+str(money[1])+","
                        +str(data[0])+":"+str(data[1])+","+buytime)
            except:
                print("error")
                f.write(str(icbc))
    else:
        with open("icbc.txt","w") as f:
            f.write(name+","+profit+","+str(money[0])+":"+str(money[1])+","
                        +str(data[0])+":"+str(data[1])+","+buytime)
            print("文件已写入")

time.sleep(10)
browser.find_element_by_xpath('//*[@id="pageturn"]/ul/li[4]').click()
time.sleep(10)

#except:
#    print("结束")

browser.close()

