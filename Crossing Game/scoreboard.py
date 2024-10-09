from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 265)
        self.write(f'Level: {self.level}', False, 'left', FONT)

    def update(self):
        self.level += 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 265)
        self.write(f'Level: {self.level}', False, 'left', FONT)

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(-280, 265)
        self.write('Game Over', False, 'left', FONT)


