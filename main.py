from tkinter import *


root = Tk()
root.geometry('1010x550+200+40')
root.resizable(False,False)
root.configure(background='white')
root.title('Database Controlls')
# root.iconbitmap('images/icon.ico')
title1 = Label(root,text='Database Controlls System12345',fg='white',bg='#19282F',font=('Tajawal',15))
title1.pack(fill=X)
    
#============= show databases ========

def show_dbs():

    import pymysql.connections
    import mysql.connector
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = ''
    )
    mycur = conn.cursor()
    mycur.execute('SHOW DATABASEs')
    
    F = Frame(root,bg='whitesmoke',bd=2,relief=GROOVE)
    F.place(x=440,y=240,width=170,height=300)
    title2 =Label(F,text='Database Founds',fg='black',bg='#FF6363',height=2)
    title2.pack(fill=X)
    for x in mycur :
        Label(F,text=x).pack()

def DB_Connect():
    import mysql.connector
    from tkinter import messagebox 
    host = Enn1.get()
    user = Enn2.get()
    passw = Enn3.get()
    try:
        conn = mysql.connector.connect(
            host = host,
            user = user,
            password = passw
        )
        messagebox.showinfo('DB[Style]','The Connect Done !')
    except mysql.connector.Error as r :
        messagebox.showerror('Error',r)

def  DBcreate():
    import mysql.connector
    from tkinter import messagebox

    db = En1.get()
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = ''
        )
        mycur = conn.cursor()
        mycur.execute('CREATE DATABASE {}'.format(db))
        messagebox.showinfo('DB[System]','Create is Done')
    except mysql.connector.Error as r:
        messagebox.showerror('Error', r)


def Col():
    global FFF
    global Ent
    global Ent0
    global Ent1
    global Ent2
    global Ent3

    FF = Frame(root,bg='whitesmoke',bd=2,relief=GROOVE)
    FF.place(x=5,y=240,width=215,height=300)
    title2 = Label(FF,text='Table-Column',fg='black',bg='#FF6363',height=2)
    title2.pack(fill=X)

    Lab = Label(FF,text='DB-Name :',fg='green')
    Lab.place(x=2,y=50)
    Ent = Entry(FF)
    Ent.place(x=80,y=50)

    Lab0 = Label(FF,text='Table-Name :',fg='red')
    Lab0.place(x=2,y=80)
    Ent0 = Entry(FF)
    Ent0.place(x=80,y=80)

    Lab1 = Label(FF,text='Col-Name :',fg='green')
    Lab1.place(x=2,y=110)
    Ent1 = Entry(FF)
    Ent1.place(x=80,y=110)

    Lab2 = Label(FF,text='Col-Type :')
    Lab2.place(x=2,y=140)
    Ent2 = Entry(FF)
    Ent2.place(x=80,y=140)

    Lab3 = Label(FF,text='Col-Lenght :')
    Lab3.place(x=2,y=170)
    Ent3 = Entry(FF)
    Ent3.place(x=80,y=170)

    b = Button(FF,text='Create Table and Add Column',cursor='hand2',fg='black',bg='#FFEBC1',bd=1,relief=SOLID,command=Create_Table)
    b.place(x=10,y=210,width=190,height='60')

def Col1():
  
    FFF = Frame(root,bg='whitesmoke',bd=2,relief=GROOVE)
    FFF.place(x=222,y=240,width=215,height=300)
    title2 = Label(FFF,text='New-Columns',fg='black',bg='#FF6363',height=2)
    title2.pack(fill=X)

    Lab = Label(FFF,text='DB-Name :',fg='green')
    Lab.place(x=2,y=50)
    Ent = Entry(FFF)
    Ent.place(x=80,y=50)

    Lab0 = Label(FFF,text='Table-Name :',fg='red')
    Lab0.place(x=2,y=80)
    Ent0 = Entry(FFF)
    Ent0.place(x=80,y=80)

    Lab1 = Label(FFF,text='Col-Name :',fg='green')
    Lab1.place(x=2,y=110)
    Ent1 = Entry(FFF)
    Ent1.place(x=80,y=110)

    Lab2 = Label(FFF,text='Col-Type :')
    Lab2.place(x=2,y=140)
    Ent2 = Entry(FFF)
    Ent2.place(x=80,y=140)

    Lab3 = Label(FFF,text='Col-Lenght :')
    Lab3.place(x=2,y=170)
    Ent3 = Entry(FFF)
    Ent3.place(x=80,y=170)

    b = Button(FFF,text='Add new Columns',cursor='hand2',fg='black',bg='#FFEBC1',bd=1,relief=SOLID,command=add_colls)
    b.place(x=10,y=210,width=190,height='60')

def Create_Table():
    import mysql.connector
    from tkinter import messagebox
    db = Ent.get()
    tbname = Ent0.get()
    col_name = Ent1.get()
    col_type = Ent2.get()
    col_lenght = Ent3.get()
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = db
        )
        mycur = conn.cursor()
        mycur.execute('CREATE TABLE {} ({} {} ({}))'.format(tbname,col_name,col_type,col_lenght))
        messagebox.showinfo('DB {System}','Create Table Done')
    except mysql.connector.Error as r:
        messagebox.showerror('DB [System]',r)


import mysql.connector
from tkinter import messagebox

def add_colls():
    db = Ent.get()
    tbname = Ent0.get()
    col_name = Ent1.get()
    col_type = Ent2.get()
    #col_length = Ent3.get()

    try:
        # Establishing the connection
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database=db
        )
        mycur = conn.cursor()
        
        # Forming the correct SQL statement
        # It's assumed col_type is something like 'VARCHAR' or 'INT' and col_length is an integer or empty
        
        sql = f"ALTER TABLE {tbname} ADD COLUMN {col_name} {col_type})"
       
        #sql = f"ALTER TABLE {tbname} ADD COLUMN {col_name} {col_type}"
        
        # Executing the SQL statement
        mycur.execute(sql)
        
        # Committing changes
        conn.commit()
        
        # Inform the user
        messagebox.showinfo('DB System', 'Column added successfully')
    except mysql.connector.Error as e:
        # Error handling
        print(e)
        messagebox.showerror('DB System', str(e))
    finally:
        # Closing the cursor and connection
        if mycur:
            mycur.close()
        if conn:
            conn.close()




# def add_colls():
#     import mysql.connector
#     from tkinter import messagebox
#     db = Ent.get()
#     tbname = Ent0.get()
#     col_name = Ent1.get()
#     col_type = Ent2.get()
#     #col_lenght = Ent3.get()
#     try:
#         conn = mysql.connector.connect(
#             host = 'localhost',
#             user = 'root',
#             password = '',
#             database = db
#         )
#         mycur = conn.cursor()
#         mycur.execute('ALTER TABLE  {} ADD COLUMN {} {} '.format(tbname,col_name,col_type))
#         messagebox.showinfo('DB {System}','Create Columns Done')
#     except mysql.connector.Error as r:
#         print(r)
#         messagebox.showerror('DB [System]',r)

    
F1 = Frame(root,bg='whitesmoke',bd=2,relief=GROOVE)
F1.place(x=5,y=40,width=300,height=190)

title2 = Label(F1,text='Database Controlls_bolly',fg='white',bg='#5534A5',font=('Tajawal',15))
title2.pack(fill=X)

#============== show databases =============

L = Label(F1,text='Show DBS :')
L.place(x=10,y=50)

botton1 = Button(F1,text='All databases',cursor='hand2',command=
show_dbs)
botton1.place(x=100,y=47,width=125)

button2 = Button(F1,text='Hide',bg='#F4DFBA',cursor='hand2')
button2.place(x=230,y=47,width=60)

#============== DB name===============

L1 = Label(F1,text='DB name :')
L1.place(x=10,y=80)

En1 = Entry(F1)
En1.place(x=100,y=80)

b1 = Button(F1,text='Create',bg='#F4DFBA',cursor='hand2',command=DBcreate)
b1.place(x=230,y=78,width=60)

#============== tables ===============

L3 = Label(F1,text='Table-Cols :')
L3.place(x=10,y=110)

botton = Button(F1,text='Create Table',cursor='hand2')
botton.place(x=100,y=107,width=125)

botton1 = Button(F1,text='Hide',bg='#F4DFBA',cursor='hand2')
botton1.place(x=230,y=107,width=60)

#============= Columns=========

L3 = Label(F1,text='Add-Cols :')
L3.place(x=10,y=140)

botton = Button(F1,text='Add-Columns',cursor='hand2')
botton.place(x=100,y=137,width=125)

botton1 = Button(F1,text='Hide',bg='#F4DFBA',cursor='hand2')
botton1.place(x=230,y=137,width=60)

#=============  F2=========
 
FF1 = Frame(root,bg='whitesmoke',bd=2,relief=GROOVE)
FF1.place(x=310,y=40,width=300,height=190)

title2 = Label(FF1,text='Database Conect',fg='white',bg='#5534A5',font=('Tajawal',15))
title2.pack(fill=X)

#========== server =====

LL1 = Label(FF1,text='Server name :')
LL1.place(x=10,y=50)

Enn1 = Entry(FF1)
Enn1.place(x=100,y=50)
#========= User========

LL2 = Label(FF1,text='User name :')
LL2.place(x=10,y=80)
Enn2 = Entry(FF1)
Enn2.place(x=100,y=80)

#========= Password=========

LL3 = Label(FF1,text='Password :')
LL3.place(x=10,y=110)
Enn3 = Entry(FF1)
Enn3.place(x=100,y=110)

#============ button connect==========

botton_coonect = Button(FF1,text='Connect',fg='black',bg='#FFEBC1',bd=1,relief=SOLID,cursor='hand2',command=DB_Connect)
botton_coonect.place(x=227,y=49,width=65,height=80)


LL4 = Label(FF1,text='Test to connect the Server',fg='blue')
LL4.place(x=10,y=156)

logo = PhotoImage(file='images/logo2.png')
logolabel = Label(root,image=logo)
logolabel.place(x=615,y=40,width=390,height=500)

Col1()
Col()
root.mainloop()