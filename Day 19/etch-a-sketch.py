import turtle

def main():
    screen.listen()
    screen.onkey(lambda: move("w"), "w")
    screen.onkey(lambda: move("a"), "a")
    screen.onkey(lambda: move("s"), "s")
    screen.onkey(lambda: move("d"), "d")
    screen.onkey(lambda: move("c"), "c")

def move(key):
    if key == "w":
        timmy.forward(10)
    elif key == "a":
        timmy.left(10)
    elif key == "s":
        timmy.back(10)
    elif key == "d":
        timmy.right(10)
    elif key == "c":
        timmy.clear()
        timmy.teleport(0, 0)

if __name__ == "__main__":
    screen = turtle.Screen()
    timmy = turtle.Turtle()
    timmy.shape("turtle")
    timmy.pensize(2)
    timmy.speed(0)

    timmy.left(90)
    
    main()

    screen.exitonclick()
