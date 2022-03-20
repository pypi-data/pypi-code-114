import tkinter as tk
import time
from tkinter import filedialog
import os
bb = ""

def a():
    txt = filedialog.askopenfilename()

    temp.set(txt)


def b():
    print(temp.get())

if not os.path.exists("C:/Users/16662/Desktop/已超好的图片"):
    os.mkdir("C:/Users/16662/Desktop/已超好的图片")

def c():
    i=temp.get()
    # oi=1
    # o=oi+1
    name="C:/Users/16662/Desktop/已超好的图片"+"_4k.png"
    o=name
    print(o)
    txt = i
    start = time.time()
    tem2 = o
    z = "C:/Users/16662/Downloads/Compressed/realesrgan-ncnn-vulkan-20211212-windows/realesrgan-ncnn-vulkan.exe -i " + txt + " -o " + tem2 + " -n realesrgan-x4plus"
    print(z)
    print("开始处理")
    print("源文件:", txt)
    os.system(z)
    end = time.time()
    hh = "%.2f" % (end - start)
    print("----------")
    print("处理完成")
    print("")
    #print("输出位置:", h)
    print("本次耗时:", hh, "s")
    print("")
    input("按Enter退出")


top = tk.Tk()

temp = tk.StringVar()

g = tk.Button(top, text='选择文件', command=a)

g.pack()
k = tk.Button(top, text='显示路径', command=b)

k.pack()

p=tk.Button(top, text='超分辨率', command=c)
p.pack()
top.mainloop()

