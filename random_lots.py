# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 19:28:59 2018

@author: ecupl
"""

import random, time, os

def menu():
    os.system('cls')
    print('请选择抽签类型：')
    print('-----------------------')
    print('1.随机式抽签')
    print('2.随机不重复抽签')
    print('3.概率分布式抽签')
    print('0.结束程序')
    print('-----------------------')


#随机抽签
def RandomDrawRe():
    inputx = input('请输入个数')
    while True:
        randomNum = random.randint(1,int(inputx))
        print(randomNum)
        print('================================================\n')
        time.sleep(0.5)
        nextstep = input('输入S停止抽签，输入C更换个数，其他任意键继续')
        if nextstep == 'S' or nextstep == 's':
            break
        if nextstep == 'C' or nextstep == 'c':
            inputx = input('请重新输入个数')


#随机不重复抽签
def RandomDraw():
    inputx = input('请输入个数')
    randomList = list(range(1,int(inputx)+1))
    while True:
        randomNum = random.sample(randomList,1)[0]
        print(randomNum)
        print('================================================\n')
        randomList.remove(randomNum)
        time.sleep(0.5)
        if len(randomList) == 0:
            print('当前已抽签完毕!!!')
        nextstep = input('输入S停止抽签，输入C更换个数，其他任意键继续')
        if nextstep == 'S' or nextstep == 's':
            break
        if nextstep == 'C' or nextstep == 'c':
            RandomDraw()
            break
        if len(randomList) == 0:
            break

#概率分布式抽签
def ProDraw():
    inputarr = input('请输入具体名单，以逗号隔开').split(',')
    inputrate = input('请输入概率，以逗号隔开').split(',')
    inputrate = list(map(int, inputrate))
    while True:
        start = 0
        index = 0
        randnum = random.randint(1, sum(inputrate))
        for index, scope in enumerate(inputrate):
            start+=scope
            if randnum <= start:
                break
        print(inputarr[index])
        print('================================================\n')
        time.sleep(0.5)
        nextstep = input('输入S停止抽签，输入C更换个数，其他任意键继续')
        if nextstep == 'S' or nextstep == 's':
            break
        if nextstep == 'C' or nextstep == 'c':
            inputarr = input('请输入具体名单，以逗号隔开').split(',')
            inputrate = input('请输入概率，以逗号隔开').split(',')
            inputrate = list(map(int, inputrate))
    

#主程序
print('HELLO,抽签即将开启，请稍等......')
j=3
for i in range(1,4):
    print(j)
    time.sleep(1)
    j-=1
while True:
    menu()
    choice = int(input('请输入您的选择：'))
    print()
    if choice == 1:
        RandomDrawRe()
    elif choice == 2:
        RandomDraw()
    elif choice == 3:
        ProDraw()
    elif choice == 0:
        break
print('^_^程序执行完毕，即将自动关闭^_^')
j=3
for i in range(1,4):
    print(j)
    time.sleep(1)
    j-=1
        
            
        
        
        
        
        
        
        
        
        







