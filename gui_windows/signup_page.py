from tkinter import *
import sqlite3
from PIL import Image, ImageTk
from tkinter import messagebox

class Signup_Page_Window:
    def __init__(self, signup_master, db_path, signup_img_path):
        # Signup window
        self.signup_master=signup_master
        self.signup_master.geometry("925x500+-10+0")
        self.signup_master.title("Create New Account")

        self.db_path = db_path
        self.signup_img_path = signup_img_path

        # Colors and Fonts that will be used
        blue_color = '#48b3fa'
        cyan_color = '#76d7c4'
        brand_font = 'chiller'
        font2 = 'candara'
        
        # Create a variables that holds the values in the entries
        self.new_account_id=StringVar()
        self.new_account_pass=StringVar()
        self.new_account_pass_confirm=StringVar()        
        
        # Load the background image
        img = Image.open(self.signup_img_path)
        pic = ImageTk.PhotoImage(img)

        # Create a Canvas widget to display the image and text
        canvas = Canvas(self.signup_master, width=925, height=500)
        canvas.place(x=0, y=0)

        canvas.create_image(0, 0, anchor=NW, image=pic)

        # Keep a reference to the image
        canvas.image = pic

        # Add the text on top of the image with no background
        canvas.create_text(230, 220, text="SALETAK", font=(brand_font, 30, "bold"), fill='white')
        canvas.create_text(230, 265, text="GROCERY MANAGEMENT APP", font=(brand_font, 25, "bold"), fill='white')
        canvas.create_text(590, 80, text="Create New Account", font=(font2, 20, "bold"), fill='white')

        # ID Entry
        self.admin_username=Entry(self.signup_master,width=25,textvariable=self.new_account_id,font="arial 10 bold",bg=blue_color,border=0)
        self.admin_username.place(x = 480,y = 155)
        self.admin_username.insert(0,'ID/Username')
        self.admin_username.bind('<FocusIn>', self.on_enter_id)
        self.admin_username.bind('<FocusOut>', self.on_leave_id)
        Frame(self.signup_master,width=200,height=2,bg='black').place(x=475,y=180)

        # Password Entry
        self.admin_pass1=Entry(self.signup_master,width=25,textvariable=self.new_account_pass,font="arial 10 bold",border=0,bg=blue_color)
        self.admin_pass1.place(x = 480, y = 215)
        self.admin_pass1.insert(0,'Password')
        self.admin_pass1.bind('<FocusIn>', self.on_enter_pass)
        self.admin_pass1.bind('<FocusOut>', self.on_leave_pass)
        Frame(self.signup_master,width=200,height=2,bg='black').place(x=475,y=240)

        # Confirm Password Entry
        self.admin_pass_confirm=Entry(self.signup_master,width=25,textvariable=self.new_account_pass_confirm,font="arial 10 bold",border=0,bg=blue_color)
        self.admin_pass_confirm.place(x = 480, y = 275)
        self.admin_pass_confirm.insert(0,'Confirm Password')
        self.admin_pass_confirm.bind('<FocusIn>', self.on_enter_pass_confirm)
        self.admin_pass_confirm.bind('<FocusOut>', self.on_leave_pass_confirm)
        Frame(self.signup_master,width=200,height=2,bg='black').place(x=475,y=305)

        sign_up=Button(self.signup_master,text="Sign Up",command=self.create_account,bg=cyan_color,bd=5,fg="black",width=12,font="arial 12 bold").place(x=475,y=350)

    # on enter funtions to delete the ID/Username shown if the user clicked on the Entry
    def on_enter_id(self, e):
        name = self.admin_username.get()
        if name == 'ID/Username':
            self.admin_username.delete(0, 'end')

    # off enter funtions to get the ID/Username shown if the user didnt entered anything in the entry
    def on_leave_id(self, e):
        name = self.admin_username.get()
        if name == '':
            self.admin_username.insert(0, 'ID/Username')

    def on_enter_pass(self, e):
        name = self.admin_pass1.get()
        if name == 'Password':
            self.admin_pass1.delete(0, 'end')

    def on_leave_pass(self, e):
        name = self.admin_pass1.get()
        if name == '':
            self.admin_pass1.insert(0, 'Password')

    def on_enter_pass_confirm(self, e):
        name = self.admin_pass_confirm.get()
        if name == 'Confirm Password':
            self.admin_pass_confirm.delete(0, 'end')

    def on_leave_pass_confirm(self, e):
        name = self.admin_pass_confirm.get()
        if name == '':
            self.admin_pass_confirm.insert(0, 'Confirm Password')

    def create_account(self):
        # Connecting to the users database
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
            """)
            conn.commit()

            username = self.admin_username.get()
            password = self.admin_pass1.get()
            confirm_password = self.admin_pass_confirm.get()

            # Validate input
            if username == 'ID/Username' or not username.strip():
                messagebox.showerror('Error', 'Invalid or unavailable username')
                return

            # Check if the two passwords entered are the same
            if password != confirm_password:
                messagebox.showerror('Error', 'Passwords do not match')
                return

            # Check for the password length
            if len(password) < 4:
                messagebox.showerror('Error', 'Password must be at least 6 characters long')
                return

            # Make sure if there is spaces or not
            if password.count(" ") > 0:
                messagebox.showerror('Error', 'Password can not have spaces')
                return

            # Insert account into database
            cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()

            self.signup_master.destroy()
            messagebox.showinfo('Success', 'Account has been created')

        except sqlite3.IntegrityError:
            messagebox.showerror('Error', 'Username already exists')
        except Exception as e:
            messagebox.showerror('Error', f'An unexpected error occurred: {e}')
        finally:
            conn.close()