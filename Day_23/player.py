import turtle

class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.teleport(0, -280)

    def wall_collision(self):
        x = self.xcor()
        y = self.ycor()
        if y < -290:
            self.sety(-275)
        if x > 290:
            self.setx(275)
        elif x < -290:
            self.setx(-275)
        
    def movement(self, key):
        if key == "w":
            self.goto(self.xcor(), self.ycor() + 30)
        elif key == "s":
            self.goto(self.xcor(), self.ycor() - 30)
        elif key == "a":
            self.goto(self.xcor() - 30, self.ycor())
        elif key == "d":
            self.goto(self.xcor() + 30, self.ycor())

    def reset(self):
        self.teleport(0, -280)

class LevelDrawer(Player):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.teleport(-280, 260)
        self.pendown()

    def write_level(self, level):
        self.clear()
        self.write(f"Level: {level}", move=False, align="left", font=("Arial", 16, "normal"))

    def game_over(self, level):
        self.clear()
        self.teleport(0, 0)
        self.write(f"Game Over! \nYour level: {level}", move=False, align="center", font=("Arial", 30, "normal"))
        
