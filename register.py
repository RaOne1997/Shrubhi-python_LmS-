from tkinter import *
from tkinter import ttk, messagebox

import pymysql
from PIL import ImageTk


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Regristration windows")
        self.root.geometry("1350x700+0+0")

        # ==bg image===

        self.bg = ImageTk.PhotoImage(file="image/How To Add a Background Image to the Top Section of Your Webpage.png")
        bg = Label(self.root, image=self.bg).place(x=0, y=0)
        # ==left image===

        # self.left = ImageTk.PhotoImage(file="image/side.jpg")
        # left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500 )

        # ===Register form===

        frame1 = Frame(self.root)

        frame1.place(x=600, y=54, width=700, height=500)

        title = Label(frame1, text="Register Here", font=("new time roman", 20, "bold"), bg="white", fg="green").place(
            x=50, y=10)
        # --------------------1

        titleF = Label(frame1, text="First name", font=("new time roman", 15, "bold"), bg="white", fg="black").place(
            x=80, y=50)
        self.txt_fname = Entry(frame1, font=("new time roman", 15), bg="white", fg="black")
        self.txt_fname.place(x=80, y=80)

        titleL = Label(frame1, text="Last name", font=("new time roman", 15, "bold"), bg="white", fg="black").place(
            x=400, y=50)
        self.txt_Lname = Entry(frame1, font=("new time roman", 15), bg="white", fg="black")
        self.txt_Lname.place(x=400, y=80)
        # --------------------------------------2

        title_cont = Label(frame1, text="Contact number", font=("new time roman", 15, "bold"), bg="white",
                           fg="black").place(x=80, y=150)
        self.txt_Contact = Entry(frame1, font=("new time roman", 15), bg="white", fg="black")
        self.txt_Contact.place(x=80, y=180)

        title_email = Label(frame1, text="Email", font=("new time roman", 15, "bold"), bg="white", fg="black").place(
            x=400, y=150)
        self.txt_Email = Entry(frame1, font=("new time roman", 15), bg="white", fg="black")
        self.txt_Email.place(x=400, y=180)

        # --------------------------------------3

        Secuq = Label(frame1, text="Security Question", font=("new time roman", 15, "bold"), bg="white",
                      fg="black").place(x=80, y=250)
        self.cmb_ans = ttk.Combobox(frame1, font=("new time roman", 15), state='readonly', justify='center')

        self.cmb_ans['value'] = ('select', 'what is your pet name', 'what is your childwood name'
                            , 'what is your school name')
        self.cmb_ans.place(x=80, y=280)
        self.cmb_ans.current(0)

        ans = Label(frame1, text="Answer", font=("new time roman", 15), bg="white", fg="black").place(x=400, y=250)
        self.txt_Ans = Entry(frame1, font=("new time roman", 15), bg="white", fg='black')
        self.txt_Ans.place(x=400, y=280)
        # ------------------------------4
        passw = Label(frame1, text="Password", font=("new time roman", 15,), bg="white", fg="black").place(x=80, y=350)
        self.txt_pass = Entry(frame1, show='*', font=("new time roman", 15), bg="white")
        self.txt_pass.place(x=80, y=380)

        con_pass = Label(frame1, text="Confirmed Password", font=("new time roman", 15, "bold"), bg="white", fg="black").place(x=400, y=350)
        self.txt_con_pass = Entry(frame1, show='*', font=("new time roman", 15), bg="white")
        self.txt_con_pass.place(x=400, y=380)

        # -----------------------5
        #varible
        self.cheval=IntVar()
        chk = Checkbutton(root, text="agery traem and condution",variable=self.cheval, onvalue="1", offvalue="2", bg="#dfaa11",
                          font=("new time roman", 15), ).place(x=600, y=580)

        self.btn_img = ImageTk.PhotoImage(file="image/Register-Now-Button-300x96.png")
        but_reg = Button(root, image=self.btn_img, bd=0, cursor="hand2",
                         bg="#dfaa11", command=self.register_data).place(x=1000, y=580, width="300", height="60")
        #-------------------------6
        titleF = Button(frame1, text="Already account.....!",command=self.logp, font=("new time roman", 10, ),bd=0, bg="white", fg="red").place(x=550, y=450)
    def logp(self):
        self.root.destroy()
        import login
    def cler(self):

        self.txt_fname.delete(0,END),
        self.txt_Lname.delete(0,END),
        self.txt_Contact.delete(0,END),
        self.txt_Email.delete(0,END),
        self.cmb_ans.current(0),
        self.txt_Ans.delete(0,END),
        self.txt_pass.delete(0,END)
        self.txt_con_pass.delete(0,END)




    def register_data(self):
         if self.txt_fname.get()=="" or self.txt_Lname.get()=="" or self.txt_Email.get()=="" or self.txt_Contact.get()=="" or self.txt_Ans.get()=="" or self.txt_pass.get()=="" or self.txt_con_pass.get()=="" :
             messagebox.showerror("error", "All filds are required", parent=self.root)

         elif self.txt_pass.get()!=self.txt_con_pass.get():
             messagebox.askretrycancel("Password", "Password not match", parent=self.root)
         elif self.cheval.get()==0:
             messagebox.showerror("error", "please agery", parent=self.root)
         else :
           try:
                conn=pymysql.connect(host="localhost",user="root", password="", database="py_invmanag")
                cur=conn.cursor()
                cur.execute("select * from regristration where email=%s",self.txt_Email.get())
                row=cur.fetchone()
                if row!= None:
                    messagebox.showerror("error", "Email is already user", parent=self.root)
                else:
                     cur.execute("INSERT INTO `regristration`(first_name,last_name,contact,email,seq_que,sec_ans,password) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                                (    self.txt_fname.get(),
                                     self.txt_Lname.get(),
                                     self.txt_Contact.get(),
                                     self.txt_Email.get(),
                                     self.cmb_ans.get(),
                                     self.txt_Ans.get(),
                                     self.txt_pass.get()
                     ))
                     conn.commit()
                     conn.close()
                     messagebox.showinfo("success", "Register Successful", parent=self.root)
                     self.cler()
           except EXCEPTION as es:
            messagebox.showerror("error",f"Error due to exception:{str(es)}", parent=self.root)








root = Tk()

obj = Register(root)
root.mainloop()
