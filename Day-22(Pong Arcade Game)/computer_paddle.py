from turtle import Turtle


STARTING_POSITIONS=[(380,40),(380, 20),(380, 0),(380, -20),(380,-40)]
PADDLE_SPEED=20

class ComputerPaddle:
    def __init__(self):
        self.segments=[]
        self.create_paddle()
        self.head=self.segments[0]
    def create_paddle(self):
        for position in STARTING_POSITIONS:
            computer_paddle = Turtle('square')
            computer_paddle.color('white')
            computer_paddle.setheading(90)
            computer_paddle.penup()
            computer_paddle.goto(position)
            self.segments.append(computer_paddle)
    def direction(self):
        if self.head.ycor()>=270:
            self.head.setheading(270)
        elif self.head.ycor()<=-270:
            self.head.setheading(90)
    def move(self):
        self.direction()
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(PADDLE_SPEED)