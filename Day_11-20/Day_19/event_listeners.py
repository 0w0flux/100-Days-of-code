import turtle
import random

def main():
    screen.listen()
    screen.onkey(lambda: move("w"), "w")
    screen.onkey(lambda: move("a"), "a")
    screen.onkey(lambda: move("s"), "s")
    screen.onkey(lambda: move("d"), "d")

def move(key):
    timmy.color(random_color())
    if key == "w":
        timmy.forward(10)
    elif key == "a":
        timmy.left(90)
    elif key == "s":
        timmy.back(10)
    elif key == "d":
        timmy.right(90)

def random_color():
    r= random.randint(0, 255)
    g= random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

if __name__ == "__main__":
    screen = turtle.Screen()
    timmy = turtle.Turtle()
    timmy.shape("turtle")
    timmy.pensize(2)
    timmy.speed(0)
    turtle.colormode(255)
    timmy.color(random_color())
    timmy.left(90)
    
    main()

    screen.exitonclick()