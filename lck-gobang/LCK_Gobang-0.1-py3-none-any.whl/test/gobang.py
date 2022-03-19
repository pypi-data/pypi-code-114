#简陋、无GUI、不像五子棋的五子棋
#初始化数据,row是行，column是列
Player="O"
num = 15 
flag = False
judge = 5
row = 0
column = 0
List= []

#这一段是欢迎进入游戏以及各种规则，建立一个嵌套列表方便定位
def init_input():
    global num
    global judge
    global List
    List = [[" " for j in range(num+1)] for i in range(num+1)]
    print("")
    print("Welcom to the Gomoku game!")
    print("")
    print("Caution:")
    print("")
    print("1.please don't input the number that more than 15")
    print("")
    print("2.please don't input the number that less than 0")
    print("")
    print("3.plaese don't input any character which not the number ")
    print("")
    print("I hope you could obey the rule")
    print("")
    print("May you have a good time")
    print("")
    input("Press 'Enter' key enter the Gomoku game immediately")
    print("")
    

    

#画棋盘
def chessboard():
    for i in range(15):
        print(" - - "*15)
        print("| ", end="")
        for j in range(15):
            print(" %s | " %List[i][j], end="")
        print("")
    print(" - - "*15)



#判断棋子横向的状况
def judge_row():
    global flag
    length = 1
    for a in range(1,judge):
        if List[row][column]==List[row][column+a]:
            length += 1
        else:
            break
    for a in range(1,judge):
        if List[row][column]==List[row][column-a]:
            length += 1
        else:
            break
    if length >= judge:
        flag=True

#判断棋子纵向情况
def judge_column():
    global flag
    length = 1
    for b in range(1,judge):
        if List[row][column]==List[row+b][column]:
            length += 1
        else:
            break
    for b in range(1,judge):
        if List[row][column]==List[row-b][column]:
            length += 1
        else:
            break
    if length >= judge:
        flag=True

#判断棋子两种斜向的情况    
def judge_slope1():
    global flag
    length = 1
    for c in range(1,judge):
        if List[row][column]==List[row+c][column-c]:
            length += 1
        else:
            break
    for c in range(1,judge):
        if List[row][column]==List[row-c][column+c]:
            length+=1
        else:
            break
    if length >= judge:
        flag=True

def judge_slope2():
    global flag
    length=1
    for d in range(1,judge):
        if List[row][column]==List[row+d][column+d]:
            length += 1
        else:
            break
    for d in range(1,judge):
        if List[row][column]==List[row-d][column-d]:
            length+=1
        else:
            break
    if length >= judge:
        flag = True

        
        

#用户棋子输入
def user_input():
    global List
    global row
    global column
    while True:
        row = int(input("please input your row lacation："))-1 
        print("") 
        column = int(input("please input which column lacation: "))-1 
        print("")
        if List[row][column] != " ":
            print("")
            print("This location is occupied")
            print("")
            continue
        List[row][column] = Player
        break
        

#棋子切换
def judge_user():
    global Player
    if Player == "O":
        Player="X"
    elif Player == "X":
        Player="O"

#判断棋子胜利的条件
def winner():
    global flag
    judge_row()
    judge_column()
    judge_slope1()
    judge_slope2()
    if flag == True:
        print("")
        print("%s is winner!" %Player)
        print("")
        return flag


#主要逻辑结构
init_input()
chessboard()
while True:
    user_input()
    chessboard()
    if winner():
        break
    judge_user()
input("Press 'Enter' key exit the Gomoku game immediately")
print("")

