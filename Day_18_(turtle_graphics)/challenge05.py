import turtle
import random

def main():
    for i in range(num_circles):
        if (i + 1) % 5 == 0 or (i + 1) % 6 == 0 or (i + 1) % 6 == 0:
            timmy.left(angle)
            continue
        timmy.color(random_color())
        timmy.circle(radius)
        timmy.left(angle)
    pass

def random_color():
    r= random.randint(0, 255)
    g= random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

if __name__ == "__main__":
    timmy = turtle.Turtle()
    timmy.shape("turtle")
    timmy.pensize(2)
    timmy.speed(0)
    turtle.colormode(255)
    num_circles = 67

    radius = 100
    distance = 2 * radius
    angle = 360 / num_circles
    
    main()

    screen = turtle.Screen()
    screen.exitonclick()
