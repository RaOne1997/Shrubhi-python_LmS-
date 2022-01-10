from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import pymysql


class hello:
    def __init__(self, root):
        self.root = root
        self.root.title("LMS")
        self.root.geometry("1350x700+0+0")

        self.bg = ImageTk.PhotoImage(file="image/How To Add a Background Image to the Top Section of Your Webpage.png")
        Label(self.root, image=self.bg).place(x=0, y=0)
        self.back = Button(root, text="Back", command=self.addstud, font=("rockwell", 15), bg="white",
                           fg="black")
        self.back.place(x=10, y=10)
        # =====frame
        frame1 = Frame(self.root, bd=4, relief=RIDGE)
        frame1.place(x=490, y=54, width=840, height=640)
        # =======tabl
        scroll_x = Scrollbar(frame1, orient=HORIZONTAL)
        scroll_y = Scrollbar(frame1, orient=VERTICAL)
        self.tv = ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5, 6, 7,8,9), xscrollcommand=scroll_x.set,
                               yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.tv.xview)
        scroll_y.config(command=self.tv.yview)
        self.tv.heading(1, text="RollNo")
        self.tv.heading(2, text="First Name")
        self.tv.heading(3, text="Last Name")
        self.tv.heading(4, text="Email")
        self.tv.heading(5,text="Contact")
        self.tv.heading(6, text="Address")
        self.tv.heading(7, text="Gender")
        self.tv.heading(8, text="Class")
        self.tv.heading(9, text="DOB")
        self.tv['show'] = "headings"
        self.tv.column(1, width=100)
        self.tv.column(2, width=140)
        self.tv.column(3, width=140)
        self.tv.column(4, width=200)
        self.tv.column(5, width=100)
        self.tv.column(6, width=150)
        self.tv.column(7, width=100)
        self.tv.column(8, width=100)
        self.tv.column(9, width=100)
        self.tv.pack(fill=BOTH, expand=1)
        self.fatchtabel()

    def fatchtabel(self):
        conn = pymysql.connect(host="localhost", user="root", password="", database="py_invmanag")
        cur = conn.cursor()
        cur.execute("select * from studinfo ")
        row = cur.fetchall()
        if len(row) != 0:
            self.tv.delete(*self.tv.get_children())
            for rows in row:
                self.tv.insert('', END, value=rows)
            conn.commit()
        conn.close()
    def addstud(self):
        root.destroy()
        import studentrecord

root = Tk()

obj = hello(root)
root.mainloop()
