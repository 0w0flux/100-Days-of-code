import turtle
import random

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.pensize(10)
timmy.speed(0)

color_list =["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan", "magenta", "lime", "navy", "olive", "aqua", "gold", "violet"]
direction = [0, 90, 180, 270]

def repeat():
    global timmy
    for _ in range(250):
        timmy.pencolor(random.choice(color_list))
        timmy.setheading(random.choice(direction))
        timmy.forward(20)

    timmy.penup()    
    timmy.home()
    timmy.pendown()
    
repeat()
repeat()
repeat()
repeat()
repeat()
repeat()
    
screen = turtle.Screen()
screen.exitonclick()

