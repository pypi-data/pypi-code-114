def dq(wjm):#读取文件，wjm=文件名
    with open(wjm,"r",encoding="UTF-8") as file:
        nr = file.read()
        return nr
def dqsc(wjm):#读取输出，wjm=文件名
    nr = dq(wjm)
    print(nr)