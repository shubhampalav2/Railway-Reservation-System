from tkinter import *
from Add import Add
from Reserv import Reserv
from tkinter import messagebox


class Home:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x700")
        self.root.title("railway reservation system")
        title=Label(self.root,text="Railway Reservation System",font=("times new roman",40,"bold"),bg="#010c48",fg="white").place(x=0,y=0,relwidth=1)
        B1= Button(root, text="Add Trains",bg="green",command=self.Add,height=3,width=13)
        B1.place(x=10,y=240)
        B2= Button(root, text="Reservation",command=self.Reserv,bg="green",height=3,width=13)
        B2.place(x=480,y=240)
        B3= Button(root, text="LogOut",command=root.quit,bg="yellow",height=3,width=13)
        B3.place(x=1150,y=4)
    def iExit(self):
        iExit=messagebox.askyesno("Railway Reservation System","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return
    def Reserv(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Reserv(self.new_win)
    def Add(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Add(self.new_win)


if __name__ == "__main__":
    root=Tk()
    obj=Home(root)
    root.mainloop()
