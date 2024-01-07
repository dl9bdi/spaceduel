from turtle import Turtle, Screen
from ship import Ship
from scoreboard import Scoreboard
import time
from random import randint
import winsound

explosion_colors = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (255, 255, 128), (255, 255, 255)]
screen = Screen()
screen.bgcolor("black")
screen.title("Space Duel")
screen.setup(width=1000, height=800)

screen.tracer(0)
screen.colormode(255)

ship1 = Ship(x_pos=-200, y_pos=0, color="blue")
ship2 = Ship(x_pos=200, y_pos=0, color="green")

screen.listen()
screen.onkeypress(ship1.accelerate, "Up")
screen.onkeypress(ship1.turn_left, "Left")
screen.onkeypress(ship1.turn_right, "Right")
screen.onkeypress(ship1.fire, "Down")

screen.onkeypress(ship2.accelerate, "w")
screen.onkeypress(ship2.turn_left, "a")
screen.onkeypress(ship2.turn_right, "d")
screen.onkeypress(ship2.fire, "s")

scoreboard = Scoreboard()
scoreboard.write_text("Go on")


def star_background():
    for i in range(0, 20):
        st_xpos = randint(-500, 500)
        st_ypos = randint(-400, 400)
        scaling = randint(1, 10) / 20
        newstar = Turtle()
        newstar.penup()
        newstar.shape("circle")
        newstar.color("white")
        newstar.shapesize(stretch_wid=scaling, stretch_len=scaling)
        newstar.goto(st_xpos, st_ypos)


def explode(explode_ship):
    explode_ship.shape("circle")
    explode_ship.color("white")
    ship1.ship_bullet.hideturtle()
    ship2.ship_bullet.hideturtle()
    for i in range(0, 5):
        explode_ship.shapesize((i + 1) * 1)
        explode_ship.color(explosion_colors[i])
        # explode_ship.color((1,0,0))
        screen.update()
        time.sleep(0.3)
    time.sleep(0.7)
    explode_ship.hideturtle()
    screen.update()


game_is_on = True
star_background()
while game_is_on:
    if (scoreboard.player1_remaining_ships > 0) and (scoreboard.player2_remaining_ships > 0):
        time.sleep(0.01)
        screen.update()
        ship1.move()
        ship2.move()
        if ship1.distance(ship2) < 20:
            # game_is_on = False
            print("Crash")
            winsound.Beep(440, 300)
            explode(ship1)
            ship1.hideturtle()
            ship2.hideturtle()
            scoreboard.player1_remaining_ships -= 1
            scoreboard.player2_remaining_ships -= 1
            scoreboard.color_ships_left()
            ship1.reset_ship_position()
            ship2.reset_ship_position()
            screen.update()
        if (ship1.ship_bullet.bullet_runs == True) and (ship1.ship_bullet.distance(ship2) < 30):
            # game_is_on = False
            print("Hit by ship1")
            winsound.Beep(1000, 300)

            explode(ship2)
            scoreboard.player2_remaining_ships -= 1
            scoreboard.color_ships_left()
            ship1.reset_ship_position()
            ship2.reset_ship_position()
            screen.update()
        if (ship2.ship_bullet.bullet_runs == True) and (ship2.ship_bullet.distance(ship1) < 30):
            # game_is_on = False
            print("Hit by ship 2")
            winsound.Beep(2000, 300)

            explode(ship1)
            scoreboard.player1_remaining_ships -= 1
            scoreboard.color_ships_left()
            ship1.reset_ship_position()
            ship2.reset_ship_position()

            screen.update()
    else:
        game_is_on = False
if scoreboard.player1_remaining_ships > 0:
    winner = "player 1"
else:
    winner = "player 2"
scoreboard.clear()

scoreboard.goto(-100, 100)
scoreboard.write_text(f"Game over\n winner is {winner}\n Click to end game ")
screen.exitonclick()
