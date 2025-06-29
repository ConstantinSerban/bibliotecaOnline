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


allBid = []

def returnn():
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status
    
    bid = bookInfo1.get()

    extractBid = "select Bid from "+issueTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            print(i[0])
            allBid.append(i[0])
        if bid in allBid:
            checkAvail = "select Status from "+bookTable+" where Bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
            if check == 'rezervata':
                status = True
            else:
                status = False
        else:
            messagebox.showerror("Eroare","Nu se gaseste ID-ul cartii!")
    except:
        messagebox.showerror("Erare","Nu se poate lua ID-ul cartii!")

    issueSql = "delete from "+issueTable+" where Bid = '"+bid+"'"
  
    print(bid in allBid)
    print(status)
    updateStatus = "update "+bookTable+" set Status = 'disp' where Bid = '"+bid+"'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Sucess',"Carte returnata cu succes!")
        else:
            allBid.clear()
            messagebox.showinfo('Mesaj',"Verifica ID")
            root.destroy()
            return
    except:
        messagebox.showerror("Eroare cautare","Datele introduse sunt gresite. Incearca din nou.")

    allBid.clear()
    root.destroy()
    
def returnBook(): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
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
        
    headingLabel = Label(headingFrame1, text="Returneaza carte", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   

    lb1 = Label(labelFrame,text="ID carte : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)

    SubmitBtn = Button(root,text="Returneaza",bg='#d1ccc0', fg='black',command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Iesire",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()