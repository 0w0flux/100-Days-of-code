import turtle
import random

color_list = [(101, 190, 171), (100, 164, 209), (207, 137, 182), (213, 230, 240), (56, 179, 154), (49, 124, 170), (187, 222, 211), (217, 163, 85)]

def main():
    timmy.goto(-200, -200)
    y = -200
    x = -200
    for row in range(10):
        for col in range(9):
            timmy.dot(30, random.choice(color_list))
            timmy.forward(50)
        y += 50
        timmy.goto(x, y)


if __name__ == "__main__":
    timmy = turtle.Turtle()
    timmy.shape("turtle")
    timmy.speed("fastest")
    turtle.colormode(255)
    timmy.penup()
    
    main()
    timmy.pos()

    screen = turtle.Screen()
    screen.exitonclick()

