def dq(wjm):#读取文件，wjm=文件名
    with open(wjm,"r",encoding="UTF-8") as file:
        nr = file.read()
        return nr
def dqsc(wjm):#读取输出，wjm=文件名
    nr = dq(wjm)
    print(nr)
def dqzs(wjm,bt,dx,ztdx):
    nr = dq(wjm)
    import tkinter as t
    window = t.Tk()
    window.title(bt)
    window.geometry(dx)
    wz = t.Label(window,text=nr,font=("kaiti",ztdx))
    wz.pack()
    window.mainloop()
def tpzs(tpm,bt,dx):
    import tkinter as t
    window = t.Tk()
    window.title(bt)
    window.geometry(dx)
    img = t.PhotoImage(file=tpm)
    wz = t.Label(window,image=img)
    wz.pack()
    window.mainloop()