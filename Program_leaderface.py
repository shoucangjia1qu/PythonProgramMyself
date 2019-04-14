# -*- coding: utf-8 -*-

from PIL import Image
import cv2, os, shutil
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg



class face(object):
    def __init__(self):
        self.face_casade = cv2.CascadeClassifier("D:\\python\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
        self.dirname = 0
        self.faceloc = 0
        self.pic = 0
        self.mainface = 0
    
    def faceDective(self,dirname):
        img = cv2.imread(dirname)
        try:
            imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        except:
            self.dirname = 0
            self.faceloc = 0
            self.pic = 0
            return
        faceloc = self.face_casade.detectMultiScale(imgGray,scaleFactor=1.2,minNeighbors=5,minSize=(10,10),flags=cv2.CASCADE_SCALE_IMAGE)
        self.dirname = dirname
        self.faceloc = faceloc
        self.pic = img
    
    def drawpic(self,picname,faceloc=None):
        if faceloc is not None:
            row = 1
            for x,y,w,h in faceloc:
                picname = cv2.rectangle(picname,(x-5,y-5),(x+w+5,y+h+5),(0,255,0),5)
                cv2.putText(picname,"{}".format(row),(int(x+0.3*w),y+h+30),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),3)
                row += 1
        picname = picname[:,:,[2,1,0]]
        plt.imshow(picname)
        plt.xticks([]);plt.yticks([])       #隐藏坐标轴
        plt.show()
        
    def scratchface(self,dirname,faceloc,threshold,tp='M'):
        if not isinstance(threshold, int):
            raise ValueError('请输入整数字！')
        else:
            row = 1
            for x,y,w,h in faceloc:
                if row == threshold:
                    pic = Image.open(dirname)
                    face = pic.crop((x,y,x+w,y+h))
                    face = face.resize((200,200),Image.ANTIALIAS)
                    break
                else:
                    row += 1
            if tp=='M':
                self.mainface = face
            elif tp=='S':
                return face
            else:
                raise ValueError('tp must be M or S ! ')
                
    def faceCompare(self,targetdirname):
        self.faceDective(targetdirname)
        if isinstance(self.faceloc, int):
            return 0
        elif np.shape(self.faceloc)[0] == 0:
            return 0
        mainh=np.array(self.mainface.histogram())     #16等分，3组
        #对目标图片的脸一一比对
        for i in range(len(self.faceloc)):
            targetface = self.scratchface(targetdirname,self.faceloc,i+1,tp='S')
            targeth = np.array(targetface.histogram())
            try:
                diff = np.linalg.norm(mainh-targeth)/np.sqrt(len(mainh))        #对于黑白的无法进行计算
            except:
                return 0
            if diff<=100:
                return 1

class tkaction(face):
    def __init__(self):
        self.mainpicpath = 0
        self.searchdir = 0
        self.facequantity = 0
        self.maindirname = 0
        self.mainfaceloc = 0
        face.__init__(self)
        #super().__init__()
        
    def selectPic(self):
        mainpicpath = filedialog.askopenfilename()
        path.set(mainpicpath)
        self.mainpicpath = mainpicpath
#        self.showpic()

    def selectDir(self):
        searchdir = filedialog.askdirectory()
        srhdir.set(searchdir)
        self.searchdir = searchdir    
    
    def showpic(self):
        try:
            picerror.set('')
            dirname = pathchoose.get()
            self.faceDective(dirname)
            faceloc = self.faceloc
            picname = self.pic
            row = 1
            length = max(picname.shape)
            if length<1000:
                for x,y,w,h in faceloc:
                    picname = cv2.rectangle(picname,(x-5,y-5),(x+w+5,y+h+5),(0,255,0),2)
                    cv2.putText(picname,"{}".format(row),(int(x+0.3*w),y+h+int(0.08*length)),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    row += 1
            elif length<2000:
                for x,y,w,h in faceloc:
                    picname = cv2.rectangle(picname,(x-5,y-5),(x+w+5,y+h+5),(0,255,0),5)
                    cv2.putText(picname,"{}".format(row),(int(x+0.3*w),y+h+int(0.08*length)),cv2.FONT_HERSHEY_COMPLEX,3,(0,255,0),3)
                    row += 1
            else:
                for x,y,w,h in faceloc:
                    picname = cv2.rectangle(picname,(x-5,y-5),(x+w+5,y+h+5),(0,255,0),10)
                    cv2.putText(picname,"{}".format(row),(int(x+0.3*w),y+h+int(0.08*length)),cv2.FONT_HERSHEY_COMPLEX,5,(0,255,0),5)
                    row += 1
            picname = picname[:,:,[2,1,0]]
            plt.rcParams['font.sans-serif'] = ['KaiTi']  # 显示中文
            fig=plt.figure(figsize=((5.5,4.5)),dpi=100,facecolor='#F0F0F0')
            plt.xticks([]);plt.yticks([])       #隐藏坐标轴
            plt.imshow(picname)
            canvas =FigureCanvasTkAgg(fig, master=frameshow)
            canvas.get_tk_widget().grid(row=1,column=0,pady=10,padx=10,sticky=tk.N)
            self.maindirname = dirname
            self.facequantity = len(faceloc)
            self.mainfaceloc = faceloc
        except:
            picerror.set('请选择正确的图片！')
        
    def copypic(self,oldpath,filename):
        currentpath = os.getcwd()
        if not os.path.exists(currentpath+'\\leaderface'):
            os.mkdir(currentpath+'\\leaderface')
        if not os.path.exists(currentpath+'\\leaderface'+'\\'+filename):
            shutil.copy(oldpath,currentpath+'\\leaderface'+'\\'+filename)
    
    def search(self):
        picexts = ['jpg','jpeg','png','bgm']
        targetpath = text2other.get()
        if not os.path.exists(targetpath):
            searchlabel.set('请选择正确路径！')
            return
        try:
            thres = int(textother.get())
        except:
            searchlabel.set('请输入正整数！')
            return
        if thres>self.facequantity:
            searchlabel.set('请选择正确的编号！')
            return
        faceloc = self.mainfaceloc
        dirname = self.maindirname
        try:
            self.scratchface(dirname, faceloc, thres)       #截取需要检索的主图
#            searchlabel.set('搜索中......')
            for pathname, documents, files in os.walk(targetpath):
                for file in files:
                    ext = file.split('.')[-1]
                    if ext not in picexts:
                        continue
                    newpicpath = pathname+'/'+file
                    path1label.set(newpicpath)
                    mark = self.faceCompare(newpicpath)
                    if mark == 0:
                        continue
                    #赋值图片至指定目录
                    self.copypic(newpicpath,file)
            searchlabel.set('搜索完成！')
                    #界面上展示路径
        except:
            searchlabel.set('Error!')
        
    def opendir (self):
        currentpath = os.getcwd()
        if not os.path.exists(currentpath+'\\leaderface'):
            os.mkdir(currentpath+'\\leaderface')
        os.system('start '+currentpath+'\\leaderface')

        
            
            
            
            
tkact = tkaction()

#前端化
mainwin = tk.Tk()
mainwin.geometry("1080x720")
mainwin.title("leaderface")
path = tk.StringVar()
srhdir = tk.StringVar()
picerror = tk.StringVar()
searchlabel = tk.StringVar()
path1label = tk.StringVar()

#一、设置标题
labeltitle = tk.Label(mainwin, text="人脸图片检索系统", fg="red", font=("微软雅黑",16))
labeltitle.pack(pady=20)
#二、设置主容器
mainframe = tk.Frame(mainwin)
mainframe.pack()


##2.1设置子容器(0,0)
framechoose = tk.Frame(mainframe)
framechoose.grid(row=0,column=0,sticky=tk.W)
###设置文本框标签
labelchoose = tk.Label(framechoose, fg='black',text='请选择需检索图片:',font=("微软雅黑",14))
labelchoose.grid(row=0,column=0,padx=0,sticky=tk.W)
###设置选择图片按钮
buttonchoose = tk.Button(framechoose, text="选择", width=10, command=tkact.selectPic)
buttonchoose.grid(row=0,column=2,padx=10)
###设置路径展示框
path.set('')
pathchoose = tk.Entry(framechoose,width=(30),textvariable=path)
pathchoose.grid(row=0,column=1,sticky=tk.W)
###设置图片检索按钮
button2choose = tk.Button(framechoose, text="检索", width=10, command=tkact.showpic)
button2choose.grid(row=0,column=3,padx=10)


##2.2设置子容器(1,0)
frameshow = tk.Frame(mainframe)
frameshow.grid(row=1,column=0,columnspan=2,sticky=tk.W)
###设置错误提示标签
picerror.set('')
labelshow = tk.Label(frameshow, fg='red', font=("微软雅黑",14), textvariable=picerror)
labelshow.grid(row=0,column=0,padx=0,sticky=tk.NW)
###设置画布
canvasshow =tk.Canvas(frameshow, width=500,height=400)
canvasshow.grid(row=1,column=0,pady=10,padx=10,sticky=tk.N)
canvasshow.grid_propagate(0)


##2.3设置子容器(1,1)
frameother = tk.LabelFrame(mainframe,text='搜索图片',font=("微软雅黑",10),padx=15,width=320,height=500)
frameother.grid(row=1,column=2,sticky=tk.NW,padx=30)
frameother.grid_propagate(0)
###设置文本框标签
labelother = tk.Label(frameother, fg='black',text='faceID:',font=("微软雅黑",14))
labelother.grid(row=0,column=0,padx=10,sticky=tk.W,pady=10)
###设置输入框标签
textother = tk.Entry(frameother,width=10)
textother.grid(row=0,column=1,padx=10,pady=10)
###设置文本框2标签
label2other = tk.Label(frameother, fg='black',text='选择路径:',font=("微软雅黑",14))
label2other.grid(row=1,column=0,padx=10,sticky=tk.W,pady=10)
###设置读取路径1按钮
buttonother = tk.Button(frameother, text='选择路径', width=10, height=3, command=tkact.selectDir)
buttonother.grid(row=0,column=2,padx=10,pady=10,rowspan=2)
###设置输入框2标签
srhdir.set('')
text2other = tk.Entry(frameother, width=10, textvariable=srhdir)
text2other.grid(row=1,column=1,padx=10,pady=10)
###设置搜索时的内容
searchlabel.set('')
srhlabelother = tk.Label(frameother, fg='red', textvariable=searchlabel, font=("微软雅黑",14))
srhlabelother.grid(row=4,column=0,padx=10,pady=20,columnspan=3,sticky=tk.W)
###设置搜索2按钮
button2other = tk.Button(frameother, text="搜  索", width=30, command=tkact.search)
button2other.grid(row=3,column=0,padx=10,pady=20,columnspan=3)
###设置空白
blanklabelother = tk.Label(frameother, fg='red', text='', font=("微软雅黑",14),width=20,height=3)
blanklabelother.grid(row=5,column=0,padx=10,pady=10,columnspan=3,sticky=tk.W)
###设置打开文件夹
button3other = tk.Button(frameother, text="打开文件夹", width=10, height=3, command=tkact.opendir,  borderwidth=3, relief='ridge')
button3other.grid(row=6,column=2,padx=10,pady=10,rowspan=2)



mainwin.mainloop()







