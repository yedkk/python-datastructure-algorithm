# This program ask user to give sides and return graph to users
# Author Kangdong Yuan

# import random and turtle
import random
import turtle
t = turtle.Turtle()

# set the function
def makePolygon (sides,length,width,fillColor,angle,borderColor):

# fill the color
    t.color(borderColor,fillColor)
    t.begin_fill()

# draw the graph
    for i in range(sides):
        t.color(borderColor,fillColor)
        t.pensize(width)
        t.forward(length)
        t.right(angle)
    t.end_fill()

# get the color and sides from user
colors = ['coral','gold','brown','red','green','blue','yellow','purple','orange','cyan','pink','magenta','goldenrod']
sides = int(input("Enter the number of sides, less 3 to exit."))

# set a while loop to ensure enter less 3 to exit
while sides >= 3:
    turtle.home()

# calculate the length width angle and get color from random
    length = 600/sides
    width = (sides%20)+1
    borderColor = colors[random.randint(0,12)]
    fillColor = colors[random.randint(0,12)]
    angle = 360/sides
    makePolygon(sides,length, width, fillColor,angle,borderColor)
    sides = int(input("Enter the number of sides, less 3 to exit."))






