from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1_remaining_ships = 3
        self.player2_remaining_ships = 3
        self.ships_player1 = []
        self.ships_player2 = []
        self.draw_ships()
        self.pencolor("yellow")
        self.penup()
        self.hideturtle()
        self.goto(-100, 350)

    def draw_ships(self):
        for i in range(0, 3):
            ship_left = Turtle()
            ship_left.penup()
            ship_left.shapesize(stretch_len=2, stretch_wid=2)
            ship_left.setheading(90)
            ship_left.color("blue")
            ship_left.goto(-450 + 30 * i, 380)
            self.ships_player1.append(ship_left)

        for i in range(0, 3):
            ship_left = Turtle()
            ship_left.penup()
            ship_left.shapesize(stretch_len=2, stretch_wid=2)
            ship_left.setheading(90)
            ship_left.color("green")
            ship_left.goto(380 + 30 * i, 380)
            self.ships_player2.append(ship_left)

    def color_ships_left(self):
        for ships in self.ships_player1:
            ships.color("black")
        for i in range(0, self.player1_remaining_ships):
            self.ships_player1[i].color("blue")

        for ships in self.ships_player2:
            ships.color("black")
        for i in range(0, self.player2_remaining_ships):
            self.ships_player2[i].color("green")

    def write_text(self, outtext):
        self.write(outtext, font=("Arial", 22, "normal"))