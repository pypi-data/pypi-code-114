f = open('1.txt')  # 八进制文件保存在这里  这是目录
temp = []
while True:
    k = f.read(3)  # 三位一组
    if k:
        temp.append(k)
    else:
        break

f.close()
for i in temp:
    num = '0o' + i
    num = int(num, base=0)
    num = chr(num)
    print(num, end='')  # 使用python3版本运行该脚本
