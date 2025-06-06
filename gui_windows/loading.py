from tkinter import *

class LoadingBox:
    def __init__(self, parent, message="Loading, please wait..."):
        self.parent = parent
        self.loading_box = Toplevel(parent)
        self.loading_box.title("Loading")
        self.loading_box.geometry("200x100")
        self.loading_box.resizable(False, False)
        self.loading_box.transient(parent)  # Set as a child of the parent window
        self.loading_box.grab_set()  # Make modal

        # Center the loading window
        x = parent.winfo_x() + (parent.winfo_width() // 2) - 100
        y = parent.winfo_y() + (parent.winfo_height() // 2) - 50
        self.loading_box.geometry(f"+{x}+{y}")

        # Add a label for the message
        self.label = Label(self.loading_box, text=message, font=("Arial", 12))
        self.label.pack(expand=True, pady=20)

    def close(self):
        """Close the loading box."""
        self.loading_box.destroy()