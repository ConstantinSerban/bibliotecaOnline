from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

mypass = "password"
mydatabase = "BiblioOnline"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

userTable = "cont"

def createAdminUserFunction():
    global username
    nume = username.get()

    createAdminUser = "update " +userTable+ " set tip = '1' where utilizator = '" + nume + "'"
    try:
        c=cur.execute(createAdminUser)
        con.commit()
        if c==1:
            messagebox.showinfo('Success', nume + " a devenit admin!")
        else:
            messagebox.showerror('Eroare', "Utilizatorul nu exista. Incearca din nou.")
    except:
        messagebox.showerror('Eroare', "Utilizatorul nu exista. Incearca din nou.")

    username.delete(0, END)
    root.destroy()

def createAdminUser():
    global username, Canvas1, con, cur, userTable, root

    root = Tk()
    root.title("Biblioteca online")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    root.iconbitmap("book.ico")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#FF4040")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Creaza admin", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    lb2 = Label(labelFrame, text="Utilizator : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    username = Entry(labelFrame)
    username.place(relx=0.3, rely=0.5, relwidth=0.62)

    SubmitBtn = Button(root, text="Make Admin", bg='#d1ccc0', fg='black', command=createAdminUserFunction)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Iesire", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()