import turtle
import random

def main():
    screen.listen()
    screen.onkey(lambda: player_movement("a"), "Left")
    screen.onkey(lambda: player_movement("d"), "Right")
    start()
    create_score()
    draw_score()
    create_food()
    draw_food()
    game()

def game():
    if not running:
        print(f"You died! Score: {score}")
        return
    
    snake_movement()
    check_score_change()
    check_wall_collision()
    check_food_collision()
    check_snake_collision()
    screen.update()
    screen.ontimer(game, 75)

def start():
    global h1
    h1 = block(0, 0)
    block(-20, 0)
    block(-40, 0)
    
def player_movement(key):
    global direction
    if key == "a":
        h1.left(90)
        if direction != "right":
            direction = "left"
    elif key == "d":
        h1.right(90)
        if direction != "left":
            direction = "right"

def snake_movement():
    prev_x = h1.xcor()
    prev_y = h1.ycor()

    h1.forward(20)

    for i in range(1, len(snake)):
        x = snake[i].xcor()
        y = snake[i].ycor()
        snake[i].goto(prev_x, prev_y)
        prev_x, prev_y = x, y

def block(x, y):
    global snake
    block = turtle.Turtle("square")
    block.color("#75ff53")
    block.penup()
    block.goto(x, y)
    snake.append(block)
    return block

def create_score():
    global score_drawer
    score_drawer = turtle.Turtle()
    score_drawer.hideturtle()
    score_drawer.penup()
    score_drawer.color("white")
    score_drawer.goto(0, 240)
    return score_drawer

def draw_score():
    score_drawer.clear()
    score_drawer.write(
        f"Score: {score}",
        align="center",
        font=("Arial", 30, "normal")
    )

def check_score_change():
    global score, old_score
    if score > old_score:
        create_block()
        draw_score()
        old_score = score
        print(f"Score: {score}")

def create_block():
    x = snake[len(snake)-1].xcor()
    y = snake[len(snake)-1].ycor()
    block(x, y)

def create_food():
    global food
    food = turtle.Turtle("square")
    food.penup()
    food.color("red")
    return food

def draw_food():
    x = random.randrange(-280, 281, 20)
    y = random.randrange(-280, 281, 20)
    food.goto(x, y)

def check_food_collision():
    global score
    if h1.distance(food) < 20:
        score += 1
        draw_food()

def check_wall_collision():
    global running
    if abs(h1.xcor()) > 290 or abs(h1.ycor()) > 290:
        running = False

def check_snake_collision():
    global running
    for segment in snake[1:]:
        if h1.distance(segment) < 15:
            running = False

if __name__ == "__main__":
    width = 600
    height = 600
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title("Snake Game")
    screen.bgcolor("black")
    screen.tracer(0)

    score = 0
    old_score = 0
    snake = []
    running = True
    direction = None

    main()

    screen.exitonclick()