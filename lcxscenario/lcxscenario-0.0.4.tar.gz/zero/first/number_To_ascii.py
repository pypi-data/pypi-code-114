flag = '98 117 103 107 117 123 110 97 48 100 48 110 103 100 97 107 97 49 125'
flag = flag.split(' ')
for i in flag:
    print(chr(int(i)),end="")          #十进制转换成ascii码