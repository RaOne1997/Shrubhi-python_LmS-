from tkinter import *
from tkinter import ttk, messagebox

import pymysql
from PIL import ImageTk


class home:
    def __init__(self, root):
        self.root = root
        self.root.title("LMS")
        self.root.geometry("1350x700+0+0")

        # ==bg image===

        self.bg = ImageTk.PhotoImage(file="image/How To Add a Background Image to the Top Section of Your Webpage.png")
        bg = Label(self.root, image=self.bg).place(x=0, y=0)
        # ----------------frame
        frame1 = Frame(self.root)
        frame1.place(x=600, y=54, width=700, height=500)
        #=========logoutbtn
        bgs = Button(root, text="Logout", bd=0,bg="#dfaa11",fg="black",command=self.logout ,font=("rockwell", 10)).place(x=1200, y=10)

        #--------------ADDstudent
        bgs = Button(frame1, text="STUDENT", bd=0,bg="black",fg="white",command=self.studen ,font=("rockwell", 20)).place(x=50, y=100)
        # ----------------addBook
        ab = Button(frame1, text="BOOKS", bd=0, bg="black", fg="white",command=self.book, font=("rockwell", 20)).place(x=250, y=100)

    # ----------------addreturn
        ib = Button(frame1, text="ISSUE BOOK", bd=0, bg="black", fg="white",command=self.issu,font=("rockwell", 20)).place(x=450, y=100)
    # ----------------addstudent
        rb = Button(frame1, text="RETURN BOOK", bd=0, bg="black", fg="white", font=("rockwell", 20)).place(x=230,y=200)

    def logout(self):
        root.destroy()
        import login
    def studen(self):
        root.destroy()
        import studentrecord
    def book(self):
        root.destroy()
        import bookrecord
    def issu(self):
        root.destroy()
        import issuebook

root = Tk()

obj = home(root)
root.mainloop()
