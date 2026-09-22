import turtle
import random

shapes = {
    "Triangle": 3,
    "Square": 4,
    "Pentagon": 5,
    "Hexagon": 6,
    "Heptagon": 7,
    "Octagon": 8,
    "Nonagon": 9,
    "Decagon": 10,
    "Hendecagon": 11,
    "Dodecagon": 12,
    "Tridecagon": 13,
    "Tetradecagon": 14,
    "Pentadecagon": 15,
    "Hexadecagon": 16,
    "Heptadecagon": 17,
    "Octadecagon": 18,
    "Enneadecagon": 19,
    "Icosagon": 20
}

turtle_colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "cyan",
    "magenta",
    "turquoise",
    "lime",
    "violet",
    "gold",
    "coral",
    "salmon",
    "skyblue",
    "orchid",
    "teal",
    "plum",
    "khaki"
]

def main():
    color_list = []
    for shape, sides in shapes.items():
        degree = 360 / sides

        # Colors
        while True:
            random_color = random.choice(turtle_colors)
            if random_color not in color_list:
                break

        timmy.color(random_color)
        color_list.append(random_color)
        

        for _ in range(sides):
            timmy.forward(100 * scale)
            timmy.left(degree)
       
if __name__ == "__main__":
    scale = 0.5
    timmy = turtle.Turtle()
    timmy.shape("turtle")
    timmy.pensize(2)
    timmy.speed(0)
    timmy.left(180)

    main()

    screen = turtle.Screen()
    screen.exitonclick()