from tkinter import *
from PIL import ImageTk, Image
import sys
sys.path.append(r"venv\Lib\site-packages")
import pymysql
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

mypass = "password"
mydatabase = "BiblioOnline"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

def resize_image(e):
    global image, resized, image2
    image = Image.open("biblio.jpg")
    resized = image.resize((e.width, e.height), Image.Resampling.LANCZOS)  # ✅ FIXED
    image2 = ImageTk.PhotoImage(resized)
    Canvas1.create_image(0, 0, image=image2, anchor=NW)  # optional: use anchor to align correctly

def pagina_u(username):
    global Canvas1, img
    root = Tk()
    root.title("Biblioteca online")
    root.iconbitmap("book.ico")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    background_image = Image.open("biblio.jpg")
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)
    Canvas1.create_image(0, 0, image=img, anchor=NW)
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.08)

    headingLabel = Label(headingFrame1, text="Biblioteca Online", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=0.9)

    headingLabel2 = Label(root, text="Bine ai venit " + username + "! ", bg='black', fg='white', font=('Courier', 12))
    headingLabel2.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

    btn1 = Button(root, text="Vezi lista cartilor", bg='black', fg='white', command=View)
    btn1.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="Rezerva carte", bg='black', fg='white', command=issueBook)
    btn2.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    btn3 = Button(root, text="Returneaza carte", bg='black', fg='white', command=returnBook)
    btn3.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

    root.bind("<Configure>", resize_image)
    root.mainloop()
