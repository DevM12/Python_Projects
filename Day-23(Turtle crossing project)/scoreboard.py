from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.hideturtle()
        self.penup()
        self.goto(-220,260)
        self.level=1
    def score(self):
        self.write(f'Level: {self.level}',False,'center',FONT)
    def next_level(self):
        self.level+=1
        self.clear()
    pass
