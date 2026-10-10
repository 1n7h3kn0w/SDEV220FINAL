import tkinter as gui
from tkinter import ttk
from tkinter.messagebox import showerror
from FinalClasses import * # The reason I do this rather than just 'import FinalClasses' is that I dont have to do FinalClasses.WHATEVER to access things like this
import File as IO
from pathlib import Path as PATH

# This is where I declare all of my constants

DEBUG = True

# This is the constant for where data is saved
FILE_LOCATION = "Pleasent.data"

ORDERS = {}
FOOD_ITEMS = {}
STORE_ITEMS = {}

NEXT_ORDER_ID = 0
NEXT_FOOD_ID = 0
NEXT_STORE_ID = 0
# This handles reading the file where data should save
if(PATH(FILE_LOCATION).exists()):
    (ORDERS, FOOD_ITEMS, STORE_ITEMS, NEXT_ORDER_ID, NEXT_FOOD_ID, NEXT_STORE_ID) = IO.ReadFile(FILE_LOCATION)
else:
    IO.ClearFile(FILE_LOCATION)

# This is all of the basic window setup
window = gui.Tk()
window.title("Pleasent Market CRUD App")
window.geometry("800x600")

XPAD = 25
YPAD = 25

# These are all of the functions for CRUD

def CREATE():
    match(options.index(dropdown.get())):
        case(0):
            pass
        case(1):
            pass
        case(2):
            pass
        case(_):
            print("There was an error detecting the dropdown box value, exiting now.")
            exit(1)

def READ():
    pass

def UPDATE():
    pass

def DELETE():
    pass

# This is where all of the buttons for the GUI are configured

#This is all of the code for switching between Orders FoodItems and StoreItems
options = ["Orders", "Food Items", "Store Items"]
dropdown = ttk.Combobox(window, values=options, state="readonly")
dropdown.set(options[0])
dropdown.pack(pady=YPAD, padx=XPAD)

#This is all of the code for switching the CRUD UI

container = gui.Frame(window)
container.pack(fill="both", expand=True)


"""
for name in options:
    frame = gui.Frame(container)
    frames[name] = frame
    
    gui.Label(frame, text=f"TEST: {dropdown.get()}").pack(padx=XPAD, pady=YPAD)
"""

# This is all the setup for the pages containers

frames = {
options[0]:gui.Frame(container),
options[1]:gui.Frame(container),
options[2]:gui.Frame(container)
}


def RefreshPage(selected: str) -> None:
        
    frame = frames[selected]
    
    for widget in frame.winfo_children():
        widget.destroy()
    
    match(selected):
        case "Orders":
            status = gui.Label(frame, text="ORDERS") # These are the STATUS of the window
            status.pack()
        case "Food Items":
            status = gui.Label(frame, text="FOOD") # These are the STATUS of the window
            status.pack()
        case "Store Items":
            status = gui.Label(frame, text="STORE") # These are the STATUS of the window
            status.pack()
    
    return

def SwitchWindow(event = None) -> None:
    selected = dropdown.get()
    
    RefreshPage(selected)
    
    for frame in frames.values():
        frame.pack_forget()
    
    frames[selected].pack(fill="both", expand=True)
    
    return

dropdown.bind("<<ComboboxSelected>>", SwitchWindow)

# This runs the loop for displaying the window and handling input

SwitchWindow() # This is to set it to "Orders" by default

window.mainloop()

# This handles outputing the saved data

IO.WriteFile(FILE_LOCATION, (ORDERS, FOOD_ITEMS, STORE_ITEMS, NEXT_ORDER_ID, NEXT_FOOD_ID, NEXT_STORE_ID))