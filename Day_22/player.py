import turtle

class Player:
    def __init__(self, x, y):
        
        self.head = create_character()
        self.mid = create_character()
        self.bottom = create_character()

        self.head.goto(x, y)
        self.mid.goto(x, y + 20)
        self.bottom.goto(x, y + 40)

        self.parts = [self.head, self.mid, self.bottom]

    def move(self, y_change):
        for part in self.parts:
            part.goto(part.xcor(), part.ycor() + y_change)

def create_character():
    char = turtle.Turtle("square")
    char.color("white")
    char.penup()
    return char

def create_drawer():
    drawer = create_character()
    drawer.hideturtle()
    drawer.speed(0)
    drawer.penup()
    return drawer

def create_score_drawer():
    score_drawer = turtle.Turtle()
    score_drawer.color("white")
    score_drawer.penup()
    score_drawer.speed(0)
    score_drawer.goto(0, 350)
    return score_drawer


