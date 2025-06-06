from tkinter import *
import sqlite3
import random
import pandas as pd
from tkinter import messagebox
import os
import smtplib
from PIL import Image, ImageTk
from tkinter import Tk, Label, Frame, Entry, Button
import ssl
from email.message import EmailMessage
import email

from .admin_page import Admin_Page_Window
from .signup_page import Signup_Page_Window
from .loading import LoadingBox

class Main_Page_Window:
    def __init__(self, master, db_path, csv_path, logo_img_path, signup_img_path):
        self.master = master
        self.master.geometry("1920x1080+-10+0")
        self.master.title("SALETAK shop management system")

        self.db_path = db_path
        self.csv_path = csv_path
        self.logo_img_path = logo_img_path
        self.signup_img_path = signup_img_path

        # UI styling
        font1 = 'bahnschrift semibold condensed'
        color1 = '#3498db'
        font2 = 'candara'
        color2 = '#76d7c4'

        # Title label
        title = Label(
            self.master,
            text="SALETAK",
            bd=12,
            relief=GROOVE,
            fg="white",
            bg='#21618c',
            font=('chiller', 30, "bold"),
            pady=2
        ).pack(fill=X)

        # Load product data
        data = pd.read_csv(self.csv_path)

        # Initialize product quantity variables
        self.Pantene = IntVar()
        self.Nivea = IntVar()
        self.CeraVe = IntVar()
        self.Vatika = IntVar()
        self.Garnier = IntVar()
        self.Vaseline = IntVar()

        self.Pasta = IntVar()
        self.rice = IntVar()
        self.wheat = IntVar()
        self.food_oil = IntVar()
        self.Bread = IntVar()
        self.sugar = IntVar()

        self.V7 = IntVar()
        self.coca_cola = IntVar()
        self.Sprite = IntVar()
        self.Fanta = IntVar()
        self.Miranda = IntVar()
        self.pepsi = IntVar()

        self.Digestive = IntVar()
        self.Ulker = IntVar()
        self.Fitness = IntVar()
        self.oreo = IntVar()
        self.Biskrem = IntVar()
        self.Lino = IntVar()

        # Price and customer variables
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()
        self.biscuit_price = StringVar()

        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.c_mail = StringVar()
        self.bill_no = StringVar()
        self.search_bill = StringVar()

        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.admin_username = StringVar()
        self.admin_pass = StringVar()

        # Validation for numeric input
        vcmd = (self.master.register(lambda P: P.isdigit() or P == ""), "%P")

        # Customer details frame
        F0=LabelFrame(self.master,bd=10,relief=GROOVE,text="Customer Details",font=(font1,15,"bold"),fg="gold",bg=color1)
        F0.place(x=0,y=70,width=950)

        cname_label=Label(F0,text="Customer Name",bg=color1,font=("times new romen",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F0,width=20,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_label=Label(F0,text="Phone No.",bg=color1,font=("times new romen",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F0,width=20,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        # Email frame
        Frame1=LabelFrame(self.master,bd=10,relief=GROOVE,text="send bill via Email ",font=(font1,15,"bold"),fg="gold",bg=color1)
        Frame1.place(x=950,y=70,width=587)

        cmail_label=Label(Frame1,text="Email",bg=color1,font=("times new romen",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cmail_txt=Entry(Frame1,width=20,textvariable=self.c_mail,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        send_btn=Button(Frame1,text="Send",command=self.send_email_bill,bg=color2,bd=5,fg="black",width=8,font="arial 12 bold").grid(row=0,column=7)

        # Product frames
        cosmetic_frame=LabelFrame(self.master,bd=10,relief=GROOVE,text="Cosmetic",font=(font1,15,"bold"),fg="gold",bg=color1)
        cosmetic_frame.place(x=5,y=152,width=277,height=393)

        bath_txt=Entry(cosmetic_frame,width=4,textvariable=self.Pantene,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        bath_label=Label(cosmetic_frame,text="Pantene",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Nivea_label=Label(cosmetic_frame,text="Nivea",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Nivea_txt=Entry(cosmetic_frame,width=4,textvariable=self.Nivea,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        CeraVe_label=Label(cosmetic_frame,text="CeraVe",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        CeraVe_txt=Entry(cosmetic_frame,width=4,textvariable=self.CeraVe,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=2,column=1,padx=10,pady=10,sticky=W)
        Vatika_label=Label(cosmetic_frame,text="Vatika",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Vatika_txt=Entry(cosmetic_frame,width=4,textvariable=self.Vatika,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        Garnier_label=Label(cosmetic_frame,text="Garnier",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Garnier_txt=Entry(cosmetic_frame,width=4,textvariable=self.Garnier,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        body_lt_label=Label(cosmetic_frame,text="Vaseline",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_lt_txt=Entry(cosmetic_frame,width=4,textvariable=self.Vaseline,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=5,column=1,padx=10,pady=10,sticky=W)

        grocery_frame=LabelFrame(self.master,bd=10,relief=GROOVE,text="Grocery",font=(font1,15,"bold"),fg="gold",bg=color1)
        grocery_frame.place(x=276,y=152,width=220,height=393)

        g1_label=Label(grocery_frame,text="Pasta",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(grocery_frame,width=4,textvariable=self.Pasta,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        g2_label=Label(grocery_frame,text="Rice",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(grocery_frame,width=4,textvariable=self.rice,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        g3_label=Label(grocery_frame,text="Wheat",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(grocery_frame,width=4,textvariable=self.wheat,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=2,column=1,padx=10,pady=10,sticky=W)
        g4_label=Label(grocery_frame,text="Food oil",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(grocery_frame,width=4,textvariable=self.food_oil,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        g5_label=Label(grocery_frame,text="Bread",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(grocery_frame,width=4,textvariable=self.Bread,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        g6_label=Label(grocery_frame,text="Sugar",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(grocery_frame,width=4,textvariable=self.sugar,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=5,column=1,padx=10,pady=10,sticky=W)

        drinks_frame=LabelFrame(self.master,bd=10,relief=GROOVE,text="Cold Drink",font=(font1,15,"bold"),fg="gold",bg=color1)
        drinks_frame.place(x=490,y=152,width=220,height=393)

        d1_label=Label(drinks_frame,text="V7",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        d1_txt=Entry(drinks_frame,width=4,textvariable=self.V7,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        d2_label=Label(drinks_frame,text="Coca cola",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        d2_txt=Entry(drinks_frame,width=4,textvariable=self.coca_cola,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        d3_label=Label(drinks_frame,text="Sprite",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        d3_txt=Entry(drinks_frame,width=4,textvariable=self.Sprite,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=2,column=1,padx=10,pady=10,sticky=W)
        d4_label=Label(drinks_frame,text="Fanta",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        d4_txt=Entry(drinks_frame,width=4,textvariable=self.Fanta,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        d5_label=Label(drinks_frame,text="Miranda",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        d5_txt=Entry(drinks_frame,width=4,textvariable=self.Miranda,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        d6_label=Label(drinks_frame,text="Pepsi",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        d6_txt=Entry(drinks_frame,width=4,textvariable=self.pepsi,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=5,column=1,padx=10,pady=10,sticky=W)

        biscuits_frame=LabelFrame(self.master,bd=10,relief=GROOVE,text="Biscuits",font=(font1,15,"bold"),fg="gold",bg=color1)
        biscuits_frame.place(x=705,y=152,width=230,height=393)

        c1_label=Label(biscuits_frame,text="Digestive",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(biscuits_frame,width=4,textvariable=self.Digestive,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        c2_label=Label(biscuits_frame,text="Ulker",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(biscuits_frame,width=4,textvariable=self.Ulker,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        c3_label=Label(biscuits_frame,text="Oreo",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(biscuits_frame,width=4,textvariable=self.oreo,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=2,column=1,padx=10,pady=10,sticky=W)
        c4_label=Label(biscuits_frame,text="Fitness",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(biscuits_frame,width=4,textvariable=self.Fitness,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        c5_label=Label(biscuits_frame,text="Biskrem",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(biscuits_frame,width=4,textvariable=self.Biskrem,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        c6_label=Label(biscuits_frame,text="Lino",font=(font2,16,"bold"),fg="black",bg=color1).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(biscuits_frame,width=4,textvariable=self.Lino,font=(font2,16,"bold"),bd=5,relief=SUNKEN,validate="key", validatecommand=vcmd).grid(row=5,column=1,padx=10,pady=10,sticky=W)

        # Image section
        self.image_section()

        # Bill area
        F6=LabelFrame(self.master,bd=10,relief=GROOVE)
        F6.place(x=1160,y=152,width=380,height=393)
        bill_title=Label(F6,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F6,orient=VERTICAL)
        self.txtarea=Text(F6,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        # Bill menu
        prices_frame=LabelFrame(self.master,bd=10,relief=GROOVE,text="Bill Menu",font=(font1,15,"bold"),fg="gold",bg=color1)
        prices_frame.place(x=0,y=540,relwidth=1,height=180)

        m1=Label(prices_frame,text="Total Cosmetic Price",bg=color1,fg="black",font=(font2,14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky=W)
        ml_txt=Entry(prices_frame,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        m2=Label(prices_frame,text="Total Grocery Price",bg=color1,fg="black",font=(font2,14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky=W)
        m2_txt=Entry(prices_frame,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
        m3=Label(prices_frame,text="Total Cold-drink Price",bg=color1,fg="black",font=(font2,14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky=W)
        m3_txt=Entry(prices_frame,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        m4=Label(prices_frame,text="Total Biscuit Price",bg=color1,fg="black",font=(font2,14,"bold")).grid(row=3,column=0,padx=20,pady=1,sticky=W)
        m4_txt=Entry(prices_frame,width=18,textvariable=self.biscuit_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=1)

        # Buttons
        btn_frame=Frame(prices_frame,bd=7,relief=GROOVE)
        btn_frame.place(x=635,y=10,width=865,height=115)

        total_btn=Button(btn_frame,command=self.total,text="Total",bg=color2,bd=5,fg="black",pady=15,width=14,font="arial 12 bold").grid(row=0,column=0,padx=15,pady=15)
        genbill_btn=Button(btn_frame,text="Generate Bill",command=self.bill_area,bg=color2,bd=5,fg="black",pady=15,width=14,font="arial 12 bold").grid(row=0,column=1,padx=15,pady=15)
        buy_btn = Button(btn_frame, text="Buy", command=self.buy, bg=color2, bd=5, fg="black", pady=15, width=11, font="arial 12 bold").grid(row=0, column=2, padx=15, pady=15)
        clear_btn=Button(btn_frame,text="Clear",command=self.clear_data,bg=color2,bd=5,fg="black",pady=15,width=11,font="arial 12 bold").grid(row=0,column=3,padx=15,pady=15)
        exit_btn=Button(btn_frame,text="Exit",command=self.exit_app,bg=color2,bd=5,fg="black",pady=15,width=11,font="arial 12 bold").grid(row=0,column=4,padx=15,pady=15)

        self.welcome_bill()

        # Bill search
        F8=LabelFrame(self.master,bd=10,relief=GROOVE,text="Bill Search ",font=(font1,15,"bold"),fg="gold",bg=color1)
        F8.place(x=0,y=712,width=350,height=80)
        bn_txt=Entry(F8,width=18,textvariable=self.search_bill,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=30,pady=1)
        search_btn=Button(F8,text="Search",command=self.find_bill,bg=color2,bd=5,fg="black",width=8,font="arial 12 bold").grid(row=0,column=2)

        # Admin area
        login_signup_frame=LabelFrame(self.master,bd=10,relief=GROOVE,text="Admin area ",font=(font1,15,"bold"),fg="gold",bg=color1)
        login_signup_frame.place(x=351,y=712,width=1186,height=80)

        Label(login_signup_frame,text="Login :  | ",font=(font2,15,"bold"),fg="black",bg=color1).grid(row=0,column=0)
        Label(login_signup_frame,text="ID ",font=(font2,15,"bold"),fg="black",bg=color1).grid(row=0,column=1)
        admin_id1=Entry(login_signup_frame,width=25,textvariable=self.admin_username,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=2,sticky=E)
        Label(login_signup_frame,text="  Password",font=(font2,15,"bold"),fg="black",bg=color1).grid(row=0,column=3)
        admin_pass1=Entry(login_signup_frame,width=18,textvariable=self.admin_pass,font="arial 10 bold",bd=7,relief=SUNKEN,show='X').grid(row=0,column=4,sticky=E)
        a_login=Button(login_signup_frame,text="Login",command=self.login_page,bg=color2,bd=5,fg="black",width=12,font="arial 12 bold").grid(row=0,column=5,padx=35)
        Label(login_signup_frame,text="  Create New Account",font=(font2,15,"bold"),fg="black",bg=color1).grid(row=0,column=6)
        a_sign_up=Button(login_signup_frame,text="Sign Up",command=self.signup_page,bg=color2,bd=5,fg="black",width=12,font="arial 12 bold").grid(row=0,column=7,padx=35)

    #Saletak Image
    def image_section(self):
        color1 = '#3498db'
        img=Image.open(self.logo_img_path)
        pic=ImageTk.PhotoImage(img)
        F5=LabelFrame(self.master,bd=10,relief=GROOVE,bg=color1)
        F5.place(x=930,y=152,width=230,height=393)
        
        image_label=Label(F5,image=pic)
        image_label.image=pic
        image_label.pack()

    #Product Prices
    def total(self):
        # Each Cosmetic product price
        self.c_p=self.Pantene.get()*140
        self.c_n=self.Nivea.get()*75
        self.c_ce=self.CeraVe.get()*450
        self.c_v=self.Vatika.get()*145
        self.c_g=self.Garnier.get()*250
        self.c_vas=self.Vaseline.get()*75

        # Total price
        self.total_cosmetic_price=float(
                self.c_p+
                self.c_n+
                self.c_ce+
                self.c_v+
                self.c_g+
                self.c_vas
                )

        self.cosmetic_price.set(str(self.total_cosmetic_price) + " EGP")

        # Each grocery product price
        self.g_p=self.Pasta.get()*20
        self.g_rc=self.rice.get()*38
        self.g_wh=self.wheat.get()*30
        self.g_sg=self.sugar.get()*37
        self.g_fol=self.food_oil.get()*240
        self.g_br=self.Bread.get()*10

        # Total price
        self.total_grocery_price=float(
                self.g_br+
                self.g_fol+
                self.g_p+
                self.g_rc+
                self.g_sg+
                self.g_wh
                )

        self.grocery_price.set(str(self.total_grocery_price) + " EGP")
        
        # Each Cold drink price
        self.cd_v7=self.V7.get()*20
        self.cd_cc=self.coca_cola.get()*15
        self.cd_fa=self.Fanta.get()*15
        self.cd_sp=self.Sprite.get()*15
        self.cd_mr=self.Miranda.get()*15
        self.cd_ps=self.pepsi.get()*15

        # Total price
        self.total_cold_drink_price=float(
                self.cd_cc+
                self.cd_v7+
                self.cd_fa+
                self.cd_ps+
                self.cd_mr+
                self.cd_sp
                )
        self.cold_drink_price.set(str(self.total_cold_drink_price) + " EGP")
        
        # Each biscuit price
        self.bc_di=self.Digestive.get()*125
        self.bc_o=self.oreo.get()*120
        self.bc_ln=self.Lino.get()*85
        self.bc_ul=self.Ulker.get()*145
        self.bc_fit=self.Fitness.get()*70
        self.bc_bis=self.Biskrem.get()*150

        # Total price
        self.total_biscuit_price=float(
                self.bc_di+
                self.bc_ln+
                self.bc_ul+
                self.bc_o+
                self.bc_fit+
                self.bc_bis
                )
        
        self.biscuit_price.set(str(self.total_biscuit_price) + " EGP")

        #Total Tax
        self.tax=round(((self.total_cosmetic_price+
                self.total_grocery_price+
                self.total_cold_drink_price+
                self.total_biscuit_price)*0.14),2)
        
        # All order total price
        self.total_bill=round(
                self.total_cosmetic_price+
                self.total_grocery_price+
                self.total_cold_drink_price+
                self.total_biscuit_price+
                self.tax, 2
                )
        
    #Bill
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t     || SALETAK SHOP ||")
        self.txtarea.insert(END,"\n_________________________________________\n")
        self.txtarea.insert(END,f"\nBill No. : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name :   {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone no.:    {self.c_phon.get()}")
        self.txtarea.insert(END,"\n==========================================")
        self.txtarea.insert(END,"\nProducts\t\t\tQTY\t   Price")
        self.txtarea.insert(END,"\n==========================================")
        
        
    def bill_area(self):
       
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Fill Customer details")
        elif self.cosmetic_price=="EGP 0.0" and self.grocery_price=="EGP 0.0" and self.cold_drink_price=="EGP 0.0" and self.biscuit_price=="EGP 0.0":
            messagebox.showerror("Error","No product purchased")
        else: 
            self.welcome_bill()
            # cosmetic
            if self.Pantene.get()!=0:
                self.txtarea.insert(END,f"\nPantene    \t\t\t{self.Pantene.get()}\t    {self.c_p}")
            if self.CeraVe.get()!=0:
                self.txtarea.insert(END,f"\nCeraVe \t\t\t{self.CeraVe.get()}\t    {self.c_ce}")
            if self.Nivea.get()!=0:
                self.txtarea.insert(END,f"\nNivea\t\t\t{self.Nivea.get()}\t    {self.c_n}")
            if self.Vatika.get()!=0:
                self.txtarea.insert(END,f"\nVatika\t\t\t{self.Vatika.get()}\t    {self.c_v}")
            if self.Garnier.get()!=0:
                self.txtarea.insert(END,f"\nGarnier \t\t\t{self.Garnier.get()}\t    {self.c_g}")
            if self.Vaseline.get()!=0:
                self.txtarea.insert(END,f"\nVaseline\t\t\t{self.Vaseline.get()}\t    {self.c_vas}")
            
            #Grocery print
            if self.Pasta.get()!=0:
                self.txtarea.insert(END,f"\nPasta   \t\t\t{self.Pasta.get()}\t    {self.g_p}")
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\nRice     \t\t\t{self.rice.get()}\t    {self.g_rc}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\nWheat    \t\t\t{self.wheat.get()}\t    {self.g_wh}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\nFood oil \t\t\t{self.food_oil.get()}\t    {self.g_fol}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\nSugar    \t\t\t{self.sugar.get()}\t    {self.g_sg}")
            if self.Bread.get()!=0:
                self.txtarea.insert(END,f"\nBread     \t\t\t{self.Bread.get()}\t    {self.g_br}")
    
            
            #Biscuit print
            if self.Digestive.get()!=0:
                self.txtarea.insert(END,f"\nDigestive  \t\t\t{self.Digestive.get()}\t    {self.bc_di}")
            if self.oreo.get()!=0:
                self.txtarea.insert(END,f"\nOreo     \t\t\t{self.oreo.get()}\t    {self.bc_o}")
            if self.Ulker.get()!=0:
                self.txtarea.insert(END,f"\nUlker \t\t\t{self.Ulker.get()}\t    {self.bc_ul}")
            if self.Fitness.get()!=0:
                self.txtarea.insert(END,f"\nFitness \t\t\t{self.Fitness.get()}\t    {self.bc_fit}")
            if self.Biskrem.get()!=0:
                self.txtarea.insert(END,f"\nBiskrem  \t\t\t{self.Biskrem.get()}\t    {self.bc_bis}")
            if self.Lino.get()!=0:
                self.txtarea.insert(END,f"\nLino   \t\t\t{self.Lino.get()}\t    {self.bc_ln}")
            
            
            #Cold-drink print
            if self.V7.get()!=0:
                self.txtarea.insert(END,f"\nV7     \t\t\t{self.V7.get()}\t    {self.cd_v7}")
            if self.coca_cola.get()!=0:
                self.txtarea.insert(END,f"\nCoca-Cola\t\t\t{self.coca_cola.get()}\t    {self.cd_cc}")
            if self.Fanta.get()!=0:
                self.txtarea.insert(END,f"\nFanta    \t\t\t{self.Fanta.get()}\t    {self.cd_fa}")
            if self.Sprite.get()!=0:
                self.txtarea.insert(END,f"\nSprite\t\t\t{self.Sprite.get()}\t    {self.cd_sp}")
            if self.pepsi.get()!=0:
                self.txtarea.insert(END,f"\nPepsi    \t\t\t{self.pepsi.get()}\t    {self.cd_ps}")
            if self.Miranda.get()!=0:
                self.txtarea.insert(END,f"\nMiranda   \t\t\t{self.Miranda.get()}\t    {self.cd_mr}")

            self.txtarea.insert(END, f"\n\nTotal Bill (Before tax) :\t\t\t  {(round(self.total_bill - self.tax,2)):.2f} EGP")
            self.txtarea.insert(END, "\n`````````````````````````````````````````")
            self.txtarea.insert(END,f"\nVAT (14%) :\t\t\t       {self.tax:.2f} EGP")
            self.txtarea.insert(END,"\n`````````````````````````````````````````")

            self.txtarea.insert(END,f"\nTotal Bill :\t\t\t      {self.total_bill:.2f} EGP")
            self.txtarea.insert(END,"\n`````````````````````````````````````````")
           
            self.save_bill()
       
    def save_bill(self):
        op=messagebox.askyesno("save bill","Do you want to save the bill ?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            fp1=open("bills/"+str(self.bill_no.get())+".txt","w")
            fp1.write(self.bill_data)
            fp1.close()
            messagebox.showinfo("Saved",f"Bill No. :{self.bill_no.get()} Saved successfuly")
        else:
            return
    
    def find_bill(self):
        present = False
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,f1.read())
                f1.close()
                present = True
                
        if not present:
            messagebox.showerror("Error","Invalid Bill No.")
        
    def clear_data(self):
        #   cosmatic variable
        op=messagebox.askyesno("Clear","Do you want to clear the bill")
        if op>0:
            self.Pantene.set(0)
            self.Nivea.set(0)
            self.CeraVe.set(0)
            self.Vatika.set(0)
            self.Garnier.set(0)
            self.Vaseline.set(0)
            
            # grocery varible
            self.Pasta.set(0)
            self.rice.set(0)
            self.wheat.set(0)
            self.food_oil.set(0)
            self.Bread.set(0)
            self.sugar.set(0)
            
            # cold drink
            self.V7.set(0)
            self.coca_cola.set(0)
            self.Sprite.set(0)
            self.Fanta.set(0)
            self.Miranda.set(0)
            self.pepsi.set(0)
            
            # biscuit varible 
            
            self.Digestive.set(0)
            self.Ulker.set(0)
            self.Fitness.set(0)
            self.oreo.set(0)
            self.Biskrem.set(0)
            self.Lino.set(0)
            
            #product price varible
            
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")
            self.biscuit_price.set("")
            
            #customer details
            
            self.c_name.set("")
            self.c_phon.set("")
            self.c_mail.set("")
            self.bill_no.set("")
            self.search_bill.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            
            self.welcome_bill()
    
        else:
            return
                
        
    def exit_app(self):
        op1=messagebox.askyesno("Exit","Do you want to Exit")
        if op1>0:
            self.master.destroy()
        else:
            return

    def buy(self):

        try:
            # Attempt to read the stock CSV file
            df = pd.read_csv(self.csv_path, encoding='utf-8-sig')
        except FileNotFoundError:
            messagebox.showerror("Error", "The stock.csv file was not found.")
            return
        except pd.errors.EmptyDataError:
            messagebox.showerror("Error", "The stock.csv file is empty.")
            return
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while opening the stock file: {str(e)}")
            return

        products_name = [
            self.Pantene.get(),
            self.Nivea.get(),
            self.CeraVe.get(),
            self.Vatika.get(),
            self.Garnier.get(),
            self.Vaseline.get(),
            self.Pasta.get(),
            self.rice.get(),
            self.wheat.get(),
            self.food_oil.get(),
            self.Bread.get(),
            self.sugar.get(),
            self.V7.get(),
            self.coca_cola.get(),
            self.Sprite.get(),
            self.Fanta.get(),
            self.Miranda.get(),
            self.pepsi.get(),
            self.Digestive.get(),
            self.Ulker.get(),
            self.oreo.get(),
            self.Fitness.get(),
            self.Biskrem.get(),
            self.Lino.get()
            ]
        # self.bill_area()

        op1=messagebox.askyesno("Purchase","Do you want to to Purchase?")
        if not op1:
            return

        unavailable_product = {}
        available = True
        # Iterate over the DataFrame rows
        for index, row in df.iterrows():
            if products_name[index] > row["Quantity"]:
                available = False
                unavailable_product.update({row["Product"]: row["Quantity"]})

        
        if available:
            for index, row in df.iterrows():
                quantity_ordered = products_name[index]
                if quantity_ordered > 0:  # Ensure some quantity was ordered
                    df.at[index, 'Quantity'] -= quantity_ordered  # Reduce the stock

            # Save the updated DataFrame back to the CSV file
            df.to_csv(self.csv_path, index=False, encoding='utf-8-sig')
            self.loading_box(available)
        else:
            self.loading_box(available, unavailable_product)


    def send_email_bill(self):
        # get_3 = self.c_mail.get()

        # op=messagebox.askyesno("Send bill","Do you want to Send the bill ?")
        # if op>0:
        #     self.bill_data=self.txtarea.get('1.0',END)
        #     fp1=open("bills/"+str(self.bill_no.get())+".txt","w")
        #     msg=self.bill_data
        # else:
        #     return


        # try:
        #     email_sender = '' # email
        #     email_password = '' # email passsword
        #     email_receiver = get_3

        #     subject = 'Saletak Order'
        #     body = msg

        #     em = EmailMessage()
        #     em['From'] = email_sender
        #     em['To'] = email_receiver
        #     em['Subject'] = subject
        #     em.set_content(body)

        #     context = ssl.create_default_context()

        #     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        #         smtp.login(email_sender, email_password)
        #         smtp.sendmail(email_sender, email_receiver, em.as_string())
        #     statement_1 = "MAIL HAS BEEN SENT"
        #     messagebox.showinfo("Sent", f"Bill No. :{self.bill_no.get()} Sent successfuly")

        #     return statement_1
        # except email.errors.HeaderParseError:
        #      statement_2 = "SOMETHING WENT WRONG"
        #      return statement_2
        # except smtplib.SMTPRecipientsRefused:
        #     messagebox.showerror("Email Error", "The recipient email address is invalid or could not be reached.")
        # except Exception as e:
        #     messagebox.showerror("Error", f"An error occurred: {e}")
        pass
    
    def login_page(self):
        ad_id = self.admin_username.get()
        ad_pass = self.admin_pass.get()

        # Connect to the database
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            # Check if the username exists and the password matches
            cursor.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (ad_id, ad_pass))
            user = cursor.fetchone()

            if user:
                global login_window
                login_window = Tk()
                obj1 = Admin_Page_Window(login_window, ad_id, self.csv_path)  # Assuming this is the next window class
                login_window.mainloop()
            else:
                messagebox.showerror("Error", "Invalid username or password")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        finally:
            conn.close()

    
    def signup_page(self):
        global signup_window
        signup_window = Toplevel()
        obj2 = Signup_Page_Window(signup_window, self.db_path, self.signup_img_path)
        signup_window.mainloop()

    def loading_box(self, available, unavailable_products = 0):
        # Show the loading box
        self.loading = LoadingBox(self.master, "Loading, please wait...")

        # Start the task without blocking the main loop
        self.simulate_task_step(available, unavailable_products, 0)

    def simulate_task_step(self, status, unavailable_products, step):
        """Simulates a task step-by-step."""
        if step < 3:  # Simulate 3 steps
            self.master.after(1000, self.simulate_task_step, status, unavailable_products, step + 1)  # Wait 1 second and continue
        else:
            # Task is complete, close the loading box
            self.loading.close()
            if status:
                messagebox.showinfo("Done", "Purchase Done!")
            else:
                products_tuple = unavailable_products.items()
                for product in products_tuple:
                    messagebox.showerror("Error",f"You only have {product[1]} from {product[0]}")