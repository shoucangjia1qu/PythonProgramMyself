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
#进入嵌套框架
browser.switch_to_frame('perbank-content-frame')
browser.switch_to_frame('content-frame')

for i in range(10):
    name = 0
    profit = 0
    money = 0
    data = 0
    buytime = 0
    curr_html = browser.page_source
    bs = BeautifulSoup(curr_html,"html.parser")
    table = bs.select('#datatableModel')[0]
    contents = table.select(".ebdp-pc4promote-circularcontainer")
    for row in contents:
        name = row.find_all("a")[0].text
        buytime = row.select(".ebdp-pc4promote-circularcontainer-text1")[0].text
        profit=row.select(".ebdp-pc4promote-doublelabel")[0].text.strip()
        money=row.select(".ebdp-pc4promote-doublelabel")[1].text.strip()
        data=row.select(".ebdp-pc4promote-doublelabel")[2].text.strip()
        if os.path.exists("icbc.txt"):
            with open("icbc.txt","r") as f:
                icbc = f.read()
            with open("icbc.txt","w") as f:
                try:
                    f.write(icbc+"\n"+name+","+profit+","+money+","
                            +data+","+buytime)
                except:
                    print("error")
                    f.write(str(icbc))
        else:
            with open("icbc.txt","w") as f:
                f.write(name+","+profit+","+money+","
                            +data+","+buytime)
                print("文件已写入")
    
    time.sleep(5)
    try:
        browser.find_element_by_xpath('//*[@id="pageturn"]/ul/li[4]').click()
    except:
        print("结束")
        break

browser.close()

