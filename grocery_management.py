from classes.main_page import Main_Page_Window
from tkinter import Tk
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'db', 'users.db')
csv_path = os.path.join(BASE_DIR, 'db', 'stock.csv')

logo_img_path = os.path.join(BASE_DIR, 'assets', 'saletak_logo.jpg')
signup_img_path = os.path.join(BASE_DIR, 'assets', 'signup_bg.jpg')

def main():
    global root       
    root=Tk()

    #obj=Admin_Page_Window(root)       
    obj = Main_Page_Window(root, db_path, csv_path, logo_img_path, signup_img_path)
    root.mainloop()

if __name__ == "__main__":
    main()