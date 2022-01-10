from tkinter import *
from tkinter import messagebox

import pymysql
from PIL import ImageTk


class login:
    def __init__(self, root):

        self.root = root
        self.root.title("Login  windows")
        self.root.geometry("1380x700+100+0")
        self.root.resizable(False,False)

        # ==bg image===

        self.bg = ImageTk.PhotoImage(file="image/1900851.png")
        bg = Label(self.root, image=self.bg).place(x=-160, y=-200)

        self.lbl_result1 = Label(root, text="", font=('arial', 18))
        self.lbl_result1.grid(row=3, columnspan=2)
        # == regrister ===

        titleF = Button(root, text=" Click here for Register ",command=self.regpage,  font=("rockwell", 10, "bold"),bd=0, bg="#608A61",fg="black")
        titleF.place( x=600, y=510)
        # ==login btun
        but_reg = Button(root, text="LOGIN", command=self.demo, bd=0, cursor="hand2",
                         font=("rockwell", 15, "bold"),
                         bg="#608A61", ).place(x=600, y=580, width="100", height="30")

        # root .wm_attributes('-transparentcolor', 'white')

        # == Entry field for Username
        Label(root, text="Username/Email", font=("rockwell", 15), bg="#608A61").place(x=500, y=270)
        self.username = Entry(root, text="First name", font=("rockwell", 15), bg="#608A61", fg="black",
                              width=30)
        self.username.place(x=500, y=300)

        # == Entry field for Password
        Label(root,text="Password",font=("rockwell", 15),bg="#608A61").place(x=500, y=350)
        self.passw = Entry(root, show="*", font=("rockwell", 15), bg="#608A61", fg="black", width=30)
        self.passw.place(x=500, y=380)

        # ==display userpass
    def regpage(self):
        self.root.destroy()
        import register


    def demo(self):
        if self.username.get() == "" or self.passw.get() == "":
            messagebox.showerror("error", "All fields are required ", parent=self.root)

        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="", database="py_invmanag")
                cur = conn.cursor()
                cur.execute("select * from regristration where email = %s and password = %s",
                            (self.username.get(), self.passw.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("error", "invalid username and password", parent=self.root)
                else:
                    messagebox._show("wef", "success", parent=self.root)
                    self.homep()
                    conn.close()

            except EXCEPTION as es:
                messagebox.showerror("error", f"Error due to exception:{str(es)}", parent=self.root)
    def homep(self):
        root.destroy()
        import home
root = Tk()

obj = login(root)
root.mainloop()
