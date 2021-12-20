from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import sqlite3
conn=sqlite3.connect('railway.db')
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS trainsdetails(TrainNo INTEGER PRIMARY KEY,
                                                      TrainName TEXT NOT NULL,
                                                      StartPlace TEXT NOT NULL,
                                                      EndPlace TEXT NOT NULL,
                                                      Price INTEGER NOT NULL)""")
print("Table created successfully")
conn.commit()
conn.close()

class Add:
    def __init__(self,root):
        self.root=root
        self.root.geometry("780x700")
        self.root.title("railway reservation system")
        title=Label(self.root,text="Add Trains",font=("times new roman",40,"bold"),bg="#010c48",fg="white").place(x=0,y=0,relwidth=1)
        global e1
        global e2
        global e3
        global e4
        global e5
        self.TrainNo=StringVar()
        self.TrainName=StringVar()
        self.StartPlace=StringVar()
        self.EndPlace=StringVar()
        self.Price=StringVar()
        Label(self.root, text="TrainNo",font=("times new roman",12,"bold")).place(x=10, y=100)
        Label(self.root, text="TrainName",font=("times new roman",12,"bold")).place(x=10, y=140)
        Label(self.root, text="StartPlace",font=("times new roman",12,"bold")).place(x=10, y=180)
        Label(self.root, text="EndPlace",font=("times new roman",12,"bold")).place(x=10, y=220)
        Label(self.root, text="Price",font=("times new roman",12,"bold")).place(x=10, y=260)
        e1=Entry(self.root,textvariable=self.TrainNo)
        e1.place(x=140, y=100)
        e2=Entry(self.root,textvariable=self.TrainName)
        e2.place(x=140, y=140)
        e3=Entry(self.root,textvariable=self.StartPlace)
        e3.place(x=140, y=180)
        e4=Entry(self.root,textvariable=self.EndPlace)
        e4.place(x=140, y=220)
        e5=Entry(self.root,textvariable=self.Price)
        e5.place(x=140, y=260)
        B1= Button(root, text="Insert",bg="red",command=self.add,height=3,width=13)
        B1.place(x=80,y=340)
        B2= Button(root, text="Update",bg="red",command=self.edit,height=3,width=13)
        B2.place(x=200,y=340)
        B3= Button(root, text="Delete",bg="red",command=self.delete,height=3,width=13)
        B3.place(x=320,y=340)
        B4= Button(root, text="Clear",bg="red",command=self.clear,height=3,width=13)
        B4.place(x=440,y=340)
        train_frame=Frame(self.root,bd=3,relief=RIDGE)
        train_frame.place(x=0,y=420,relwidth=1,height=150)
        scrolly=Scrollbar(train_frame,orient=VERTICAL)
        scrollx=Scrollbar(train_frame,orient=HORIZONTAL)
        self.trainsdetails=ttk.Treeview(train_frame,columns=("TrainNo","TrainName","StartPlace","EndPlace","Price"))
        self.trainsdetails.heading("TrainNo",text="TrainNo")
        self.trainsdetails.heading("TrainName",text="TrainName")
        self.trainsdetails.heading("StartPlace",text="StartPlace")
        self.trainsdetails.heading("EndPlace",text="EndPlace")
        self.trainsdetails.heading("Price",text="Price")
        self.trainsdetails["show"]="headings"
        self.trainsdetails.pack(fill=BOTH,expand=1)
        self.trainsdetails.bind("<ButtonRelease-1>",self.get_data)
        self.show()
    def delete(self):
       value_del=(self.TrainNo.get())
       print(value_del)
       conn=sqlite3.connect('railway.db')
       c2=conn.cursor()
       sql="DELETE FROM trainsdetails WHERE TrainNo=?"
       c2.execute(sql,(value_del,))
       c2.execute("""SELECT * FROM trainsdetails""")
       list123 = c2.fetchall()
       conn.commit()
       messagebox.showinfo("Title","Record is deleted")
       self.show()
    def add(self):
        try:
            if(self.TrainName.get()=="" or self.StartPlace.get()=="" or self.EndPlace.get()=="" or self.Price.get()==""):
                conn1=sqlite3.connect('rail.db')
                c1=conn1.cursor()
                messagebox.showinfo("","NULL POINTER EXCEPTION")
            elif self.Price.get()!="":
                conn1=sqlite3.connect('railway.db')
                c1=conn1.cursor()
                sql= '''INSERT INTO trainsdetails(TrainNo,TrainNAME,StartPlace,EndPlace,Price) VALUES (?,?,?,?,?)'''
                c1.execute(sql,(self.TrainNo.get(),
                                self.TrainName.get(),
                                self.StartPlace.get(),
                                self.EndPlace.get(),
                                self.Price.get()))
                conn1.commit()
                c1.execute("""SELECT * FROM trainsdetails""")
                list123 = c1.fetchall()
                messagebox.showinfo("","Record is inserted")
                self.show()
            else:
                conn1=sqlite3.connect('railway.db')
                c1=conn1.cursor()
                messagebox.showinfo("Error","Datatype MisMatch Exception")                               
        except Exception as e:
            print(e)
            print("sql error")
        finally:
            conn1.close()
            print("finally")    
    def edit(self):
        conn2=sqlite3.connect('railway.db')
        c=conn2.cursor()
        sql="UPDATE trainsdetails set TrainNo=?,TrainName=?,StartPlace=?,EndPlace=?,Price=? where TrainNo=?"
        c.execute(sql,(self.TrainNo.get(),
                       self.TrainName.get(),
                       self.StartPlace.get(),
                       self.EndPlace.get(),
                       self.Price.get(),
                       self.TrainNo.get()))
        conn2.commit()
        c.execute("""SELECT * FROM trainsdetails""")
        conn2.commit()
        list = c.fetchall()
        messagebox.showinfo("Success","Record is edited")
        self.show()
        conn2.close()
    def clear(self):
        self.TrainNo.set("")
        self.TrainName.set("")
        self.StartPlace.set("")
        self.EndPlace.set("")
        self.Price.set("")
    def get_data(self,event=""):
        f=self.trainsdetails.focus()
        content=(self.trainsdetails.item(f))
        row=content['values']
        try:
             self.TrainNo.set(row[0])
             self.TrainName.set(row[1])
             self.StartPlace.set(row[2])
             self.EndPlace.set(row[3])
             self.Price.set(row[4])
        except Exception as e:
            print(e)
        
    def show(self):
         conn1=sqlite3.connect('railway.db')
         c1=conn1.cursor()
         try:
             c1.execute("""SELECT * FROM trainsdetails""")
             rows=c1.fetchall()
             self.trainsdetails.delete(*self.trainsdetails.get_children())
             for row in rows:
                 self.trainsdetails.insert('',END,values=row)
         except exception as e:
             print(e)      
    

             
        
if __name__ == "__main__":
    root=Tk()
    obj=Add(root)
    root.mainloop()
