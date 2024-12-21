import time
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake game')
screen.tracer(0)
screen.listen()
food=Food()
snake=Snake()
game_score=ScoreBoard()

def play_game():
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food)<15:
            game_score.increase_score()
            food.refresh()
            snake.new_segment()
        if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()< -280:
            game_is_on=game_score.game_over()
        for segment in snake.segments[1:]:
            if snake.head.distance(segment)<10:
                game_is_on=game_score.game_over()
screen.onkey(play_game, 'space')
screen.onkey(snake.right_arrow, 'Right')
screen.onkey(snake.up_arrow, 'Up')
screen.onkey(snake.left_arrow, 'Left')
screen.onkey(snake.down_arrow, 'Down')










screen.exitonclick()

