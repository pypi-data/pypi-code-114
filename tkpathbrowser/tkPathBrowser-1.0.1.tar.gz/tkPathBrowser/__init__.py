import tkinter.filedialog
from tkinter import Tk
from tkinter.ttk import Button


class PathBrowser(object):
    """路径浏览器"""

    def __init__(self, master: Tk, tkPlus=None, default=''):
        """初始化"""
        self.master = master
        self.etr = tkPlus.functions.EntryWithPlaceholder(master, placeholder="请选择路径..")
        if default:
            self.etr.insert(0, default)

        self.btn = Button(self.master, text="浏览...", command=self.browse)

    def show(self,ln=1,col=1):
        """显示控件"""
        self.etr.grid(column=col,row=ln)
        self.btn.grid(column=col+1,row=ln)

    def browse(self, types=[], title="浏览..."):
        """浏览"""
        thing = tkinter.filedialog.askopenfilename(filetypes=types, title=title)  # 浏览文件
        self.change(thing)  # 切换内容

    def change(self, val):
        """更改内容"""
        self.etr.foc_in()  # 焦点转换，避免被视为提示
        self.etr.select_clear()  # 清空文本
        self.etr.insert(0, val)  # 重设
