from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import sqlite3
conn=sqlite3.connect('railway.db')
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS trainsdetails( TrainNo INTEGER PRIMARY KEY,
                                                      TrainName TEXT,
                                                      StartPlace TEXT,
                                                      DestinationPlace TEXT,
                                                      Price INTEGER)""")
c.execute("""CREATE TABLE IF NOT EXISTS reservation( PassengerNo INTEGER PRIMARY KEY,
                                                     PassengerName TEXT,
                                                     StartPlace TEXT,
                                                      DestinationPlace TEXT,
                                                      TrainNo INTEGER,
                                                       TrainName TEXT,
                                                       Gender TEXT,
                                                       Age INTEGER,
                                                      Price INTEGER,
                                                      Date TEXT,
                                                      NoOfTickets INTEGER,
                                                      Total INTEGER)""")
conn.commit()
conn.close()
class Reserv:
    def __init__(self,root):
        self.root=root
        self.root.geometry("780x700")
        self.root.title("railway reservation system")
        title=Label(self.root,text="Reservation",font=("times new roman",40,"bold"),bg="#010c48",fg="white").place(x=0,y=0,relwidth=1)
        global e1
        global e2
        global e3
        global e4
        global e5
        global e6
        global e7
        global e8
        global e9
        global e10
        global e11
        #All variables
        self.PassengerNo=StringVar()
        self.PassengerName=StringVar()
        self.StartPlace=StringVar()
        self.DestinationPlace=StringVar()
        self.TrainNo=StringVar()
        self.TrainName=StringVar()
        self.Gender=StringVar()
        self.Age=StringVar()
        self.Price=StringVar()
        self.Date=StringVar()
        self.NoOfTickets=StringVar()
        self.Total=StringVar()
        #button
        B1= Button(root, text="Reserve",bg="red",font=("times new roman",10,"bold"),command=self.reserve,height=3,width=13)
        B1.place(x=10,y=600)
        B2= Button(root, text="Cancel",bg="red",font=("times new roman",10,"bold"),command=self.cancel,height=3,width=13)
        B2.place(x=140,y=600)
        B3= Button(root, text="Search",bg="red",font=("times new roman",10,"bold"),command=self.search,height=3,width=13)
        B3.place(x=270,y=600)
        B4= Button(root, text="Clear Data",bg="red",font=("times new roman",10,"bold"),command=self.clear,height=3,width=13)
        B4.place(x=400,y=600)
        Label(self.root, text="PassengerNo",font=("times new roman",12,"bold")).place(x=10, y=100)
        Label(self.root, text="PassengerName",font=("times new roman",12,"bold")).place(x=10, y=140)
        Label(self.root, text="StartPlace",font=("times new roman",12,"bold")).place(x=10, y=180)
        Label(self.root, text="DestinationPlace",font=("times new roman",12,"bold")).place(x=10, y=220)
        Label(self.root, text="TrainNo",font=("times new roman",12,"bold")).place(x=10, y=260)
        Label(self.root, text="TrainName",font=("times new roman",12,"bold")).place(x=10, y=300)
        Label(self.root, text="Gender",font=("times new roman",12,"bold")).place(x=10, y=340)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.Gender,values=("Male","Female","Others"),font=("goudy old style",15)).place(x=140,y=340)
        Label(self.root, text="Age",font=("times new roman",12,"bold")).place(x=10, y=380)
        Label(self.root, text="Price",font=("times new roman",12,"bold")).place(x=10, y=420)
        Label(self.root, text="Date",font=("times new roman",12,"bold")).place(x=10, y=460)
        Label(self.root, text="NoOfTickets",font=("times new roman",12,"bold")).place(x=10, y=500)
        Label(self.root, text="Total",font=("times new roman",12,"bold")).place(x=10, y=540)
        e1=Entry(root,textvariable=self.PassengerNo)
        e1.place(x=140, y=100)
        e2=Entry(root,textvariable=self.PassengerName)
        e2.place(x=140, y=140)
        e3=Entry(root,textvariable=self.StartPlace)
        e3.place(x=140, y=180)
        e4=Entry(root,textvariable=self.DestinationPlace)
        e4.place(x=140, y=220)
        e5=Entry(root,textvariable=self.TrainNo)
        e5.place(x=140, y=260)
        e6=Entry(root,textvariable= self.TrainName)
        e6.place(x=140, y=300)
        e7=Entry(root,textvariable=self.Age)
        e7.place(x=140, y=380)
        e8=Entry(root,textvariable=self.Price)
        e8.place(x=140, y=420)
        e9=Entry(root,textvariable=self.Date)
        e9.place(x=140, y=460)
        e10=Entry(root,textvariable=self.NoOfTickets)
        e10.place(x=140, y=500)
        e11=Entry(root,textvariable=self.Total)
        e11.place(x=140, y=540)
        train_frame=Frame(self.root,bd=3,relief=RIDGE)
        train_frame.place(x=400,y=100,width=900,height=250)
        scrolly=Scrollbar(train_frame,orient=VERTICAL)
        scrollx=Scrollbar(train_frame,orient=HORIZONTAL)
        self.reservation=ttk.Treeview(train_frame,columns=("PassengerNo","PassengerName","StartPlace","DestinationPlace","TrainNo","TrainName","Gender","Age","Price","Date","NoOfTickets","Total"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrollx.config(command=self.reservation.xview)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.reservation.yview)
        self.reservation.heading("PassengerNo",text="PassengerNo")
        self.reservation.heading("PassengerName",text="PassengerName")
        self.reservation.heading("StartPlace",text="StartPlace")
        self.reservation.heading("DestinationPlace",text="DestinationPlace")
        self.reservation.heading("TrainNo",text="TrainNo")
        self.reservation.heading("TrainName",text="TrainName")
        self.reservation.heading("Gender",text="Gender")
        self.reservation.heading("Age",text="Age")
        self.reservation.heading("Price",text="Price")
        self.reservation.heading("Date",text="Date")
        self.reservation.heading("NoOfTickets",text="NoOfTickets")
        self.reservation.heading("Total",text="Total")
        self.reservation["show"]="headings"
        '''self.reservation.column("PassengerNo",width=80)
        self.reservation.column("PassengerName",width=100)
        self.reservation.column("StartPlace",width=60)
        self.reservation.column("DestinationPlace",width=100)
        self.reservation.column("TrainNo",width=50)
        self.reservation.column("TrainName",width=100)
        self.reservation.column("Gender",width=60)
        self.reservation.column("Age",width=40)
        self.reservation.column("Price",width=50)
        self.reservation.column("Date",width=40)
        self.reservation.column("NoOfTickets",width=90)
        self.reservation.column("Total",width=40)'''
        self.reservation.pack(fill=BOTH,expand=1)
        self.reservation.bind("<ButtonRelease-1>",self.get_data)
        self.show()
    def show(self):
         conn1=sqlite3.connect('railway.db')
         c1=conn1.cursor()
         try:
             c1.execute("""SELECT * FROM reservation""")
             rows=c1.fetchall()
             self.reservation.delete(*self.reservation.get_children())
             for row in rows:
                 self.reservation.insert('',END,values=row)
         except exception as e:
             print(e)
    def cancel(self):
        conn=sqlite3.connect('railway.db')
        c2=conn.cursor()
        sql="DELETE FROM reservation WHERE PassengerNo=?"
        val=(self.PassengerNo.get())
        c2.execute(sql,(val,))
        c2.execute("""SELECT * FROM trainsdetails""")
        list123 = c2.fetchall()
        conn.commit()
        messagebox.showinfo("Title","Ticket is Cancelled")
        self.show()
    def search(self):
        conn1=sqlite3.connect('railway.db')
        c1=conn1.cursor()
        sql="""SELECT * FROM reservation where StartPlace=? and DestinationPlace=?"""
        c1.execute(sql,(self.StartPlace.get(),self.DestinationPlace.get()))
        rows=c1.fetchall()
        self.reservation.delete(*self.reservation.get_children())
        for row in rows:
            self.reservation.insert('',END,values=row)
        if rows:
            messagebox.showinfo("Title","Record Found")
        else:
            messagebox.showinfo("Title","Record Not Found")
                
        
    def reserve(self):
        try:
            if(self.TrainName.get()=="" or self.StartPlace.get()=="" or self.DestinationPlace.get()=="" or self.Age.get()=="" or self.PassengerName.get()=="" or self.PassengerNo.get()=="" or self.TrainNo.get()=="" or self.NoOfTickets.get()=="" or self.Price.get()==""):
                conn1=sqlite3.connect('railway.db')
                c1=conn1.cursor()
                messagebox.showinfo("Title","NULL POINTER EXCEPTION")
                
            else:
                conn1=sqlite3.connect('railway.db')
                c1=conn1.cursor()
                sql= '''INSERT INTO reservation(PassengerNo,PassengerName,StartPlace,DestinationPlace,TrainNo,TrainName,Gender,Age,Price,Date,NoOfTickets,Total) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''
                c1.execute(sql,(self.PassengerNo.get(),
                                self.PassengerName.get(),
                                self.StartPlace.get(),
                                self.DestinationPlace.get(),
                                self.TrainNo.get(),
                                self.TrainName.get(),
                                self.Gender.get(),
                                self.Age.get(),
                                self.Price.get(),
                                self.Date.get(),
                                self.NoOfTickets.get(),
                                self.Total.get()))
                conn1.commit()
                c1.execute("""SELECT * FROM reservation""")
                list = c1.fetchall()
                messagebox.showinfo("Success","Ticket is reserved")
                self.show()

        except Exception as e:
            print(e)
            messagebox.showinfo("Title","Datatype MisMatch Exception")
    def get_data(self,event=""):
         f=self.reservation.focus()
         content=(self.reservation.item(f))
         row=content['values']
         try:
             self.PassengerNo.set(row[0])
             self.PassengerName.set(row[1])
             self.StartPlace.set(row[2])
             self.DestinationPlace.set(row[3])
             self.TrainNo.set(row[4])
             self.TrainName.set(row[5])
             self.Gender.set(row[6])
             self.Age.set(row[7])
             self.Price.set(row[8])
             self.Date.set(row[9])
             self.NoOfTickets.set(row[10])
             self.Total.set(row[11]) 
         except Exception as e:
             print(e)
    def clear(self):
        self.PassengerNo.set("")
        self.PassengerName.set("")
        self.StartPlace.set("")
        self.DestinationPlace.set("")
        self.TrainNo.set("")
        self.TrainName.set("")
        self.Gender.set("")
        self.Age.set("")
        self.Price.set("")
        self.Date.set("")
        self.NoOfTickets.set("")
        self.Total.set("") 
       
        
            
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Reserv(root)
    root.mainloop()
