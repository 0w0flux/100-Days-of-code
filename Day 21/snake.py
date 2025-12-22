import turtle
import random

def main():
    screen.listen()
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
    
    screen.onkey(lambda: player_movement("d"), "d")
    screen.onkey(lambda: player_movement("a"), "a")
    movement()
    default_movement()
    check_score_change()
    check_wall_collision()
    check_food_collision()
    check_snake_collision()
    screen.update()
    screen.ontimer(game, 75)

def start():
    global h1
    h1 = block(0, 0)
    h2 = block(-20, 0)
    h3 = block(-40, 0)

def player_movement(key):
    global h1, score, old_score
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
        snake[i].goto(x, y)

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
    score_drawer.goto(0, 300)
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
    added_blocks = block(x, y)

def create_food():
    global food
    food = turtle.Turtle("square")
    food.penup()
    food.color("red")
    return food

def draw_food():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    food.goto(x, y)

def check_food_collision():
    global score
    if h1.distance(food) < 20:
        score += 1
        draw_food()

def check_wall_collision():
    global running
    x = h1.xcor()
    y = h1.ycor()

    if x > 290 or x < -290 or y > 290 or y < -290:
        running = False
        return True
    return False

def check_snake_collision():
    global running
    for segment in snake[1:]:
        if h1.distance(segment) < 20:
            running = False
            return True
    return False


if __name__ == "__main__":
    width = 600
    height = 600
    screen = turtle.Screen()
    screen.screensize(width, height)
    screen.title("Snake Game")
    screen.bgcolor("black")
    screen.tracer(0)

    score = 0
    old_score = 0
    snake = []
    direction = 0
    running = True

    main()

    screen.exitonclick()