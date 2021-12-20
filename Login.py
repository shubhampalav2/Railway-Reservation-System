from tkinter import *
from tkinter import messagebox
from Home import Home
import os

class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("780x700")
        self.root.title("railway reservation system")
        title=Label(self.root,text="Login Page",font=("times new roman",40,"bold"),bg="#010c48",fg="white").place(x=0,y=0,relwidth=1)
        global e1
        global e2
        global e3
        global e4
        Label(root, text="UserName",font=("times new roman",12,"bold")).place(x=10, y=100)
        Label(root, text="Password",font=("times new roman",12,"bold")).place(x=10, y=140)
        e1=Entry(root)
        e1.place(x=140, y=100)
        e2=Entry(root)
        e2.place(x=140, y=140)
        e2.config(show="*")
        #button
        B1= Button(root, text="Login", command=self.Home,height=3,width=13)
        B1.place(x=10,y=340)
    def Home(self):
        self.uname=e1.get()
        self.password=e2.get()
        if(self.uname=="" and self.password==""):
            messagebox.showinfo("","Blank Not allowed")
        elif(self.uname=="Admin" and self.password=="rail@123"):
            messagebox.showinfo("","Login Successfull")
            self.root.destroy()
            os.system("python Home.py")
            '''self.new_win=Toplevel(self.root)
            self.new_obj=Home(self.new_win)'''
        else:
            messagebox.showinfo("","Invalid Username and Password")
        
   

        


if __name__ == "__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()
'''def Ok():
    uname=e1.get()
    password=e2.get()

    if(uname=="" and password==""):
        messagebox.showinfo("","Blank Not allowed")
    elif(uname=="Admin" and password=="rail@123"):
        messagebox.showinfo("","Login Successfull")  
    else:
        messagebox.showinfo("","Invalid Username and Password")
        



        

def Close():
    top.destory()





    
    





top=Tk()
top.title("Railway Reservation System")
top.geometry()
global e1
global e2
global e3
global e4
Label(top, text="UserName").place(x=10, y=10)
Label(top, text="Password").place(x=10, y=40)

e1=Entry(top)
e1.place(x=140, y=10)

e2=Entry(top)
e2.place(x=140, y=40)
e2.config(show="*")

B1= Button(top, text="Login", command=Ok,height=3,width=13)
B1.place(x=10,y=240)

B2= Button(top, text="Exit",height=3,width=13,command=Close)
B2.place(x=180,y=240)

top.mainloop()'''




