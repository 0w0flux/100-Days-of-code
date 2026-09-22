import turtle
import player, ball as ball_class

def main():
    screen.listen()
    start()
    game()

def start():
    global p1, p2, score_drawer, ball, game_over
    p1 = player.Player(x=-400, y=0)
    p2 = player.Player(x=400, y=0)

    ball = ball_class.Ball()

    drawer = player.create_drawer()
    drawer.pensize(2.5)
    drawer_movement(drawer, height)
    drawer.hideturtle()

    score_drawer = player.create_score_drawer()
    draw_score(score_drawer)
    score_drawer.hideturtle()

    game_over = False

    screen.onkeypress(lambda: key_down("w"), "w")
    screen.onkeyrelease(lambda: key_up("w"), "w")
    screen.onkeypress(lambda: key_down("s"), "s")
    screen.onkeyrelease(lambda: key_up("s"), "s")
    screen.onkeypress(lambda: key_down("Up"), "Up")
    screen.onkeyrelease(lambda: key_up("Up"), "Up")
    screen.onkeypress(lambda: key_down("Down"), "Down")
    screen.onkeyrelease(lambda: key_up("Down"), "Down")
    screen.onkeypress(restart_game, "r")

def restart_game():
    global p1_score, p2_score, old_p1_score, old_p2_score, ball_hit_count, game_over
    p1_score = 0
    p2_score = 0
    old_p1_score = 0
    old_p2_score = 0
    ball_hit_count = 0
    game_over = False
    
    p1.reset()
    p2.reset()
    ball.reset()
    draw_score(score_drawer)
    
    score_drawer.goto(0, 350)
    score_drawer.clear()
    draw_score(score_drawer)

def game():
    if not running or game_over:
        return

    if keys_pressed["w"]:
        p1.move(10)
    if keys_pressed["s"]:
        p1.move(-10)
    if keys_pressed["Up"]:
        p2.move(10)
    if keys_pressed["Down"]:
        p2.move(-10)

    ball.move()
    ball_collision()
    score_change()
    check_score_change()
    check_win_condition()

    screen.update()
    screen.ontimer(game, 16)

def score_change():
    global p1_score, p2_score, ball_hit_count
    if ball.body.xcor() < -500:
        p2_score += 1
        ball_hit_count = 0
        ball.reset()
        p1.reset()
        p2.reset()

    if ball.body.xcor() > 500:
        p1_score += 1
        ball_hit_count = 0
        ball.reset()
        p1.reset()
        p2.reset()

def check_win_condition():
    global game_over
    if p1_score >= WINNING_SCORE:
        game_over = True
        show_winner("PLAYER 1 WINS!")
    elif p2_score >= WINNING_SCORE:
        game_over = True
        show_winner("PLAYER 2 WINS!")

def show_winner(message):
    score_drawer.goto(0, 0)
    score_drawer.clear()
    score_drawer.write(message, align="center", font=("Arial", 48, "bold"))
    
    restart_drawer = turtle.Turtle()
    restart_drawer.speed(0)
    restart_drawer.color("white")
    restart_drawer.penup()
    restart_drawer.hideturtle()
    restart_drawer.goto(0, -50)
    restart_drawer.write("Press R to restart", align="center", font=("Arial", 24, "normal"))

def key_down(key):
    keys_pressed[key] = True

def key_up(key):
    keys_pressed[key] = False

def ball_collision():
    global ball_hit_count
    
    if ball.body.ycor() > 390 or ball.body.ycor() < -390:
        ball.bounce_y()

    paddle_hit = False
    
    p1_left = p1.head.xcor() - PADDLE_WIDTH // 2
    p1_right = p1.head.xcor() + PADDLE_WIDTH // 2
    p1_top = p1.head.ycor() + PADDLE_HEIGHT // 2
    p1_bottom = p1.head.ycor() - PADDLE_HEIGHT // 2
    
    p2_left = p2.head.xcor() - PADDLE_WIDTH // 2
    p2_right = p2.head.xcor() + PADDLE_WIDTH // 2
    p2_top = p2.head.ycor() + PADDLE_HEIGHT // 2
    p2_bottom = p2.head.ycor() - PADDLE_HEIGHT // 2
    
    ball_left = ball.body.xcor() - BALL_SIZE // 2
    ball_right = ball.body.xcor() + BALL_SIZE // 2
    ball_top = ball.body.ycor() + BALL_SIZE // 2
    ball_bottom = ball.body.ycor() - BALL_SIZE // 2
    
    if (ball_right > p1_left and ball_left < p1_right and
        ball_bottom < p1_top and ball_top > p1_bottom and ball.x_change < 0):
        hit_offset = ball.body.ycor() - p1.head.ycor()
        ball.bounce_x_with_angle(hit_offset)
        ball.body.setx(p1_right + BALL_SIZE // 2 + 2)
        paddle_hit = True
    
    if (ball_right > p2_left and ball_left < p2_right and
        ball_bottom < p2_top and ball_top > p2_bottom and ball.x_change > 0):
        hit_offset = ball.body.ycor() - p2.head.ycor()
        ball.bounce_x_with_angle(hit_offset)
        ball.body.setx(p2_left - BALL_SIZE // 2 - 2)
        paddle_hit = True
    
    if paddle_hit:
        ball_hit_count += 1
        update_ball_speed()

def update_ball_speed():
    global ball_hit_count
    
    if ball_hit_count >= 3:
        current_speed = (ball.x_change**2 + ball.y_change**2)**0.5
        
        if current_speed < MAX_BALL_SPEED:
            increase_factor = 1.1
            ball.x_change *= increase_factor
            ball.y_change *= increase_factor
            
            print(f"Ball speed: {current_speed:.1f} → {(ball.x_change**2 + ball.y_change**2)**0.5:.1f}")
        
        ball_hit_count = 0

def drawer_movement(drawer, height):
    dash_length = 20
    gap_length = 15

    drawer.goto(0, height // 2)
    drawer.setheading(270)
    drawer.forward(gap_length / 2)

    while drawer.ycor() > -height // 2:
        drawer.pendown()
        drawer.forward(dash_length)
        drawer.penup()
        drawer.forward(gap_length)

def draw_score(score_drawer):
    score_drawer.goto(0, 350)
    score_drawer.clear()
    score_drawer.write(
        f"{p1_score}      {p2_score}",
        align="center",
        font=("Arial", 24, "normal")
    )
    print("------------Score-------------")
    print(f"Player 1: {p1_score} \nPlayer 2: {p2_score}")
    print("-------------------------------")

def check_score_change():
    global p1_score, old_p1_score, p2_score, old_p2_score
    if p1_score > old_p1_score:
        draw_score(score_drawer)
        old_p1_score = p1_score
    elif p2_score > old_p2_score:
        draw_score(score_drawer)
        old_p2_score = p2_score

if __name__ == "__main__":
    PADDLE_WIDTH = 20
    PADDLE_HEIGHT = 140
    BALL_SIZE = 20
    WINNING_SCORE = 10
    MAX_BALL_SPEED = 15

    width = 1000
    height = 800
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.bgcolor("black")
    screen.title("Pong | R: Restart")
    screen.tracer(0)

    running = True
    game_over = False
    p1_score = 0
    old_p1_score = 0
    p2_score = 0
    old_p2_score = 0
    ball_hit_count = 0

    keys_pressed = {
        "w": False,
        "s": False,
        "Up": False,
        "Down": False
    }

    main()
    screen.exitonclick()