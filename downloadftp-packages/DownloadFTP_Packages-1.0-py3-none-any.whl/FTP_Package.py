# @Time : 2022/3/17 23:57
# @Author : Mark
# @File : FTP_Package


from ftplib import FTP
import tkinter as tk
import os
import sys
# 导入消息对话框子模块
import tkinter.messagebox as tk_box
from threading import Thread

# # 项目
# project_model = "T8520"
#
# # 下载版本
# download_edition = '1.0.0.6'
#
# # 本地存放路径
# local_path = 'D:' + os.sep + '1' + os.sep

# 定义登录窗口
class LoginExecute():
    def __init__(self):
        self.win = tk.Tk()
        # 实例化FTP方法
        self.ftp = FTP()
        # 把窗口的 x 功能禁吊
        # 窗体的通信协议方法
        self.win.protocol('WM_DELETE_WINDOW', self.callback)
        # 软件标题
        self.win.title('登录')
        # 软件标题的图标
        self.win.iconbitmap(self.standard_path("main.ico"))
        # 初始化界面大小
        self.win.geometry('400x300')
        # 登陆界面
        tk.Label(self.win, text='FTP：').place(x=100, y=60)
        tk.Label(self.win, text='端口：').place(x=100, y=100)
        tk.Label(self.win, text='账户：').place(x=100, y=140)
        tk.Label(self.win, text='密码：').place(x=100, y=180)

        # FTP输入框
        self.var_ftp_host = tk.StringVar()
        # 设置初始值 --FTP
        self.var_ftp_host.set('172.16.23.240')
        self.enter_ftp_host = tk.Entry(self.win, textvariable=self.var_ftp_host)
        self.enter_ftp_host.place(x=160, y=60)
        # 端口输入框
        self.var_ftp_port = tk.StringVar()
        # 设置初始值--端口
        self.var_ftp_port.set(21)
        self.enter_ftp_port = tk.Entry(self.win, textvariable=self.var_ftp_port)
        self.enter_ftp_port.place(x=160, y=100)
        # 账号输入框
        self.var_usr_name = tk.StringVar()
        # 设置初始值 --账号
        self.var_usr_name.set('xdcftp')
        self.enter_usr_name = tk.Entry(self.win, textvariable=self.var_usr_name)
        self.enter_usr_name.place(x=160, y=140)
        # 密码输入框
        self.var_usr_pwd = tk.StringVar()
        # 设置初始值--密码
        self.var_usr_pwd.set('1q2w3e4r5t~!@')
        self.enter_usr_pwd = tk.Entry(self.win, textvariable=self.var_usr_pwd, show='*')
        self.enter_usr_pwd.place(x=160, y=180)


        # 登录按钮
        bt_login = tk.Button(self.win, text='登录', command=self.login_main)
        bt_login.place(x=120, y=230)
        # 退出按铃
        bt_logquit = tk.Button(self.win, text='退出', command=self.close_win)
        bt_logquit.place(x=260, y=230)

        self.win.mainloop()

    def login_main(self):
        self.host = self.enter_ftp_host.get()
        self.port = self.enter_ftp_port.get()
        self.user = self.enter_usr_name.get()
        self.poss = self.enter_usr_pwd.get()

        if self.host != '' and self.port != '' and self.user != '' and self.poss != '':
            # 访问ftp & 登录
            self.request_ftp()
            # 关闭窗口
            self.win.destroy()
            # 实例化FTP软件窗口
            w = FtpExecute()
            # 启动软件
            w.launch_window(self.ftp)
            print('FPT:%s,端口:%s' % (self.host, self.port))
            print('账号:%s,密码:%s' % (self.user, self.poss))
        else:
            if self.host == '':
                self.showinfo_window('FTP IP地址不能为空')
            else:
                pass
            if self.port == '':
                self.showinfo_window('FTP端口号不能为空')
            else:
                pass
            if self.user == '':
                self.showinfo_window('登录账号不能为空')
            else:
                pass
            if self.poss == '':
                self.showinfo_window('登录密码不能为空')
            else:
                pass

    # _______________________FTP______________________________
    # 初始化访问的ftp ip 和 端口号 & 登录
    def request_ftp(self):
        # 编码格式
        encode = ['UTF-8', 'gbk', 'GB2312', 'GB18030', 'Big5', 'HZ']
        # 断言是否可以正常连接ftp
        try:
            # 连接ftp
            self.ftp.connect(self.host, int(self.port))
            # 如果连接不到ftp报出提示
        except:
            # 无法连接到服务器
            self.showerror_window('无法连接FTP服务器,请检测网络')
            # 终止程序继续执行
            sys.exit(0)
        else:
            # 给ftp设置 gbk 的编码格式
            self.ftp.encoding = encode[1]
            # 登录
            self.login()

        # 登录方法----用户名，密码

    def login(self):
        # 登录 ftp
        self.ftp.login(self.user, self.poss)
        # 欢迎信息
        # print(self.ftp.welcome)




    # 提示消息框
    def showinfo_window(self, messages):
        # 去掉tk弹框
        tk.Tk().withdraw()
        tk_box.showinfo(title="提示", message=messages)

    # 错误弹框
    def showerror_window(self, messages):
        # 去掉tk弹框
        tk.Tk().withdraw()
        # 弹出错误提示框
        tk_box.showerror(title="错误信息", message=messages)

    # 窗口显示图标 -- 目的:准确目录
    def standard_path(self, retative_path):
        try:
            base_path = sys._MEIPASS
        except:
            # 获取根目录
            base_path = os.path.abspath('')
            # base_path = self.gml + os.sep + 'logo' + os.sep
        # 文件名称与路径拼接
        return os.path.join(base_path, retative_path)

    # 这个函数不做任何事，实际上让关闭按钮失效
    def callback(self):
        pass

    # 这个函数做两个事情，关闭窗口&结束程序
    def close_win(self):
        # 关闭窗口
        self.win.destroy()
        # 终止程序 -- 线程也会死掉
        sys.exit(0)

# 定义FTP软件窗口
class FtpExecute():
    # 这个函数不做任何事，实际上让关闭按钮失效
    def callback(self):
        pass

    # 窗口显示图标 -- 目的:准确目录
    def standard_path(self, retative_path):
        try:
            base_path = sys._MEIPASS
        except:
            # 获取根目录
            base_path = os.path.abspath('')
            # base_path = self.gml + os.sep + 'logo' + os.sep
        # 文件名称与路径拼接
        return os.path.join(base_path, retative_path)

    # 启动窗口
    def launch_window(self, ftp):
        # 初始化 ftp ip、ftp 端口、登录账号、登录密码
        self.ftp = ftp
        # 初始化窗口库
        self.root = tk.Tk()

        # 把窗口的 x 功能禁吊
        # 窗体的通信协议方法
        self.root.protocol('WM_DELETE_WINDOW', self.callback)

        # # 把窗口隐藏
        # self.root.withdraw()
        # 软件标题
        self.root.title('OTA一键下载工具_v2.0')
        # 取消标题栏
        # root.overrideredirect(True)
        # 软件标题的图标
        self.root.iconbitmap(self.standard_path("main.ico"))
        # 初始化窗口大小
        self.root.geometry('570x220')
        # 最大化窗口大小
        # self.root.maxsize(1080, 860)
        # 窗口背景验证
        self.root.configure(bg="pink")

        tk.Label(self.root, text='请输入需要下载的项目(T8213、T8520【注:不能有空格】): ', font=('微软雅黑', 12), bg="pink").grid(row=0, column=0)
        self.project_model = tk.Entry(self.root, text='', width=13, font=('微软雅黑', 9))
        self.project_model.grid(row=0, column=1)

        tk.Label(self.root, text='请输入需要下载的版本(1.0.0.6、0.0.9.7【注:不能有空格】): ', font=('微软雅黑', 12), bg="pink").grid(row=1, column=0)
        self.download_edition = tk.Entry(self.root, text='', width=13, font=('微软雅黑', 9))
        self.download_edition.grid(row=1, column=1)

        tk.Label(self.root, text=r'请输入本地存放路径(D:\test  C:\User 【注:不能有空格】): ', font=('微软雅黑', 12), bg="pink").grid(row=2, column=0)
        self.local_path = tk.Entry(self.root, text='', width=13, font=('微软雅黑', 9))
        self.local_path.grid(row=2, column=1)

        self.but1 = tk.Button(self.root, text='一键下载', font=('微软雅黑', 12), width=8, height=1, command=lambda: self.download_info())
        self.but1.grid(row=3, column=1)

        # 只有通过这个退出按钮才可以退出程序  退出关闭窗口 结束主程序 随后线程自己死掉
        self.but2 = tk.Button(self.root, text=" 退 出 ", font=('微软雅黑', 12), width=8, height=1, command=lambda: self.close_win())
        self.but2.grid(row=8, column=1)
        self.root.mainloop()

    # 下载显示信息显示
    def download_info(self):
        # 定义 "项目编号" "版本号" "本地存放路径" "在末尾加在 \ 号变成新的本来存放路径" 的全局变量
        global project_model, download_edition, local_path, new_local_path
        # 将输入的项目 版本号 本地存放路径 数据 赋值给 对应的全局变量
        project_model = self.project_model.get()
        download_edition = self.download_edition.get()
        local_path = self.local_path.get()

        # 如果都不为空可以进行下一步
        if project_model != '' and download_edition != '' and local_path != '':
            # 显示下载信息
            self.download = tk.Label(self.root, text='正在下载:                                                                     ',
                                     bg="pink", font=('微软雅黑', 12))
            self.download.grid(row=4, column=0)
            self.clock = tk.Entry(self.root, bg="pink", bd=0, width=50, font=('微软雅黑', 12))
            self.clock.grid(row=5, column=0)
            self.clock.insert(0, '    加载中......')

            '''
                异步操作：
                    1.访问ftp服务器
                    2.登录ftp
                    3.通过输入的本地存放路径 得到 本地路径和远程路径
                    4.传入本地路径和远程路径 开始下载
                    5.下载成功后弹出提示框
                    6.下载完成后退出FTP
            '''
            Thread(target=self.start_download).start()
        else:
            # 判断设备版本是否为空
            if project_model == '':
                self.showinfo_window('项目编号不能为空')
            else:
                pass

            # 判断基站版本是否为空
            if download_edition == '':
                self.showinfo_window('下载的版本不能为空')
            else:
                pass

            # 判断输入的本地路径是否为空
            if local_path == '':
                self.showinfo_window('本地存放路径不能为空')
            else:
                pass

    # 这个函数做两个事情，关闭窗口&结束程序
    def close_win(self):
        # 关闭窗口
        self.root.destroy()
        # 终止程序 -- 线程也会死掉
        sys.exit(0)

    '''
    异步操作：
        1.访问ftp服务器
        2.登录ftp
        3.通过输入的本地存放路径 得到 本地路径和远程路径
        4.传入本地路径和远程路径 开始下载
        5.下载成功后弹出提示框
        6.下载完成后退出FTP
    '''
    def start_download(self):
        # 关闭窗口
        # self.root.destroy()
        # 实例化ftp文件下载 & 登录  -- ftp ip地址 端口 账号 密码
        # self.request_ftp(self.ftp_host, self.ftp_port, self.ftp_user, self.ftp_passwd)



        # "在末尾加在 \ 号变成新的本来存放路径"
        new_local_path = local_path + os.sep
        # 通过输入的本地存放路径 得到 本地路径和远程路径
        data = self.create_path(new_local_path)
        # 传入本地路径和远程路径 下载
        self.download_catalogue(data[0], data[1])
        # 下载成功后弹出提示框
        self.showinfo_window("下载完成")
        # 退出FTP
        self.quit_()

    # 提示消息框
    def showinfo_window(self, messages):
        # 去掉tk弹框
        tk.Tk().withdraw()
        tk_box.showinfo(title="提示", message=messages)

    # 错误弹框
    def showerror_window(self, messages):
        # 去掉tk弹框
        tk.Tk().withdraw()
        # 弹出错误提示框
        tk_box.showerror(title="错误信息", message=messages)

















    # _______________________FTP______________________________
    # 通过"项目型号“和”版本号“ 获取 ”需要下载的文件“ 和 ”ftp中项目存放路径“
    def get_filename(self, projectModel, downloadEdition):
        """
        projectModel: 项目编号
        downloadEdition: 下载版本

        """

        # ftp中项目存放路径
        projectRoute = f"/TestVersion/{projectModel}/"

        # 设置FTP当前操作的路径--进入该路径
        self.ftp.cwd(projectRoute)

        # 获取目录下的文件
        list = self.ftp.nlst()
        # print(f"版本数目：{len(list)}个。分别为：", list)

        # 遍历目录
        for file in list:
            # 通过输入下载的版本号获取该版本号的文件夹
            if file.endswith(downloadEdition):
                # 将 "该文件夹名" 和 "ftp中项目存放路径" 返回备用
                return [file, projectRoute]

    # 创建路径 -- 本地存放路径
    def create_path(self, local):
        # 通过"项目型号“和”版本号“ 获取 ”需要下载的文件“ 和 ”ftp中项目存放路径“
        # 所以downloadfile_info [需要下载的文件名, ftp中项目存放路径]
        downloadfile_info = self.get_filename(project_model, download_edition)

        # 创建路径 - 本地路径
        localPath = local + downloadfile_info[0]
        # 创建路径 - 远程路径
        mstscPath = downloadfile_info[1] + downloadfile_info[0]
        # print("本地地址：", local_path)
        # print("远程地址：", mstsc_path)
        # 返回 本地路径 和 远程路径
        return [localPath, mstscPath]

    # 下载单个文件  下载文件到Local_file  被下载文件mstsc_file
    def download_file(self, local_file, mstsc_file):
        print('开始%s' % mstsc_file)
        # #改变弹框中的值前 先删除
        self.clock.delete(0, tk.END)
        # 改变弹框中的值
        self.clock.insert(0, '    ' + mstsc_file)
        # start = time.time()

        # 以二进制的方式打开local_file
        file = open(local_file, 'wb')
        # ftp命令: RETR<filename> 从服务器上找回（复制）文件
        # 接收服务器上文件并写入本地文件
        self.ftp.retrbinary(cmd='RETR ' + mstsc_file, callback=file.write)
        # 完成如上操作后关闭打开的file文件
        file.close()

        print('结束%s' % mstsc_file)
        # print('%s下载完成,耗时%.2f秒' % (mstsc_file, time.time()-start))

    # 下载整个目录 local_dir(本地目录), mstsc_dir(远程目录)
    '''
        只要是目录:
            1.更新本地路径和远程路径
            2.检测本来是否有该路径---没有就创建
            3.将远程路径切到更新后的远程路径中
        不是路径
            直接下载
    '''

    def download_catalogue(self, local_dir, mstsc_dir):
        # 判断本地目录不存在
        if not os.path.exists(local_dir):
            # 创建本地目录
            os.makedirs(local_dir)

        # 进入远程操作目录 - 下载准备工作
        self.ftp.cwd(mstsc_dir)
        # 获取远程目录下的文件 - 准备下载
        remote_files = self.ftp.nlst()
        # print("远程文件目录：", remote_files)
        # 遍历远程目录下的文件
        for file in remote_files:
            # 将 远程路径 与 远程目录下的文件下遍历的文件 进行路径拼接 -- new远程路径
            Mstsc = mstsc_dir + '/' + file

            # Mstsc_dir = mstsc_dir + "/MCU/T8520_APP_V1.0.1.0.bin" # 不是目录实验
            # # 将 本地路径 与 远程目录下的文件下遍历的文件 进行路径拼接 -- new本地路径
            Local = os.path.join(local_dir, file)

            # print("正在下载", self.ftp.nlst(file))
            # Info_box(self.ftp.nlst(file))
            try:
                # 如果能正常进入--代表是文件夹
                self.ftp.cwd(Mstsc)

                # 返回出来，上面进入是测试是否是文件夹
                self.ftp.cwd("..")

                # 重新调用该方法(递归) -- 把new的本地路径和new的远程路径传过去
                self.download_catalogue(Local, Mstsc)
            except:
                # 上面报错代表不是文件夹，# 是固件包 -- 直接下载
                self.download_file(Local, file)

                # # 异步处理
                # t = Thread(target=self.download_info, args=(Local, file, ))
                # t.start()

        # 一个目录下载完后返回上个目录 ???? - 执行完后这个语句不是结束了从执行效果看反复调用此方法
        self.ftp.cwd('..')

    # 关闭ftp连接
    def close_(self):
        self.ftp.close()

    # 退出ftp
    def quit_(self):
        self.ftp.quit()








