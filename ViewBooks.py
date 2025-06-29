import tkinter
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox, ttk
import sys
sys.path.append(r"venv\Lib\site-packages")
import pymysql

mypass = "password"
mydatabase="BiblioOnline"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

bookTable = "books" 

def View(): 
    
    root = Tk()
    root.title("Biblioteca online")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    root.iconbitmap("book.ico")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Vezi lista cartilor", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.05,rely=0.3,relwidth=0.9,relheight=0.5)
    y = 0.25
    y_header = 0.1

    Label(labelFrame, text='ID', bg='black', fg='white').place(relx=0.07, rely=y_header)
    Label(labelFrame, text='Titlul', bg='black', fg='white').place(relx=0.22, rely=y_header)
    Label(labelFrame, text='Autor', bg='black', fg='white').place(relx=0.54, rely=y_header)
    Label(labelFrame, text='Stare', bg='black', fg='white').place(relx=0.83, rely=y_header)
    Label(labelFrame, text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", bg='black',fg='white').place(relx=0.0,rely=0.2)

    getBooks = "select Bid, Title, Author, Status from "+bookTable

    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            if len(i[1]) > 25:
                title = i[1][0:25] + "..."
            else:
                title = i[1]
            if len(i[2]) > 20:
                author = i[2][0:20] + "..."
            else:
                author = i[2]
            Label(labelFrame, text=i[0], bg='black', fg='white').place(relx=0.07, rely=y)
            Label(labelFrame, text=title, bg='black', fg='white').place(relx=0.22, rely=y)
            Label(labelFrame, text=author, bg='black', fg='white').place(relx=0.54, rely=y)
            Label(labelFrame, text=i[3], bg='black', fg='white').place(relx=0.83, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Nu exista nicio carte in biblioteca.")
    
    quitBtn = Button(root,text="Iesire",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()