from tkinter import *
from datetime import *
import  time
import bg as bg
from math import *
from PIL import ImageDraw,Image,ImageTk


class clock:
    def __init__(self,root):
        self.root=root
        self.root.title("clock")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        lbl2 = Frame(self.root)
        lbl2.place(x=250, y=100, height=500, width=800)
        titleF = Label(lbl2, text="First name", font=("new time roman", 15, "bold"), bg="white", fg="black").place(
            x=200, y=50)
        self.txt_fname = Entry(lbl2, font=("new time roman", 15), bg="white", fg="black")
        self.txt_fname.place(x=220, y=80)

        self.lbl=Label(self.root, bg="#E6E6FA")
        self.lbl.place(x=100, y=150, height=400, width=300)


     #   self.clock_img()
        self.working()


    def clock_img(self,hr,mins,sec):
        clock=Image.new("RGB", (400, 400), (0, 0, 0))
        draw= ImageDraw.Draw(clock)

        #=========for Clock Image
        bg=Image.open("cl.png")
        bg=bg.resize((300, 300),Image.ANTIALIAS)
        clock.paste(bg,(50, 50))

        #============hur line image
        origrn=200,200
        draw.line((origrn, 200+60*sin(radians(hr)), 200-60*cos(radians(hr))), fill="blue", width=4)
        # ============min line image
        draw.line((origrn, 200+80*sin(radians(mins)), 200-80*cos(radians(mins))), fill="yellow", width=4)
        # ============sec line image
        draw.line((origrn, 200+80*sin(radians(sec)), 200-100*cos(radians(sec))), fill="red", width=4)
        draw.ellipse((195,195,210,210),fill="white")
        clock.save("clock_new.png")

    def working(self):
            h=datetime.now().time().hour
            m=datetime.now().time().minute
            s=datetime.now().time().second
           # print(h,m,s)

            hr=(h/12)*360
            mins=(m/60)*360
            sec=(s/60)*360
            #print(hr,mins,sec)
            self.clock_img(hr,mins,sec)
            self.img=ImageTk.PhotoImage(file="clock_new.png")
            self.lbl.config(image=self.img)
            self.lbl.after(200,self.working)









root=Tk()
obj=clock(root)
root.mainloop()