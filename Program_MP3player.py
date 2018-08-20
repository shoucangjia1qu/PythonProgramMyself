# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 22:14:20 2018

@author: ecupl
"""
#MP3音乐播放器
import tkinter as tk
import os, glob
from pygame import mixer

#定义选择函数
def choose():
    global playsong
    msg.set("\n播放歌曲："+choice.get().split('\\')[-1])
    playsong=choice.get()

#定义暂停函数
def pausemp3():
    mixer.music.pause()
    msg.set("\n暂停播放{}".format(playsong.split('\\')[-1]))

#定义音量调大函数
def increase():
    global volume
    volume+=0.1
    if volume>=1:
        volume=1
    mixer.music.set_volume(volume)

#定义音量调小函数
def decrease():
    global volume
    volume-=0.1
    if volume<=0.1:
        volume=0.1
    mixer.music.set_volume(volume)

#定义播放函数
def playmp3():
    global playsong, preplaysong
    if playsong==preplaysong:
        if not mixer.music.get_busy():
            mixer.music.load(playsong)
            mixer.music.play(loops=-1)
        else:
            mixer.music.unpause()
        msg.set("\n正在播放：{}".format(playsong.split('\\')[-1]))
    else:
        playNewmp3()
        preplaysong=playsong
        
#定义播放新曲函数
def playNewmp3():
    global playsong
    mixer.music.stop()
    mixer.music.load(playsong)
    mixer.music.play(loops=-1)
    msg.set("\n正在播放：{}".format(playsong.split('\\')[-1]))

#定义停止函数
def stopmp3():
    mixer.music.stop()
    msg.set("\n停止播放")

#定义结束函数
def exitmp3():
    mixer.music.stop()
    win.destroy()


#对象初始化
mixer.init()
#设置窗口
win = tk.Tk()
win.geometry("640x380")
win.title("\nMP3播放器")
#设置标题
labeltitle = tk.Label(win, text="MP3播放器", fg="red", font=("微软雅黑",12))
labeltitle.pack()
#设置歌曲容器
frame1 = tk.Frame(win)
frame1.pack()
#创建音乐目录
music_dir = "D:\\mywork\\test\\sounds\\"
musicfiles = glob.glob(music_dir+"*.mp3")+glob.glob(music_dir+"*.wav")

playsong = preplaysong = ""
index = 0
volume = 0.6
choice = tk.StringVar()
msg = tk.StringVar()

#创建歌曲选取菜单
for mp3 in musicfiles:
    pathname,mp3name = os.path.split(mp3)
    rbtem=tk.Radiobutton(frame1, text=mp3name, variable=choice, value=mp3, command=choose)
    #默认选取第一个
    if(index==0):
        rbtem.select()
        playsong=preplaysong=mp3
    rbtem.grid(row=index, column=0, sticky="w")
    index+=1

#创建歌曲播放信息
msg.set("\n播放歌曲：")
label = tk.Label(win, textvariable=msg,  fg="blue", font=("微软雅黑",10))
label.pack()
labelsep = tk.Label(win, text="\n")
labelsep.pack()

#创建按钮容器
frame2 = tk.Frame(win)
frame2.pack()
button1 = tk.Button(frame2, text="播放", width=8, command=playmp3)
button1.grid(row=0, column=0, padx=5, pady=5)
button2 = tk.Button(frame2, text="暂停", width=8, command=pausemp3)
button2.grid(row=0, column=1, padx=5, pady=5)
button3 = tk.Button(frame2, text="音量调大", width=8, command=increase)
button3.grid(row=0, column=2, padx=5, pady=5)
button4 = tk.Button(frame2, text="音量调小", width=8, command=decrease)
button4.grid(row=0, column=3, padx=5, pady=5)
button5 = tk.Button(frame2, text="停止", width=8, command=stopmp3)
button5.grid(row=0, column=4, padx=5, pady=5)
button6 = tk.Button(frame2, text="结束", width=8, command=exitmp3)
button6.grid(row=0, column=5, padx=5, pady=5)
win.protocol("WM_DELETE_WINDOW",exitmp3)
win.mainloop()



