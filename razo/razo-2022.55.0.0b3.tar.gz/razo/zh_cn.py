pack=['''
版权所有 （c） 2022 Razo社区

特此免费授予任何获得副本的人的许可
此软件和相关文档文件（"软件"）的处理
在软件中没有限制，包括但不限于权利
使用、复制、修改、合并、发布、分发、再许可和/或出售
本软件的副本，并允许本软件所针对的人员
为此提供，但须符合以下条件：

上述版权声明和本许可声明应包含在所有
本软件的副本或大部分内容。

本软件按"原样"提供，不提供任何形式的明示或担保
暗示，包括但不限于适销性的保证，
适合特定用途和不侵权。在任何情况下都不得
作者或版权所有者对任何索赔、损害或其他责任负责
责任，无论是在合同诉讼、侵权行为还是其他情况下，均由以下原因引起：
出于或与本软件有关，或与本软件有关的使用或其他交易
软件。
''','Razo首次使用设置。',' 您同意上面的许可证吗？[y/n][默认为y]',"因为你不同意许可证，所以它正在关闭。",
'请设置root 密码（记得让别人不知道）：','你的用户名是什么（英文）？',
"键入help以获取帮助","仍在测试，请明白。",
'''
help：显示帮助。
su： 请求超级用户许可证。
shutdown：关闭razo。
info：显示信息。
setting：运行设置。
time：获取时间。
sudo（在命令之前添加）：让 sudo 之后的命令获得临时根用户权限。
[模块名称]：导入（运行）此模块。
''',
"请输入 root 密码：","su：抱歉","您真的想关机吗？[y/n]",
"关机。",{6:'星期日',0:'星期一',1:'星期二',2:'星期三',3:'星期四',4:'星期五',5:'星期六'},
'%Y-%m-%d %H：%M：%S','需要根用户权限','SYS1001：没有命令{}.',
"你好，{}.",'对不起。']
def timer():
    import datetime
    e=0
    while True:
        try:
            a=int(input('Hour:'))
            b=int(input('Minute:'))
            c=int(input('Second:'))
        except ValueError as e:
            print('Not vaild number')
        finally:
            if not e:
                break
    e=datetime.datetime.now()
    f=datetime.timedelta(hours=a,minutes=b,seconds=c)
    e+=f
    ins=[]
    for i in range(0,100000):
        ins.append(datetime.timedelta(microseconds=i))
    while True:
        print(datetime.datetime.now())
        if datetime.datetime.now()+f in ins:
            print('Time up!')
            break
