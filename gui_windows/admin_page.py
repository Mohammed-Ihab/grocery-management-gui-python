from tkinter import *
import pandas as pd
import os
from subprocess import Popen

class Admin_Page_Window:
    def __init__(self, admin_master, user_id, csv_path):
        # Admin Window
        self.admin_master=admin_master
        self.admin_master.geometry("1920x1080+-10+0")
        self.admin_master.title("Admin Area")

        self.user_id = user_id
        self.csv_path = csv_path

        # Colors and Fonts used
        font2 = 'candara'
        color1 = '#3498db'
        cyan_color = '#76d7c4'
        
        # Labels and Buttons
        window_title=Label(self.admin_master,text="SALETAK SHOP MANAGEMENT",bd=12,relief=GROOVE,bg='#21618c',fg='white',font=('chiller',30,"bold"),pady=2).pack(fill=X)
        
        Frame1=Label(self.admin_master,bd=10,relief=GROOVE,text=f"Welcome, {self.user_id}!",font=(font2,15,"bold"),fg="black",bg=color1)
        Frame1.place(x=0,y=73,height=60,width=1537)
        Frame2=LabelFrame(self.admin_master,bd=10,relief=GROOVE,text="MENU",font=(font2,15,"bold"),fg="black",bg=color1)
        Frame2.place(x=0,y=133,width=230,height=600)
        
        stock_button = Button(Frame2,text="Stock",command=self.check_stock,bg=cyan_color,bd=5,fg="black",width=15,font="arial 12 bold").grid(row=0,column=0,padx=10,pady=15)
        fill = Label(Frame2,text="",bg=color1,bd=5,fg="black",width=15,font="arial 12 bold").grid(row=1,column=0,padx=10,pady=15)

        update_stock_button = Button(Frame2,text="Update Stock",command=self.Update_stock,bg=cyan_color,bd=5,fg="black",width=15,font="arial 12 bold").grid(row=2,column=0,padx=10,pady=15)
        fill = Label(Frame2, text="", bg=color1, bd=5, fg="black", width=15, font="arial 12 bold").grid(row=3, column=0, padx=10,pady=15)

        bills = Button(Frame2,text="Bill List",command=self.bill_list,bg=cyan_color,bd=5,fg="black",width=15,font="arial 12 bold").grid(row=4,column=0,padx=10,pady=15)
        fill = Label(Frame2, text="", bg=color1, bd=5, fg="black", width=15, font="arial 12 bold").grid(row=5,column=0,padx=10,pady=15)
        clear_button = Button(Frame2,text="Clear",command=self.bill_init,bg=cyan_color,bd=5,fg="black",width=15,font="arial 12 bold").grid(row=6,column=0,padx=10,pady=15)
        
        Frame3=LabelFrame(self.admin_master,bd=10,text="Bottom",relief=GROOVE,bg=color1)
        Frame3.place(x=0,y=733,width=1537,height=60)
        
        # Notepad Area
        Frame4=LabelFrame(self.admin_master,bd=10,relief=GROOVE)
        Frame4.place(x=780,y=133,width=757,height=600)
        bill_title=Label(Frame4,text="Notepad Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        
        scrol_y=Scrollbar(Frame4,orient=VERTICAL)
        self.admintxtarea=Text(Frame4,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.admintxtarea.yview)
        self.admintxtarea.pack(fill=BOTH,expand=1)
        self.bill_init()
        

    def bill_init(self):
            # Clearing the text area and putting Saletak shop at the beginning
            self.admintxtarea.delete('1.0',END)
            self.admintxtarea.insert(END,"\t\t\t\t\t|| SALETAK SHOP ||")
            self.admintxtarea.insert(END,"\n_________________________________________________________________________________________\n")
    
    def check_stock(self):
        # Clearing
        self.bill_init()

        # Reading the stock file
        df = pd.read_csv(self.csv_path, encoding='utf-8-sig')

        # Start building the text for insertion
        self.admintxtarea.insert(END, "|| Product    || \t\t\t\t\t\t\t\t ||Quantity")
        self.admintxtarea.insert(END, "\n_________________________________________________________________________________________\n")

        # Iterate over the stock DataFrame rows
        for index, row in df.iterrows():
            self.admintxtarea.insert(END, f"\n{row['Product']}\t\t\t\t\t\t\t\t {row['Quantity']}")
    
    def bill_list(self):
        #Clearing
        self.bill_init()

        count=1 
        self.admintxtarea.insert(END,"S.No.\t Bill \n\n")

        # Iterate over the bills folder files
        for i in os.listdir("bills/"):
           self.admintxtarea.insert(END,str(count)+".\t"+str(i)+"\n\n")
           count += 1

    def Update_stock(self):        
         p=Popen(self.csv_path,shell=True)