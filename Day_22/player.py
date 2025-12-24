import turtle

class Player:
    def __init__(self, x, y):
        self.start_x = x
        self.start_y = y
        
        self.head = turtle.Turtle("square")
        self.head.color("white")
        self.head.penup()
        self.head.shapesize(7, 1, 1)
        self.head.goto(x, y)

    def move(self, y_change):
        new_y = self.head.ycor() + y_change
        
        if new_y > 330 or new_y < -330:
            return
        
        self.head.sety(new_y)
    
    def reset(self):
        self.head.goto(self.start_x, self.start_y)

def create_drawer():
    drawer = turtle.Turtle()
    drawer.hideturtle()
    drawer.speed(0)
    drawer.penup()
    drawer.color("white")
    return drawer

def create_score_drawer():
    score_drawer = turtle.Turtle()
    score_drawer.speed(0)
    score_drawer.color("white")
    score_drawer.penup()
    score_drawer.hideturtle()
    score_drawer.goto(0, 350)
    return score_drawer