'''
作者:zlq
日期:18-4-15
'''
'''
1. 模拟qq注册的功能,要求如下:
   1) 使用tkinter gui库完成客户端注册界面
   2) 服务端存储客户端注册信息使用sqlite3数据库
   3) 使用面向对象编程
'''
import tkinter as tk
from  tkinter import messagebox
import sqlite3

window = tk.Tk


def window_info():
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - 200
    y = (hs / 2) - 200
    print("%d，%d" % (ws,hs))
    return x,y


# 设置登陆窗口属性
window = tk.Tk()
window.title('欢迎来到QQ登陆界面')
a,b = window_info()
window.geometry("450x300+%d+%d" % (a,b))


tk.Label(window,text = "QQ登陆界面").place(x=80,y=50)
tk.Label(window,text = "账号").place(x=120,y=150)
tk.Label(window,text = "密码").place(x=120,y=190)


var_usr_name = tk.StringVar()
var_usr_name.set('10001')
#entry_usr_name = tk.Entry(window,textvarlable = var_usr_name)
#entry_usr_name.place(x=190,y=150)
var_usr_pwd = tk.StringVar()

entry_usr_pwd = tk.Entry(window,textvariable = var_usr_name)
entry_usr_pwd.place(x=190,y=190)

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    dicts = sqlite3.load('login')
    print(dicts)
    bool =False
    for row in dicts:
        print(row.get("name"))
    if usr_name == row["name"]:
        bool = True
        pwd = row["password"]
        print(row)
    if bool == True:
        if usr_pwd == pwd:
            tk.messagebox.showinfo(title='ture',message='hello'+usr_name)

        else:
            tk.messagebox.showerror(message='输入错误')





        # 登陆和注册按钮
btn_login = tk.Button(window,text = "登陆")
btn_login.place(x=170,y = 230)
btn_sign_up = tk.Button(window,text = "注册")
btn_sign_up.place(x=270,y = 230)


window.mainloop()