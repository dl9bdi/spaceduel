from turtle import Turtle
from math import sqrt, sin, cos, radians


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=0.4, stretch_wid=0.4)
        self.penup()
        # self.setheading(90)
        self.shape("circle")
        self.color("white")

        self.run_length = 40
        self.bullet_runs = False
        self.bullet_ran_so_far = 0
        self.hideturtle()
        self.vx = 0
        self.vy = 0

    def move(self):
        if self.bullet_ran_so_far < self.run_length:
            new_x = self.xcor() + self.vx
            new_y = self.ycor() + self.vy
            # print (self.vx, self.vy)
            self.goto(new_x, new_y)
            if self.xcor() > 500:
                self.setx(-500)
            if self.xcor() < -500:
                self.setx(500)
            if self.ycor() > 400:
                self.sety(-400)
            if self.ycor() < -400:
                self.sety(400)
            self.bullet_ran_so_far += 1
        else:
            self.bullet_runs = False
            self.hideturtle()

    # def start_bullet(self, start_x, start_y, direction):
    def start_bullet(self, firing_ship):
        if self.bullet_runs == False:
            self.bullet_runs = True
            self.bullet_ran_so_far = 0
            self.vx = 0
            self.vy = 0
            self.goto(firing_ship.xcor(), firing_ship.ycor())
            # len_v = sqrt(self.ax ** 2 + self.ay ** 2)
            len_v = 20
            dir = radians(firing_ship.heading())
            # print(f"länge v {len_v} Richtung {dir} sin(dir) {sin(dir)} cos(dir) {cos(dir)}")
            self.vx += firing_ship.vx + len_v * cos(dir)
            self.vy += firing_ship.vy + len_v * sin(dir)
            self.showturtle()

    def reset_bullet(self, firing_ship):
        self.shape("circle")
        self.color("white")
        self.goto(firing_ship.xcor(), firing_ship.ycor())
        self.run_length = 40
        self.bullet_runs = False
        self.bullet_ran_so_far = 0
        self.hideturtle()
        self.vx = 0
        self.vy = 0
