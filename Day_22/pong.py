import turtle
import random
import player

def main():
    screen.listen()
    start()
    game()

def start():
    global p1, p2, score_drawer
    p1 = player.Player(x=-400, y=0)
    p2 = player.Player(x=400, y=0)

    drawer = player.create_drawer()
    drawer.pensize(2.5)
    drawer_movement(drawer, 800)
    drawer.hideturtle()

    score_drawer = player.create_score_drawer()
    draw_score(score_drawer)
    score_drawer.hideturtle()


    screen.onkeypress(lambda: key_down("w"), "w")
    screen.onkeyrelease(lambda: key_up("w"), "w")
    screen.onkeypress(lambda: key_down("s"), "s")
    screen.onkeyrelease(lambda: key_up("s"), "s")
    screen.onkeypress(lambda: key_down("Up"), "Up")
    screen.onkeyrelease(lambda: key_up("Up"), "Up")
    screen.onkeypress(lambda: key_down("Down"), "Down")
    screen.onkeyrelease(lambda: key_up("Down"), "Down")
    screen.onkey(lambda: move_character("c"), "c")
    screen.onkey(lambda: move_character("b"), "b")
    
def game():
    if not running:
        print(f"Game Over")
        return

    if keys_pressed["w"]:
        p1.move(20)
    if keys_pressed["s"]:
        p1.move(-20)
    if keys_pressed["Up"]:
        p2.move(20)
    if keys_pressed["Down"]:
        p2.move(-20)


    check_score_change()
    screen.update()
    screen.ontimer(game, 75)

def move_character(key):
    global p1_score, p2_score
    if key == "c":
        p1_score += 1
    elif key == "b":
        p2_score += 1

def key_down(key):
    keys_pressed[key] = True

def key_up(key):
    keys_pressed[key] = False
    
def drawer_movement(drawer, height):
    dash_length = 20
    gap_length = 15

    drawer.goto(0, height // 2)
    drawer.setheading(270)
    drawer.forward(gap_length/2)

    while drawer.ycor() > -height // 2:
        drawer.pendown()
        drawer.forward(dash_length)
        drawer.penup()
        drawer.forward(gap_length)

def draw_score(score_drawer):
    score_drawer.clear()
    score_drawer.write(
        f"{p1_score}      {p2_score}",
        align="center",
        font=("Arial", 24, "normal")
    )

def check_score_change():
    global p1_score, old_p1_score, p2_score, old_p2_score
    if p1_score > old_p1_score:
        draw_score(score_drawer)
        old_p1_score = p1_score
        return 0
    
    elif p2_score > old_p2_score:
        draw_score(score_drawer)
        old_p2_score = p2_score
        return 1
    pass

if __name__ == "__main__":
    width = 1000
    height = 800
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    running = True
    p1_score = 0
    old_p1_score = 0
    p2_score = 0
    old_p2_score = 0
    
    keys_pressed = {
    "w": False,
    "s": False,
    "Up": False,
    "Down": False
    }

    main()

    screen.exitonclick()