import turtle
import random

class Ball:
    def __init__(self):
        self.body = turtle.Turtle("square")
        self.body.color("white")
        self.body.penup()
        self.body.goto(0, 0)

        self.base_speed = 8 
        self.speed_multiplier = 1 

        self.x_change = self.base_speed
        self.y_change = random.choice([-4, -3, -2, 2, 3, 4])

        self.max_speed = 12 
        self.min_y_speed = 2

    def move(self):
        self.body.setx(self.body.xcor() + self.x_change * self.speed_multiplier)
        self.body.sety(self.body.ycor() + self.y_change * self.speed_multiplier)

    def bounce_y(self):
        self.y_change *= -1

    def bounce_x_with_angle(self, hit_offset):
        max_angle_speed = 6

        self.x_change *= -1

        self.y_change = (hit_offset / 40) * max_angle_speed

        if abs(self.y_change) < self.min_y_speed:
            self.y_change = self.min_y_speed if self.y_change >= 0 else -self.min_y_speed

        self.y_change += random.uniform(-1, 1)

        speed = (self.x_change ** 2 + self.y_change ** 2) ** 0.5
        if speed > self.max_speed:
            factor = self.max_speed / speed
            self.x_change *= factor
            self.y_change *= factor

    def reset(self):
        self.body.goto(0, 0)
        self.x_change = self.base_speed * (-1 if random.choice([True, False]) else 1)
        self.y_change = random.choice([-4, -3, -2, 2, 3, 4])