import datetime
import tkinter as tk
from PIL import Image, ImageTk

# creating the window and title
root = tk.Tk()
root.geometry('620x780')
root.title("Age Calculator")

# Creating the labels
name = tk.Label(text="Name")
name.grid(column=0, row=1)
year = tk.Label(text="Year")
year.grid(column=0, row=2)
month = tk.Label(text="Month")
month.grid(column=0, row=3)
date = tk.Label(text="Day")
date.grid(column=0, row=4)

# Creating the input fields for each label and placing them on the right side of matching label
nameEntry = tk.Entry()
nameEntry.grid(column=1, row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1, row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1, row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1, row=4)


# Defining a function to get user inputs.
def getInput():
    name = nameEntry.get()
    # create a Person object and pass name and birthdate to __init__ method of that class
    user = Person(name, datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get())))
    textArea = tk.Text(master=root, height=10, width=25)
    textArea.grid(column=1, row=6)
    answer = "Hey {user}!!. You are {age} years old!!.".format(user=name, age=user.age())
    textArea.insert(tk.END, answer)


# Create a button for the user to submit their input values. The button gets linked to the getInput function
button = tk.Button(root, text="Calculate Age", command=getInput, fg="red")
button.grid(column=1, row=5)


# Define the Person class. Define the __init__ method and the age method will will calculate age from user input
class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):  # calculates user age from given input
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age


# Add image to app strictly for appearance
image = Image.open('images/age.jpg')
image.thumbnail((300, 300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)


root.mainloop()
