import tkinter as tk
from tkinter import filedialog


def a():
    txt = filedialog.askopenfilename()

    temp.set(txt)


def b():
    print(temp.get())


top = tk.Tk()

temp = tk.StringVar()

g = tk.Button(top, text='选择文件', command=a)

g.pack()
k = tk.Button(top, text='显示路径', command=b)

k.pack()

top.mainloop()
