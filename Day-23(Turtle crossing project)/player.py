from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed=5
        self.shape('turtle')
        self.configure_player()
    def configure_player(self):
        self.penup()
        self.setheading(90)
        self.penup()
        self.position_reset()
    def position_reset(self):
        self.goto(STARTING_POSITION)
    def next_level(self):
        self.position_reset()
    def move(self):
        self.forward(self.speed)
    def game_over(self):
        self.shape('square')
        self.color('red')
        self.write('Game Over')
    pass
