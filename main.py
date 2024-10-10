import tkinter as tk
from file_organizer import organize_files
import os

#Create the main window


root = tk.Tk()
root.title("Simple Input and Button GUI")
root.geometry("300x150")  # Set the window sizeFunction to be called when the button is clicked


def submit_function():
    address = entry.get()  # Get text from the entry box
    print("Address:", address)#Label for entry
    if os.path.exists(address):
        organize_files(address)


label = tk.Label(root, text="Enter directory address:")
label.pack(pady=10)  # Add padding around the labelEntry (input block) where user can type text


entry = tk.Entry(root, width=30)
entry.pack(pady=5)#Button to trigger the function show_input


button = tk.Button(root, text="Submit", command=submit_function)
button.pack(pady=10)#Start the GUI event loop

root.mainloop()



