#Veronica Stureborg
#Project 6

#importing the graphics library
from graphics import *


#setting the window size and naming it
win= GraphWin("Stoplight" , 500, 500)


#function that draws the light body
def draw_light_body(x, y, length, width):
    body = Rectangle(Point(x,y), Point(width, length))
    body.setOutline("black")
    body.setFill("white")
    body.draw(win)



#function that draws the lamp
def draw_lamp(color, x, y, radius):
    light = Circle(Point(x, y), radius)
    light.setOutline("black")
    light.setFill(color)
    light.draw(win)



#function that draws the whole traffic light
def draw_traffic_light(x, y):
    draw_light_body(x, y, 60, 120)
    draw_lamp("red", 160, 95, 15)
    draw_lamp("yellow", 160, 130, 15)
    draw_lamp("green", 160, 165, 15)



#calling the function at a specific starting point
draw_traffic_light(200,200)
