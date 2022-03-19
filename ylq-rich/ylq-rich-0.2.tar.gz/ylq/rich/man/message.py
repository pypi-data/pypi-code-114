import sys
print(f"输入的参数个数：{len(sys.argv)}")
if len(sys.argv) == 1:
    print("未输入参数，程序退出！")
    sys.exit(0)
else:
    print("程序的输入参数：",end = ' ')
    for item in sys.argv:
        print(item,end = ' ')