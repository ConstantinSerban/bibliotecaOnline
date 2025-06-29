from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sys
sys.path.append(r"venv\Lib\site-packages")
import pymysql

mypass = "password"
mydatabase="BiblioOnline"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

issueTable = "books_issued" 
bookTable = "books"

allBid = [] 

def issue():
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status,idNotFound

    idNotFound = False
    bid = inf1.get()
    issueto = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

    extractBid = "select Bid from "+bookTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])
        if bid in allBid:
            checkAvail = "select Status from " + bookTable + " where Bid = '" + bid + "'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
            if check == 'disp':
                status = True
            else:
                status = False
        else:
            messagebox.showerror("Eroare","ID-ul cartii nu se regaseste")
            idNotFound = True
            root.destroy()
    except:
        messagebox.showerror("Eroare","Nu se poate imprumuta!")

    if not idNotFound:
        issueSql = "insert into "+issueTable+" (Bid, Issueto) values ('"+bid+"','"+issueto+"')"
        show = "select * from "+issueTable

        updateStatus = "update "+bookTable+" set Status = 'rezervata' where Bid = '"+bid+"'"
        try:
            if bid in allBid and status == True:
                cur.execute(issueSql)
                con.commit()
                cur.execute(updateStatus)
                con.commit()
                messagebox.showinfo('Succes',"Carte rezervata cu succes")
                root.destroy()
            else:
                allBid.clear()
                messagebox.showinfo('Mesaj',"Cartea a fost deja imprumutata")
                root.destroy()
                return
        except:
            messagebox.showinfo("Eroare la cautare","Datele introduse sunt gresite. Incearca din nou.")

    allBid.clear()
    
def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Biblioteca online")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    root.iconbitmap("book.ico")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Rezerva carte", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  

    lb1 = Label(labelFrame,text="ID carte : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)

    lb2 = Label(labelFrame,text="Rezervata de : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)

    issueBtn = Button(root,text="Rezerva",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Iesire",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()