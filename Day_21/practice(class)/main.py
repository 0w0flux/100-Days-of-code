import turtle
import player


def main():
    global p1, p2
    p1 = player.Snake()
    p2 = player.Snake()

    animation()

def animation():
    
    p1.movement()
    p2.movement()

    screen.update()
    screen.ontimer(animation, 150)

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(500, 500)
    screen.bgcolor("black")
    screen.tracer(0)

    main()

    screen.exitonclick()