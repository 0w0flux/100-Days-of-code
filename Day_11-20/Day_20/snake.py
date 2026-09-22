import turtle

def main():
    screen.listen()
    start()
    game()

def game():
    if not running:
        return
    
    screen.onkey(lambda: player_movement("d"), "d")
    screen.onkey(lambda: player_movement("a"), "a")
    movement()
    default_movement()
    screen.update()
    screen.ontimer(game, 100)

def start():
    global h1
    h1 = block(0, 0)
    h2 = block(-20, 0)
    h3 = block(-40, 0)

def player_movement(key):
    global h1
    if key == "a":
        h1.left(90)
    elif key == "d":
        h1.right(90)

def default_movement():
    h1.forward(20)
    pass

def movement():
    for i in range(len(snake) - 1, 0, -1):
        x = snake[i - 1].xcor()
        y = snake[i - 1].ycor()
        print(x, y)
        snake[i].goto(x, y)

def block(x, y):
    global snake
    block = turtle.Turtle("square")
    block.color("#75ff53")
    block.penup()
    block.goto(x, y)
    snake.append(block)
    return block

if __name__ == "__main__":
    width = 600
    height = 600
    screen = turtle.Screen()
    screen.screensize(width, height)
    screen.title("Snake Game")
    screen.bgcolor("black")
    screen.tracer(0)

    score = 0
    old_score = -1
    snake = []
    direction = 0
    running = True

    main()

    screen.exitonclick()