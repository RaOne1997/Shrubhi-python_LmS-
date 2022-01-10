from tkinter import *
from tkinter import ttk, messagebox

import pymysql
from PIL import ImageTk


class Issu:
    def __init__(self, roots):
        self.root = roots
        self.root.title("LMS")
        self.root.geometry("1350x700+0+0")
        # ==bg image===
        self.bg = ImageTk.PhotoImage(file="image/How To Add a Background Image to the Top Section of Your Webpage.png")
        Label(self.root, image=self.bg).place(x=0, y=0)
        # =====frame1=======
        self.frame1 = Frame(self.root, bd=4, relief=RIDGE)
        self.frame1.place(x=600, y=54, width=700, height=500)
        # =====frame2==========
        frame2 = Frame(self.root, bg="red", bd=4, relief=RIDGE)
        frame2.place(x=100, y=54, width=400, height=600)
        # =====frame3==========
        frame3 = Frame(self.root, bg="red", bd=4, relief=RIDGE)
        frame3.place(x=100, y=590, width=400, height=70)
        # -----------------------1
        Label(frame2, text="Roll No", font=("rockwell", 15, "bold"), bg="red", fg="white").place(
            x=10, y=20)
        self.roll = Entry(frame2, font=("rockwell", 15), bg="whitesmoke", bd=0, fg="black")
        self.roll.place(x=10, y=50)

        Label(frame2, text="Student Name", font=("rockwell", 15, "bold"), bg="red", fg="white").place(
            x=10, y=80)
        self.sname = Entry(frame2, font=("rockwell", 15), bg="whitesmoke", fg="black")
        self.sname.place(x=10, y=110)
        # --------------------------------------2
        Label(frame2, text="BookID", font=("rockwell", 15, "bold"), bg="red",
              fg="white").place(x=10, y=140)
        self.BookID = Entry(frame2, font=("rockwell", 15), bg="whitesmoke", fg="black")
        self.BookID.place(x=10, y=170)

        Label(frame2, text="Book Name", font=("rockwell", 15, "bold"), bg="red", fg="white").place(x=10, y=200)
        self.bookname = Entry(frame2, font=("rockwell ", 15), bg="whitesmoke", fg="black")
        self.bookname.place(x=10, y=230)

        Label(frame2, text="Volume", font=("rockwell", 15, "bold"), bg="red", fg="white").place(x=10, y=260)
        self.valu = Entry(frame2, font=("rockwell ", 15), bg="whitesmoke",  fg="black")
        self.valu.place(x=10, y=290)

        # --------------------------------------3
        Label(frame2, text="Date of Issue", font=("rockwell", 15, "bold"), bg="red",
              fg="white").place(x=10, y=320)
        self.DOI = Entry(frame2, font=("rockwell", 15), bg="whitesmoke", fg="black")
        self.DOI.place(x=10, y=350)

        Label(frame2, text="Date of Return", font=("rockwell", 15, "bold"), bg="red",
              fg="white").place(x=10, y=380)
        self.DOR = Entry(frame2, font=("rockwell", 15), bg="whitesmoke", fg="black", )
        self.DOR.place(x=10, y=410)
        # -------------------button
        self.add = Button(frame3, text="Rrturn book",  font=("rockwell", 10),command=self.delete, bg="blue", fg="white")
        self.add.place(x=1, y=10)

        self.delt = Button(frame3, text="Search Book ", command=self.Search, font=("rockwell", 10), bg="blue",
                           fg="white")
        self.delt.place(x=160, y=10)
        self.search = Button(frame3, text="Clear ", command=self.cler, font=("rockwell", 10), bg="blue",
                             fg="white")
        self.search.place(x=270, y=10)

        # -------------------------------back button
        self.bg1 = ImageTk.PhotoImage(file="image/Untitled-1.jpg")
        Button(self.root, image=self.bg1, bd=0, command=self.homep).place(x=5, y=6)

        # def test(self):

        # =======tabl
        scroll_x = Scrollbar(self.frame1, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.frame1, orient=VERTICAL)
        self.tv = ttk.Treeview(self.frame1, columns=(1, 2, 3, 4, 5, 6, 7), xscrollcommand=scroll_x.set,
                               yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.tv.xview)
        scroll_y.config(command=self.tv.yview)
        self.tv.heading(1, text="Book ID")
        self.tv.heading(2, text="Book Name")
        self.tv.heading(3, text="ROll NO")
        self.tv.heading(4, text="Student Name")
        self.tv.heading(5, text="Volume")
        self.tv.heading(6, text="DOI")
        self.tv.heading(7, text="DOR")

        self.tv['show'] = "headings"
        self.tv.column(1, width=100)
        self.tv.column(2, width=140)
        self.tv.column(3, width=140)
        self.tv.column(4, width=200)
        self.tv.column(5, width=100)
        self.tv.column(6, width=150)
        self.tv.column(7, width=100)
        self.tv.pack(fill=BOTH, expand=1)
        self.fatchtabel()

    def fatchtabel(self):
        conn = pymysql.connect(host="localhost", user="root", password="", database="py_invmanag")
        cur = conn.cursor()
        cur.execute("select * from issuebook ")
        row = cur.fetchall()
        if len(row) != 0:
            self.tv.delete(*self.tv.get_children())
            for rows in row:
                self.tv.insert('', END, value=rows)

            conn.commit()
        conn.close()

    def displayall(self):
        root.destroy()
        import table

    def cler(self):

        self.roll.delete(0, END),
        self.sname.delete(0, END),
        self.bookname.delete(0, END),
        self.BookID.delete(0, END),
        self.valu.delete(0,END),
        self.DOR.delete(0, END),
        self.DOI.delete(0, END)

    # def add(self):
    #     if self.roll.get() == "" or self.sname.get() == "" or self.bookname.get() == "" \
    #             or self.BookID.get() == "" \
    #             or self.valu.get() == "" or self.DOI.get() == "" or self.DOR.get() == "":
    #         #   :
    #         messagebox.showerror("error", "All filds are required", parent=self.root)
    #
    #     else:
    #         try:
    #             conn = pymysql.connect(host="localhost", user="root", password="", database="py_invmanag")
    #             cur = conn.cursor()
    #
    #             cur.execute(
    #                 "INSERT INTO `issuebook`(roll,Sname,rollname,sname,Volume,DOI,DOR) VALUES (%s,%s,%s,"
    #                 "%s,%s,%s,%s)",
    #                 (self.roll.get(),
    #                  self.Sname.get(),
    #                  self.BookID.get(),
    #                  self.sname.get(),
    #                  self.valu.get(),
    #                  self.DOI.get(),
    #                  self.DOR.get(),
    #
    #                  ))
    #             conn.commit()
    #             conn.close()
    #             self.fatchtabel()
    #             messagebox.showinfo("success", "Issue book", parent=self.root)
    #             self.cler()
    #         except EXCEPTION as es:
    #             messagebox.showerror("error", f"Error due to exception:{str(es)}", parent=self.root)

    def delete(self):
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="py_invmanag")
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM `issuebook` WHERE `rollname`= %s",
                (self.roll.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("success", "RECORD Delete", parent=self.root)

            self.cler()
            self.fatchtabel()
            conn.commit()
            conn.close()

        except:
           print("hk")

    def Search(self):

        if self.roll.get() == "":

            messagebox.showerror("error", "roll  required", parent=self.root)
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="", database="py_invmanag")
                cur = conn.cursor()
                cur.execute("select * from issuebook where  rollname=%s", self.roll.get())
                row = cur.fetchone()
                self.BookID.insert(0,row[0])
                self.sname.insert(0,row[1])
                self.bookname.insert(0, row[3])
                self.valu.insert(0, row[4])
                self.DOI.insert(0, row[5])
                self.DOR.insert(0, row[6])

                conn.commit()
                conn.close()



            except:
                messagebox.showerror("Error", "NO RECORD Found", parent=self.root)
                self.cler()

                        # def update(self):
                        #     if self.BookID.get() == "":
                        #         #   :
                        #         messagebox.showerror("error", "Student Roll No required", parent=self.root)
                        #     else:
                        #         try:
                        #             conn = pymysql.connect(host="localhost", user="root", password="", database="py_invmanag")
                        #             cur = conn.cursor()
                        #             cur.execute("select * from studinfo where  id=%s", self.BookID.get())
                        #             row = cur.fetchone()
                        #             self.Sname.insert(0, row[1] + "  " + row[2])
                        #
                        #             conn.commit()
                        #             conn.close()
                        #
                        #
                        #
                        #         except:
                        #             messagebox.showerror("Error", "NO RECORD Found", parent=self.root)
                        #             self.cler()

    def homep(self):
        root.destroy()
        import home


root = Tk()

obj = Issu(root)
root.mainloop()
