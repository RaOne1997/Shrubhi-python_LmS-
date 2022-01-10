from tkinter import *
from tkinter import ttk, messagebox

import pymysql
from PIL import ImageTk


class addstudent:
    def __init__(self, roots):
        self.root = roots
        self.root.title("LMS")
        self.root.geometry("1350x700+0+0")
        # ==bg image===
        self.bg = ImageTk.PhotoImage(file="image/How To Add a Background Image to the Top Section of Your Webpage.png")
        Label(self.root, image=self.bg).place(x=0, y=0)
        # =====frame=======
        frame1 = Frame(self.root, bd=4, relief=RIDGE)
        frame1.place(x=600, y=54, width=700, height=500)
        # -----------------------1
        Label(frame1, text="First name", font=("rockwell", 15, "bold"), bg="white", fg="black").place(
            x=80, y=50)
        self.txt_fname = Entry(frame1, font=("rockwell", 15), bg="white", fg="black")
        self.txt_fname.place(x=80, y=80)

        Label(frame1, text="Last name", font=("rockwell", 15, "bold"), bg="white", fg="black").place(
            x=400, y=50)
        self.txt_Lname = Entry(frame1, font=("rockwell", 15), bg="white", fg="black")
        self.txt_Lname.place(x=400, y=80)
        # --------------------------------------2

        Label(frame1, text="Contact number", font=("rockwell", 15, "bold"), bg="white",
              fg="black").place(x=80, y=150)

        self.txt_Contact = Entry(frame1, font=("rockwell", 15), bg="white", fg="black")
        self.txt_Contact.place(x=80, y=180)

        Label(frame1, text="Email", font=("rockwell", 15, "bold"), bg="white", fg="black").place(
            x=400, y=150)
        self.txt_Email = Entry(frame1, font=("rockwell", 15), bg="white", fg="black")
        self.txt_Email.place(x=400, y=180)
        # --------------------------------------3
        Label(frame1, text="Class", font=("rockwell", 15, "bold"), bg="white",
                            fg="black").place(x=80, y=250)
        self.classa = ttk.Combobox(frame1, font=("new time roman", 15), state='readonly', justify='center')

        self.classa['value'] = ('select', 'MCA 1', 'MCA II','MCA III','MBA I','MBA II','MBA III')
        self.classa.place(x=80, y=280)
        self.classa.current(0)

        Label(frame1, text="Address", font=("rockwell", 15, "bold"), bg="white",
                             fg="black").place(x=400, y=250)
        self.Address = Entry(frame1, font=("rockwell", 15), bg="white", fg="black", )
        self.Address.place(x=400, y=280)
        # -------------------4
        Label(frame1, text="DOB", font=("rockwell", 15, "bold"), bg="white",
                         fg="black").place(x=80, y=320)
        self.DOB = Entry(frame1, font=("rockwell", 15), bg="white", fg="black", )
        self.DOB.place(x=80, y=350)

        self.Roll = Label(frame1, text="Roll-NO", font=("rockwell", 15, "bold"), bg="white",
                          fg="black").place(x=400, y=320)
        self.Roll = Entry(frame1, font=("rockwell", 15), bg="white", fg="black", )
        self.Roll.place(x=400, y=350)

        # ----------------------------BUttons
        self.add = Button(roots, text="ADD RECORD", command=self.add, font=("rockwell", 15), bg="white", fg="black")
        self.add.place(x=600, y=590)
        self.UPd = Button(roots, text="UPDATE RECORD", command=self.update, font=("rockwell", 15), bg="white",
                          fg="black")
        self.UPd.place(x=780, y=590)
        self.delt = Button(roots, text="DELETE RECORD", command=self.delete, font=("rockwell", 15), bg="white",
                           fg="black")
        self.delt.place(x=1000, y=590)
        self.search = Button(roots, text="SEARCH RECORD", command=self.search, font=("rockwell", 15), bg="white",
                             fg="black")
        self.search.place(x=750, y=650)

        self.showall = Button(roots, text="DISPLAY ALL", command=self.displayall, font=("rockwell", 15), bg="white",
                             fg="black")
        self.showall.place(x=950, y=650)

        #-------------------------------6
        Label(frame1, text="Gender", font=("new time roman", 15, "bold"), bg="white",
                      fg="black").place(x=80, y=400)
        self.GEN = ttk.Combobox(frame1, font=("new time roman", 15), state='readonly', justify='center')

        self.GEN['value'] = ('select', 'Male','Female')
        self.GEN.place(x=400, y=400)
        self.GEN.current(0)
        #=====================back button
        self.bg1 = ImageTk.PhotoImage(file="image/Untitled-1.jpg")
        Button(self.root, image=self.bg1,bd=0,command=self.homep).place(x=5, y=6)
    def homep(self):
        #root.destroy()
        import home
    def displayall(self):
        root.destroy()
        import table
    def cler(self):

        self.txt_fname.delete(0, END),
        self.txt_Lname.delete(0, END),
        self.txt_Contact.delete(0, END),
        self.txt_Email.delete(0, END),
        self.classa.current(0),
        self.Roll.delete(0, END),
        self.GEN.current(0),
        self.Address.delete(0, END)
        self.DOB.delete(0, END)

    def add(self):
        if self.txt_fname.get() == "" or self.txt_Lname.get() == "" or self.txt_Email.get() == "" \
                or self.txt_Contact.get() == "" \
                or self.Address.get() == "" or self.DOB.get() == "" or self.Roll.get() == "" or self.classa.get() == "":
            #   :
            messagebox.showerror("error", "All filds are required", parent=self.root)

        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="", database="py_invmanag")
                cur = conn.cursor()
                cur.execute("select * from studinfo where Email=%s or id=%s", (self.txt_Email.get(), self.Roll.get()))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("error", "Email or roll is already user", parent=self.root)

                else:
                    cur.execute(
                        "INSERT INTO `studinfo`(id,firstname,lastname,Email,contact,Address,Gender,class,DoB) VALUES (%s,%s,%s,"
                        "%s,%s,%s,%s,%s,%s)",
                        (self.Roll.get(),
                         self.txt_fname.get(),
                         self.txt_Lname.get(),
                         self.txt_Email.get(),
                         self.txt_Contact.get(),
                         self.Address.get(),
                         self.GEN.get(),
                         self.classa.get(),
                         self.DOB.get()
                         ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("success", "RECORD add", parent=self.root)
                    self.cler()
            except EXCEPTION as es:
                messagebox.showerror("error", f"Error due to exception:{str(es)}", parent=self.root)

    def search(self):
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="py_invmanag")
            cur = conn.cursor()
            cur.execute("select * from studinfo where  id=%s", self.Roll.get())
            row = cur.fetchone()
            self.txt_fname.insert(0, row[1])
            self.txt_Lname.insert(0, row[2])
            self.txt_Email.insert(0, row[3])
            self.txt_Contact.insert(0, row[4])
            self.Address.insert(0, row[5])
            self.GEN.set(row[6])
            self.classa.set(row[7])
            self.DOB.insert(0, row[8])
            conn.commit()
            conn.close()

        except:
            messagebox.showerror("Error", "NO Record found")

    def delete(self):
        if self.txt_fname.get() == "" or self.txt_Lname.get() == "" or self.txt_Email.get() == "" \
                or self.txt_Contact.get() == "" or self.Address.get() == "" or self.DOB.get() == "" \
                or self.Roll.get() == "" or self.classa.get() == "":

            messagebox.showerror("error", "All filds are required", parent=self.root)
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="", database="py_invmanag")
                cur = conn.cursor()
                cur.execute("select * from studinfo where  id=%s", self.Roll.get())
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("error", "Record is not available", parent=self.root)

                else:
                    cur.execute(
                        "DELETE FROM `studinfo` WHERE `id`= %s",
                        (self.Roll.get()))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("success", "RECORD Delete", parent=self.root)
                    self.cler()
            except EXCEPTION as es:
                messagebox.showerror("error", f"Error due to exception:{str(es)}", parent=self.root)

    def update(self):
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="py_invmanag")
            cur = conn.cursor()
            cur.execute("update studinfo set firstname=%s,lastname=%s,Email=%s,"
                        "contact=%s,Address=%s,Gender=%s,class=%s,DoB=%s WHERE id=%s ",
                        (
                            self.txt_fname.get(),
                            self.txt_Lname.get(),
                            self.txt_Email.get(),
                            self.txt_Contact.get(),
                            self.Address.get(),
                            self.GEN.get(),
                            self.classa.get(),
                            self.DOB.get(),
                            self.Roll.get()

                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("success", "RECORD Update", parent=self.root)
            self.cler()
        except EXCEPTION as es:
            messagebox.showerror("error", f"Error due to exception:{str(es)}", parent=self.root)


root = Tk()

obj = addstudent(root)
root.mainloop()
