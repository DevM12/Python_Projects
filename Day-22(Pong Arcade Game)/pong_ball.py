from turtle import Turtle

BALL_SPEED=30
class Ball:
    def __init__(self):
        self.ball=Turtle('circle')
        self.x = 365
        self.y = 0
        self.create_ball()
        self.dir=135
        self.movement=['','']
    def create_ball(self):
        self.ball.color('white')
        self.ball.turtlesize(.5)
        self.ball.penup()
        self.ball.goto(self.x,self.y)
    def reset(self):
        self.ball.goto(self.x,self.y)
        self.dir=135
        self.ball.setheading(self.dir)
        self.movement=['','']
    def move_ball(self):
        self.ball.setheading(self.dir)
        self.ball.forward(BALL_SPEED)
    def left(self):
        self.dir=180
        self.movement[0] = 'left'
        self.move_ball()
    def right(self):
        self.dir=0
        self.movement[0] = 'right'
        self.move_ball()
    def down(self):
        self.movement[1] = 'down'
        self.y -= 5
        self.move_ball()
    def up(self):
        self.y += 5
        self.movement[1] = 'up'
        self.move_ball()