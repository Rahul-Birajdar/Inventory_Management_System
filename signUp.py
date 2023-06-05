from tkinter import *
from turtle import update

import mysql.connector
import tkinter.messagebox as msgbox

from login import loginpage
#from update import mycursor

fontStyle = "Tahoma"
fontSize = 18

global windowSize1
windowSize1 = "800x500+380+50"

global session
session = False

def handlesignUp(username, password):
    print("SignUp button clicked")
    user = username.get()
    passw = password.get()

    if user == '' or passw == '':
        msgbox.showerror("uh-oh!", "Fields cannot be empty")
    else:
        conn = mysql.connector.connect(host='localhost', port=3306, database='inventory_system', user='root',password='')
        cursor = conn.cursor()
        #str = "select * from signup where username ='" + user + "' and password ='" + passw + "' "
        str = "insert into signup(username,password) values('" + username + "','" + password + "')"
        #str = ("CREATE TABLE `inventory_system`.`signup` (`username` VARCHAR(25) NULL,`password` INT NULL)");
        cursor.execute(str)

        if cursor.fetchone():
            print("SignUp successful")
            msgbox.showinfo("Success", "SignUp Validated")
            session = True
            signuppage.destroy()
            loginpage(session)
            username.set('')
            password.set('')

        #else:
        #    print("Invalid Credentials")
        #    msgbox.showerror("Error", "Invalid Credentials")


def signuppage():
    signup = Tk()
    signup.geometry(windowSize1)
    signup.title("Sign Up page")
    global username,password
    username = StringVar()
    #name = StringVar()
    password = StringVar()
    Label(signup, text="Username", font=(fontStyle, fontSize)).pack(pady=15)
    Entry(signup, textvariable=username, font=(fontStyle, fontSize)).pack(pady=15)
    Label(signup, text="Password", font=(fontStyle, fontSize)).pack(pady=15)
    Entry(signup, textvariable=password, show="*", font=(fontStyle, fontSize)).pack(pady=15)
    Button(signup, text="Sign UP",command=handlesignUp).pack(pady=15)

    signup.mainloop()

signuppage()
