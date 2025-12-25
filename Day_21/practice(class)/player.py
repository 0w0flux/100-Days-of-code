import turtle
import random

class Snake(turtle.Turtle):

    def __init__(self):
        super().__init__("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.movement()
        
    def movement(self):
        x_coord = random.randint(-230, 230)
        y_coord = random.randint(-230, 230)
        self.goto(x_coord, y_coord)
