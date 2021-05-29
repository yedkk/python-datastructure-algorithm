
# This program is graphic program to ask the data from users and return the windchill
# Kangdong Yuan

# Import the mode
from tkinter import *

# Set the class
class windchillconvert:

# Set the function
    def __init__(self):

# Set the Tk as root
        root = Tk()

# Set the Label for text and entry space
        self.title = Label(root, text="WindChill Calculator", fg="red",bg="yellow").grid(row=0,column=0)
        self.theLable= Label(root, text="Enter the temperature in degrees Fahrenheit:")
        self.theLable.grid(row=1,column=0)
        self.temp = Entry(root)
        self.temp.grid(row=1,column=1)
        self.theLable1 =Label(root,text="Enter the wind speed in mph: ")
        self.theLable1.grid(row=2,column=0)
        self.wind =Entry(root)
        self.wind.grid(row=2,column=1)

# Set the button and connect the button to function
        self.result = Button(root, text="Calculate windchill", command=self.windchill)
        self.result.grid(row=3,column=1)
        self.answer = Label(root, text="The windchill is : ")
        self.answer.grid(row=4, column=0)
        self.answer1 = Label(root, text="degree Fahrenheit")
        self.answer1.grid(row=4, column=2)

# Set the value to return value
        self.value = StringVar()
        self.number = Label(root, textvariable=self.value)
        self.number.grid(row=4,column=1)
        root.mainloop()

# Set the windchill function
    def windchill(self):
        t = float(self.temp.get())
        w = float(self.wind.get())
        wind_chill = 35.74 + 0.6215 * t - 35.75 * w**0.16 + 0.4275 * t * w**0.16
        wind_chill = round(wind_chill,2)

# Set the value callback
        self.value.set(wind_chill)

# Run this programs
start = windchillconvert()
