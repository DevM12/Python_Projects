from turtle import Turtle

STARTING_POSITIONS=[(-380,40),(-380, 20),(-380, 0),(-380, -20),(-380,-40)]
PADDLE_SPEED=20

class MovePaddle:
    def __init__(self):
        self.segments=[]
        self.create_paddle()
        self.head=self.segments[0]
    def create_paddle(self):
        for position in STARTING_POSITIONS:
            user_paddle = Turtle('square')
            user_paddle.color('white')
            user_paddle.setheading(90)
            user_paddle.penup()
            user_paddle.goto(position)
            self.segments.append(user_paddle)
    def move(self):
        if 260 >= self.head.ycor() >= -260:
            for segment in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[segment - 1].xcor()
                new_y = self.segments[segment - 1].ycor()
                self.segments[segment].goto(new_x, new_y)
            self.head.forward(PADDLE_SPEED)
        elif 260 <= self.head.ycor() and self.head.heading()==270:
            for segment in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[segment - 1].xcor()
                new_y = self.segments[segment - 1].ycor()
                self.segments[segment].goto(new_x, new_y)
            self.head.forward(PADDLE_SPEED)
        elif -260 >= self.head.ycor() and self.head.heading()==90:
            for segment in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[segment - 1].xcor()
                new_y = self.segments[segment - 1].ycor()
                self.segments[segment].goto(new_x, new_y)
            self.head.forward(PADDLE_SPEED)
        else:
            pass
    def up(self):
        self.head.setheading(90)
        self.move()

    def down(self):
        self.head.setheading(270)
        self.move()