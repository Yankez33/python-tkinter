import tkinter as tk
from tkinter import ttk  # a submodule of tkinter that binds newer widgets added in V 8.5

root = tk.Tk()
root.title("Feet to Meters")

# Create a content frame. Using a themed frame inside the window ensures bg matches content for better overall
# appearance
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky='NWES')  # defines positioning within parent element
root.columnconfigure(0, weight=1)  # tells tk to fill any extra space if window is resized
root.rowconfigure(0, weight=1)  # tells tk to fill any extra space if window is resized:


# Perform the calculation
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


# Create the Entry widget
feet = tk.StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)  # needs to identify parent widget as first parameter(
# mainframe. WIDTH sets the entry to 7 characters
feet_entry.grid(column=2, row=1, sticky="WE")

# Create remaining widgets and position in appropriate spot
meters = tk.StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky="WE")

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky="W")

ttk.Label(mainframe, text="feet").grid(column=1, row=1, sticky="W")
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky="E")
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky="W")

# Add polish to app
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)  # adds padding around all the widgets
feet_entry.focus()  # tells tk to focus on entry so cursor starts there
root.bind("<Return>", calculate)  # tells tk when return key is clicked, it should call our routine

root.mainloop()

