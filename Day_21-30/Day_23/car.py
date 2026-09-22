import turtle
import random

colors = [
    "#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF",
    "#00FFFF", "#FFA500", "#FFC0CB", "#FFD700", "#ADFF2F",
    "#40E0D0", "#7FFF00", "#FF1493", "#1E90FF", "#8A2BE2",
    "#00CED1", "#FF4500", "#9ACD32", "#6495ED", "#FF69B4"
]

LANES = list(range(-210, 271, 30))

class Car(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(colors))
        self.shape("square")
        self.shapesize(1.5, 3)
        self.penup()

        self.random_spawn()

    def random_spawn(self):
        self.setheading(random.choice([0, 180]))
        lane_y = random.choice(LANES)
        
        if self.heading() == 180:
            offset = random.randint(0, 600)
            self.teleport(350 + offset, lane_y)
        else:
            offset = random.randint(0, 600)
            self.teleport(-350 - offset, lane_y)

    def movement(self, speed):
        if self.heading() == 180:
            self.goto(self.xcor() - speed, self.ycor())
        else:
            self.goto(self.xcor() + speed, self.ycor())
    
    def respawn(self):
        if self.heading() == 180 and self.xcor() <= -350:
            new_x = random.randint(350, 800)
            new_lane = random.choice(LANES)
            if random.random() < 0.3:
                self.setheading(0)
                new_x = -new_x
            self.teleport(new_x, new_lane)
            
        elif self.heading() == 0 and self.xcor() >= 350:
            new_x = random.randint(-800, -350)
            new_lane = random.choice(LANES)
            if random.random() < 0.3:
                self.setheading(180)
                new_x = -new_x
            self.teleport(new_x, new_lane)