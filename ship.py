from turtle import Turtle
from math import sqrt, sin, cos, radians
from bullet import Bullet


class Ship(Turtle):
    def __init__(self, x_pos, y_pos, color):
        super().__init__()

        self.shapesize(stretch_len=4, stretch_wid=4)
        self.penup()
        self.setheading(90)
        self.color(color)
        self.startcolor = color
        self.start_x_pos = x_pos
        self.start_y_pos = y_pos
        self.goto(x_pos, y_pos)
        self.vx = 0
        self.vy = 0
        # self.x_move = 1
        # self.y_move = 1
        self.speed_step = 1
        self.ax = 1
        self.ay = 1
        self.ship_bullet = Bullet()
        self.maxspeed = 10

    def reset_ship_position(self):
        self.vx = 0
        self.vy = 0
        # self.x_move = 1
        # self.y_move = 1
        self.speed_step = 1
        self.ax = 1
        self.ay = 1
        self.color(self.startcolor)
        self.showturtle()
        self.goto(self.start_x_pos, self.start_y_pos)
        self.shape("classic")
        self.setheading(90)
        self.ship_bullet.reset_bullet(self)

    def move(self):

        new_x = self.xcor() + self.vx
        new_y = self.ycor() + self.vy
        self.goto(new_x, new_y)
        # self.forward(self.x_move)
        if self.xcor() > 500:
            self.setx(-500)
        if self.xcor() < -500:
            self.setx(500)
        if self.ycor() > 400:
            self.sety(-400)
        if self.ycor() < -400:
            self.sety(400)
        if self.ship_bullet.bullet_runs == True:
            self.ship_bullet.move()

    def accelerate(self):
        len_v = sqrt(self.ax ** 2 + self.ay ** 2)
        dir = radians(self.heading())
        self.vx += len_v * cos(dir)
        self.vy += len_v * sin(dir)

        if sqrt(self.vx ** 2 + self.vy ** 2) > self.maxspeed:
            self.vx -= len_v * cos(dir)
            self.vy -= len_v * sin(dir)

    def turn_left(self):
        direction = self.heading()
        direction += 10
        direction = direction % 360
        self.setheading(direction)
        # print("Turn left", direction)

    def turn_right(self):
        direction = self.heading()
        direction -= 10
        direction = direction % 360

        self.setheading(direction)
        # print("Turn right", direction)

    def fire(self):
        # print("In Ship Fire")
        # print (self.xcor(), self.ycor())
        # self.ship_bullet.start_bullet(int(self.xcor()), int(self.ycor()), self.heading())
        self.ship_bullet.start_bullet(self)

    def explode(self):
        pass
        # self.ship_bullet.shape("circle")
        # self.ship_bullet.shapesize(20)
