import turtle
from car import Car
from player import Player, LevelDrawer


def main():
    global player, level_drawer
    screen.listen()
    player = Player()
    level_drawer = LevelDrawer()
    level_drawer.write_level(level)
    spawn_cars()
    
    screen.onkeypress(lambda: player.movement("w"), "Up")
    screen.onkeypress(lambda: player.movement("a"), "Left")
    screen.onkeypress(lambda: player.movement("s"), "Down")
    screen.onkeypress(lambda: player.movement("d"), "Right")

    game_loop()

def game_loop():
    global player
    if not running:
        level_drawer.game_over(level)
        return
    
    car_collision()
    player.wall_collision()
    move_cars(get_current_speed())
    level_handler()

    for car in cars:
        car.respawn()

    screen.update()
    screen.ontimer(game_loop, 16)

def car_collision():
    global running
    for car in cars:
        if player.distance(car) < 25:
            running = False

def spawn_cars():
    global cars
    
    for i in range(25):
        tmp_car = Car()
        cars.append(tmp_car)

def move_cars(speed):
    for car in cars:
        car.movement(speed)

def get_current_speed():
    speed_index = min(level - 1, len(speed_list) - 1)
    return speed_list[speed_index]

def level_handler():
    global level
    if player.ycor() >= 290:
        level += 1
        player.reset()
        level_drawer.write_level(level)

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.title("Turtle Crossing")
    screen.bgcolor("black")
    screen.tracer(0)

    running = True
    level = 1
    cars = []
    speed_list = [5, 7, 10, 12, 15, 17, 20, 25, 30, 35, 40, 45, 50]

    main()

    screen.exitonclick()