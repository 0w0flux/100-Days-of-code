import turtle
import random

def main():
    global user_guess, finished

    red = character("red", 0)
    green = character("green", 50)
    blue = character("blue", -50)
    yellow = character("yellow", 100)
    purple = character("purple", -100)

    finish()

    user_guess = screen.textinput(title="Make a guess!", prompt=f"chose a color: {colors}")
    print(user_guess)
    all_turtles = [red, green, blue, yellow, purple]
    for i in range(1000):
        if finished == False:
            move(all_turtles)
        else:
            break

def character(color, y):
    x = turtle.Turtle()
    x.shape("turtle")
    x.pensize(5)
    x.speed(0)
    x.color(color)
    x.goto(width / -2.1, y)
    x.clear()
    return x

def finish():
    line.goto(finish_line, -240)
    line.pendown()
    line.goto(finish_line, 240)
    line.penup()
    line.teleport(10000, 10000)

def move(turtle):
    global user_guess, finished
    finished = False
    while not finished:
        for i in turtle:
            i.forward(random.randint(3, 10)) 
            if i.xcor() >= finish_line:
                win = i.color()[0]
                if win == user_guess:
                    print(f"Your guess is right! {win} won!") 
                else:
                    print(f"Your guess is wrong! {win} won! ")
                finished = True
                break   

colors = ["red", "green", "blue", "yellow", "purple"]

if __name__ == "__main__":
    screen = turtle.Screen()
    width = 1000
    height = 600
    finish_line = 480
    screen.setup(width, height)

    line = character("black", 0)
    line.penup()
    
    global user_guess, finished
    user_guess = None
    finished = False
    main()
    screen.exitonclick()
