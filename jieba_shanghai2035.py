# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 21:15:17 2018

@author: ecupl
"""
#上海2035规划
import requests,os,jieba
from bs4 import BeautifulSoup
from pyecharts import WordCloud
import jieba.analyse

os.chdir("D:\\mywork\\test\\word")
with open("shanghai2035ori.txt","r") as f:
    #f.encoding="utf-8"
    text=f.readlines()

#给文章分章节
article = text
texts=[]
listnum = ['一','二','三','四','五','六','七','八']
#把前七章加入
for number in listnum:
    n=0
    strs = ""
    for i in article:
        charpter = "第{}章".format(number)
        if charpter in i:
            texts.append(strs)
            del article[0:n]
            break
        else:
            i = i.strip()
            strs+=i
            n+=1
#加入第八章
strs = ""
for i in article:
    i = i.strip()
    strs+=i
texts.append(strs)          
#去掉空值
texts.pop(0)
#去掉空格
shanghai =[]
for i in texts:
    a=i.replace("\t","")
    shanghai.append(a)

#开始分词
m=0
for char in shanghai:
    strs = char
    cuts = jieba.lcut(strs)
    words = jieba.analyse.textrank(strs,topK=15,withWeight=True,allowPOS=( 'n'))
    words2 = jieba.analyse.textrank(strs,topK=15,withWeight=True,allowPOS=( 'v'))

    #名词图
    print("\n第{}章名词图".format(listnum[m]))
    listx = []
    listy = []
    for word,weight in words:
        cutcount = cuts.count(word)
        print(word+"出现{}次".format(cutcount),weight)
        listx.append(word)
        listy.append(weight*10000)
        
    name = listx
    value = listy
    wordcloud = WordCloud(width=1500, height=1000)
    wordcloud.add("上海2035规划第{}章名词图".format(listnum[m]), name, value, word_size_range=[50, 200])
    wordcloud.render('上海2035规划第{}章名词图.html'.format(listnum[m]))    

    #动词图
    print("\n第{}章动词图".format(listnum[m]))
    listx = []
    listy = []
    for word2,weight2 in words2:
        cutcount2 = cuts.count(word2)
        print(word2+"出现{}次".format(cutcount2),weight2)
        listx.append(word2)
        listy.append(weight2*10000)
        
    name = listx
    value = listy
    wordcloud = WordCloud(width=1500, height=1000)
    wordcloud.add("上海2035规划第{}章动词图".format(listnum[m]), name, value, word_size_range=[50, 200])
    wordcloud.render('上海2035规划第{}章动词图.html'.format(listnum[m]))
    
   
    
    m+=1




#全篇文章来一个
strall = ""
for i in text:
    i = i.strip()
    strall+=i
strall = strall.replace("\t","")

cuts = jieba.lcut(strall)
words = jieba.analyse.textrank(strall,topK=25,withWeight=True,allowPOS=( 'n'))
words2 = jieba.analyse.textrank(strall,topK=25,withWeight=True,allowPOS=( 'v'))

#名词图
print("\n全篇名词图")
listx = []
listy = []
for word,weight in words:
    cutcount = cuts.count(word)
    print(word+"出现{}次".format(cutcount),weight)
    listx.append(word)
    listy.append(weight*10000)
    
name = listx
value = listy
wordcloud = WordCloud(width=1500, height=1000)
wordcloud.add("上海2035规划全篇名词图", name, value, word_size_range=[50, 200])
wordcloud.render('上海2035规划全篇名词图.html')    

#动词图
print("\n全篇动词图")
listx = []
listy = []
for word2,weight2 in words2:
    cutcount2 = cuts.count(word2)
    print(word2+"出现{}次".format(cutcount2),weight2)
    listx.append(word2)
    listy.append(weight2*10000)
    
name = listx
value = listy
wordcloud = WordCloud(width=1500, height=1000)
wordcloud.add("上海2035规划全篇动词图", name, value, word_size_range=[50, 200])
wordcloud.render('上海2035规划全篇动词图.html')
#统计分词数量
dicts={}
for i in cuts:
    dicts[i] = dicts.get(i,0)+1






