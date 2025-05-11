import tkinter as tk
from tkinter import messagebox

class Restaurant:
    def __init__(self, root):
        self.order_number = 0

        root.grid_rowconfigure(1, weight=1)  
        root.grid_columnconfigure(0, weight=1)  
        root.grid_columnconfigure(2, weight=0)

        self.menu_frame = tk.Frame(root, width = 700, height = 100, bg = "lightgray")
        self.menu_frame.grid(column= 0, row= 0, sticky= "new")
        self.food_frame = tk.Frame(root, width= 700, height= 700, bg= "darkgray")
        self.food_frame.grid(column= 0, row= 0, sticky= "esw")
        self.price_frame = tk.Frame(root, width= 300, height= 800, bg= "black")
        self.price_frame.grid(column= 2, row= 0, sticky= "nes")
        self.appetisers_frame = tk.Frame(root, width= 700, height=700, bg= "green")
        self.main_frame = tk.Frame(root, width= 700, height=700, bg= "blue")
        self.soups_frame = tk.Frame(root, width= 700, height=700, bg= "red")
        self.drinks_frame = tk.Frame(root, width= 700, height=700, bg= "green")
        self.section1 = tk.Frame(self.main_frame, width=100, height=100, bg= "yellow")



        self.app_button = tk.Button(self.menu_frame, text= "Appetisers", command= self.appetisers)
        self.app_button.place(x= 80, y= 40)

        self.main_button = tk.Button(self.menu_frame, text= "Main Courses", command= self.mains)
        self.main_button.place(x= 240, y= 40)

        self.soup_button = tk.Button(self.menu_frame, text= "Soups", command= self.soup)
        self.soup_button.place(x= 420, y= 40)

        self.drink_button = tk.Button(self.menu_frame, text= "Drinks", command= self.drinks)
        self.drink_button.place(x= 560, y= 40)

    def appetisers(self):
        self.food_frame.grid_forget()
        self.main_frame.grid_forget()
        self.drinks_frame.grid_forget()
        self.soups_frame.grid_forget()
        self.appetisers_frame.grid(column= "0", row= "0", sticky= "esw")
        self.app_button.configure(state= "disabled", bg="darkgray")
        self.main_button.configure(state= "normal", bg= "white")
        self.main_frame.grid_propagate(False)
        self.soup_button.configure(state= "normal", bg= "white")
        self.drink_button.configure(state= "normal", bg= "white")


    def mains(self):
        self.food_frame.grid_forget()
        self.appetisers_frame.grid_forget()
        self.drinks_frame.grid_forget()
        self.soups_frame.grid_forget()
        self.main_frame.grid_forget()    
        self.main_button.configure(state= "disabled", bg="darkgray")
        self.soup_button.configure(state= "normal", bg= "white")
        self.drink_button.configure(state= "normal", bg= "white")
        self.app_button.configure(state= "normal", bg= "white")
        self.main_frame.grid(column=0, row= 1, sticky= "nsew")
        tk.Label(self.main_frame, text="Main Courses Section", bg="white", font=("Arial", 24)).pack(pady=50)
        self.section1.place(x= 0, y= 0)


    def soup(self):
        self.food_frame.grid_forget()
        self.main_frame.grid_forget()
        self.drinks_frame.grid_forget()
        self.soups_frame.grid_forget()
        self.soups_frame.grid(column= "0", row= "0", sticky= "esw")
        self.soup_button.configure(state= "disabled", bg="darkgray")
        self.drink_button.configure(state= "normal", bg= "white")
        self.main_button.configure(state= "normal", bg= "white")
        self.app_button.configure(state= "normal", bg= "white")

    def drinks(self):
        self.food_frame.grid_forget()
        self.main_frame.grid_forget()
        self.drinks_frame.grid_forget()
        self.soups_frame.grid_forget()
        self.drinks_frame.grid(column= "0", row= "0", sticky= "esw")
        self.drink_button.configure(state= "disabled", bg= "darkgrey")
        self.soup_button.configure(state= "normal", bg= "white")
        self.main_button.configure(state= "normal", bg= "white")
        self.app_button.configure(state= "normal", bg= "white")





if __name__ == "__main__":
    root = tk.Tk()
    order = Restaurant(root)
    root.title("Menu")
    root.geometry("1000x800")
    root.resizable(False, False)
    root.mainloop()
