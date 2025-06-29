from tkinter import *
from PIL import ImageTk,Image
import sys
sys.path.append(r"venv\Lib\site-packages")
# sys.path.append(r"D:\Projects\Python\Mircea_licenta\Biblioteca\venv\Lib\site-packages\pymysql")
import pymysql
from AddBook import *
from CreateAdmin import createAdminUser
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from DeleteUser import *

mypass = "password"
mydatabase = "BiblioOnline"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

def resize_image(e):
    global image,resized,image2
    image = Image.open("biblio.jpg")
    resized = image.resize((e.width,e.height), image.ANTIALAIS)

    image2 = ImageTk.PhotoImage(resized)
    Canvas1.create_image(3, 3, image=image2)

def pagina_p():
    global Canvas1
    root = Tk()
    root.title("Biblioteca online")
    root.iconbitmap("book.ico")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    background_image = Image.open("biblio.jpg")

    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)

    Canvas1.create_image(500, 540, image=img)
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.08)

    headingLabel = Label(headingFrame1, text="Biblioteca Online", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=0.9)

    headingLabel2 = Label(root, text="Bine ai venit in contul de admin!", bg='black', fg='white', font=('Courier', 11))
    headingLabel2.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

    btn1 = Button(root,text="Adauga carte",bg='black', fg='white', command=addBook)
    btn1.place(relx=0.28,rely=0.27, relwidth=0.45,relheight=0.1)

    btn2 = Button(root,text="Sterge carte",bg='black', fg='white', command=delete)
    btn2.place(relx=0.28,rely=0.37, relwidth=0.45,relheight=0.1)

    btn3 = Button(root,text="Vezi lista cartilor",bg='black', fg='white', command=View)
    btn3.place(relx=0.28,rely=0.47, relwidth=0.45,relheight=0.1)

    btn4 = Button(root,text="Rezerva carte",bg='black', fg='white', command=issueBook)
    btn4.place(relx=0.28,rely=0.57, relwidth=0.45,relheight=0.1)

    btn5 = Button(root,text="Returneaza carte",bg='black', fg='white', command=returnBook)
    btn5.place(relx=0.28,rely=0.67, relwidth=0.45,relheight=0.1)

    btn6 = Button(root, text="Sterge cont", bg='black', fg='white', command=delete1)
    btn6.place(relx=0.28, rely=0.77, relwidth=0.45, relheight=0.1)

    btn7 = Button(root, text="Creare admin", bg='black', fg='white', command=createAdminUser)
    btn7.place(relx=0.28, rely=0.87, relwidth=0.45, relheight=0.1)

    root.bind("<Configure>",resize_image)
    root.mainloop()