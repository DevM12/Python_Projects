from turtle import Turtle,Screen

screen=Screen()

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_SPEED=20

RIGHT=0
UP=90
LEFT=180
DOWN=270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.loc=[]

    def new_segment(self):
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        self.segments.append(new_segment)
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.new_segment()
    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(SNAKE_SPEED)
        self.loc=[self.head.xcor(),self.head.ycor()]
    def right_arrow(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def left_arrow(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def up_arrow(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down_arrow(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
