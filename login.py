import tkinter as tk
from turtle import update

import mysql.connector
from tkinter import *
import tkinter.messagebox as msgbox

import password as password
import username as username
from PIL import Image, ImageTk

from main import Application

global session
session = False

#def connection():
#    conn = mysql.connector.connect(host = 'localhost' ,port=3306,user='root', password='rahul',database='inventory_system')
#    if(conn):
#        print("Database Connected ")
#   return conn

def handlelogin(username, password):
    print("Login button clicked")
    user = username.get()
    passw= password.get()

    if user == '' or passw == '':
        msgbox.showerror("uh-oh!", "Fields cannot be empty")
    else:
        conn = mysql.connector.connect(host='localhost', port=3306, database='inventory_system', user='root',
                                       password='')
        cursor = conn.cursor()
        #str = "select * from login where username ='" + username + "' and password ='" + password + "' "
        str = "insert into login(username,password) values('" + username + "','"+password+"')"
        # str=("CREATE TABLE `inventory_system`.`login` (`username` VARCHAR(25) NULL,`password` INT NULL)");

        cursor.execute(str)

        if cursor.fetchone():
            print("login successful")
            msgbox.showinfo("Success", "Login Validated")
            session = True
            loginpage.destroy()
            Application(session)
            user.set('')
            passw.set('')

        else:
            print("Invalid Credentials")
            msgbox.showerror("Error", "Invalid Credentials")


def loginpage():
    login = tk.Tk()
    login.geometry("500x500")
    login.title("Login Page")
    # root.title = PhotoImage(file='login_logo.png')
    canvas = Canvas(login, width=500, height=500, bg='light blue')
    canvas.place(x=0, y=0)
    canvas.config(borderwidth=0, border=0)

    logo = Canvas(canvas, width=175, height=175)
    logo.place(x=170, y=20)
    img = ImageTk.PhotoImage(Image.open("login_logo.png"), master=logo)
    logo.create_image(0, 0, anchor=NW, image=img)

    global username, password
    username = StringVar()
    password = StringVar()

    # Defining the first row
    lblfrstrow = tk.Label(login, text="Username -", font=('Arial 20 bold'), bg='black', fg='white')
    lblfrstrow.place(x=50, y=220, width=200)

    username = tk.Entry(login, font=('Arial 20 bold'), width=100)
    username.place(x=250, y=220, height=40, width=200)

    lblsecrow = tk.Label(login, text="Password -", font=('Arial 20 bold'), bg='black', fg='white')
    lblsecrow.place(x=50, y=270, width=200)

    password = tk.Entry(login, show='*', font=('Arial 40 bold'), width=100)
    password.place(x=250, y=270, height=40, width=200)

    submitbtn = tk.Button(login, text="Login", font=('Arial 20 bold'), bg='green', command=handlelogin)
    submitbtn.place(x=180, y=400, height=50, width=120)

    login.mainloop()

loginpage()
