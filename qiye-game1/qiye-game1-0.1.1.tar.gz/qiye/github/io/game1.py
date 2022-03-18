def get_info():
    n = 40
    q = 5
    index = q

    print("*"*n)
    for i in range(q):
        if i == q//2:
            str = "qiye is so boring!"
            p = len(str)
            print("*"*(i+1) + " "*((n-q-1)//4) + str + " "*((n-q-1)//4) + "*"*index)
        else:
            print("*"*(i+1) + " "*(n-q-1) + "*"*index)
        index -= 1
    print("*"*n)
