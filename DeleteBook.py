from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "password"
mydatabase="BiblioOnline"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

issueTable = "books_issued" 
bookTable = "books"

def deleteBook():
    
    bid = bookInfo1.get()
    
    deleteSql = "delete from "+bookTable+" where Bid = '"+bid+"'"
    deleteIssue = "delete from "+issueTable+" where Bid = '"+bid+"'"
    try:
        d=cur.execute(deleteSql)
        con.commit()
        i=cur.execute(deleteIssue)
        con.commit()
        if d==1 or i==1:
            messagebox.showinfo('Succes',"Carte stearsa cu succes!")
        else:
            messagebox.showerror('Eroare', "Cartea nu se afla in biblioteca. Incearca din nou.")
    except:
        messagebox.showerror('Eroare',"Cartea nu se afla in biblioteca. Incearca din nou.")

    bookInfo1.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Biblioteca online")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    root.iconbitmap("book.ico")

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Sterge carte", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   

    lb2 = Label(labelFrame,text="ID carte : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)

    SubmitBtn = Button(root,text="Sterge",bg='#d1ccc0', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Iesire",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()