import time
from turtle import  Screen
from paddle import MovePaddle
from computer_paddle import ComputerPaddle
from pong_ball import Ball
from score_board import Score

screen=Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong Game')
screen.listen()
screen.tracer(0)

score=Score()

move_paddle=MovePaddle()
computer_paddle=ComputerPaddle()
ball=Ball()
ball.down()
def play_game():
    while True:
        screen.update()
        time.sleep(0.1)
        move_paddle.move()
        computer_paddle.move()
        score.score_board()
        if ball.ball.xcor()<-360:
            for segment in move_paddle.segments:
                if segment.distance(ball.ball) < 10:
                    if ball.movement[1]=='up':
                        ball.dir-=90
                    else:
                        ball.dir+=90
            if ball.ball.xcor()<-420:
                score.computer+=1
                ball.reset()

        elif ball.ball.xcor()>360:
            for segment in computer_paddle.segments:
                if segment.distance(ball.ball) < 10:
                    if ball.movement[1]=='up':
                        ball.dir+=90
                        ball.move_ball()
                    else:
                        ball.dir-=90
                        ball.move_ball()
            if ball.ball.xcor()>420:
                print(score.player)
                score.player+=1
                ball.reset()
        elif ball.ball.ycor()<=-280:
            if ball.movement[0]=='left':
                ball.dir-=90
                ball.move_ball()
            else:
                ball.dir+=90
                ball.move_ball()
        elif ball.ball.ycor()>=280:
            if ball.movement[0]=='left':
                ball.dir+=90
                ball.move_ball()
            else:
                ball.dir-=90
                ball.move_ball()
        ball.move_ball()

screen.onkey(play_game,'space')
screen.onkey(move_paddle.up,'Up')
screen.onkey(move_paddle.down,'Down')







screen.exitonclick()