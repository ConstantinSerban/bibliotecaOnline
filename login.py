from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sys
sys.path.append(r"venv\Lib\site-packages")
import pymysql
from main_user import pagina_u
from main_admin import pagina_p
from PIL import Image

root = Tk()
root.geometry("600x500")
root.title("Biblioteca online")
root.iconbitmap("book.ico")

background_image = Image.open("biblio.jpg")
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(1, 1, image=img)
Canvas1.pack(expand=True, fill=BOTH)

# def resize_image(e):
#     global image,resized,image2
#     image = Image.open("biblio.jpg")
#     # resized = image.resize((e.width,e.height), image.ANTIALAIS)
#     from PIL import Image  # make sure this is imported at the top
#     resized = image.resize((e.width, e.height), Image.ANTIALIAS)

#     image2 = ImageTk.PhotoImage(resized)
#     Canvas1.create_image(0, 0, image=image2)


def resize_image(e):
    global image, resized, image2
    image = Image.open("biblio.jpg")
    resized = image.resize((e.width, e.height), Image.Resampling.LANCZOS)  # ✅ Correct resampling constant
    image2 = ImageTk.PhotoImage(resized)
    Canvas1.create_image(0, 0, image=image2)


headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.08)
headingLabel = Label(headingFrame1, text="Biblioteca online", bg='black', fg='white', font=('Courier', 16))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=0.9)

mypass = "password"
mydatabase = "BiblioOnline"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

def inreg_user():
    username_info = username.get()
    password_info = password.get()
    password2_info = password2.get()
    userTable = "cont"

    if len(username_info) > 0 and len(password_info) > 0 and len(password2_info) > 0:
        if password_info == password2_info:
            insertUser = "insert into " + userTable + " (utilizator, parola) values ('" + username_info + "', '" + password_info + "')"
            try:
                cur.execute(insertUser)
                con.commit()
                messagebox.showinfo('Succes', "Cont creat cu succes!")
            except:
                messagebox.showerror('Eroare', "Contul nu a fost creat cu succes!")
        else:
            messagebox.showerror('Eroare', "Parolele trebuie sa coincida!")
    else:
        messagebox.showerror('Eroare', "Username-ul sau parola nu sunt valide!")

def con_verif():
    username1 = username_verify.get()
    password1 = password_verify.get()
    userTable = "cont"
    if len(username1) > 0 and len(password1) > 0:
        getUser = "select utilizator, parola, tip from " + userTable + " where utilizator = '" + username1 + "' and parola = '" + password1 + "'"
        try:
            cur.execute(getUser)
            con.commit()
            userData = cur.fetchall()
            if not userData:
                messagebox.showerror('Eroare', "Datele sunt incorecte!")
            else:
                if userData[0][2] == 0:
                    messagebox.showinfo('Succes', userData[0][0] + " conectat cu succes!")
                    root.destroy()
                    pagina_u(userData[0][0])
                else:
                    messagebox.showinfo('Succes', "Admin conectat cu succes!")
                    root.destroy()
                    pagina_p()
        except:
            messagebox.showerror('Eroare', "Cont inexistent!")
    else:
        messagebox.showerror('Eroare', "Username-ul sau parola invalide!")

def conectare():
    global screen2
    screen2 = Toplevel(root)
    screen2.title("Conectare")
    screen2.geometry("400x250")
    Label(screen2, text="").pack()
    Label(screen2, text="Introduceti datele de conectare: ").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Utilizator ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify).pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Parola ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify, show="*").pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Conectare", width=10, height=1, command=con_verif).pack()


def inregistrare():
    screen1 = Toplevel(root)
    screen1.title("Inregistrare")
    screen1.geometry("400x250")
    global username
    global password
    global password2
    global username_entry
    global password_entry
    global password2_entry
    username = StringVar()
    password = StringVar()
    password2 = StringVar()
    Label(screen1, text="").pack()
    Label(screen1, text="Utilizator ").pack()
    username_entry = Entry(screen1, textvariable=username).pack()
    Label(screen1, text="Parola ").pack()
    password_entry = Entry(screen1, textvariable=password, show="*").pack()
    Label(screen1, text="Repeta parola ").pack()
    password2_entry = Entry(screen1, textvariable=password2, show="*").pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Inregistrare", width=10, height=1, command=inreg_user).pack()

def createAdminUserFunction():
    global username
    nume = username.get()
    userTable = "cont"
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

    userTable = "cont"
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


def main_screen():
    global root
    root = Tk()
    root.title("Biblioteca online")
    root.geometry("600x400")

    Label(text="Biblioteca online", bg="grey", width="300", height="2", font=("Calibri", 15)).pack()
    Label(text="").pack()

    Canvas2 = Canvas(root)
    Canvas2.config(bg="#12a4d9")
    Canvas2.pack(expand=True, fill=BOTH)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)
    y = 0.1
    y_header = 0.1

headingLabel2 = Label(root, text="Pentru a putea utiliza aplicatia trebuie sa \nva inregistrati in baza de date, iar apoi sa \nva conectati cu contul creat. Dupa aceste \netape veti avea acces la urmatoarele comenzi:\nvizualizarea listei tuturor cartilor,\n imprumutarea si returnarea unei carti.", bg='black', fg='white', font=('Courier', 12))
headingLabel2.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.35)

btn_con = Button(root, text="Conectare", bg='black', fg='white', command=conectare)
btn_con.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)
btn_inreg = Button(root, text="Inregistrare", bg='black', fg='white', command=inregistrare)
btn_inreg.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

root.bind("<Configure>",resize_image)
root.mainloop()
main_screen()

