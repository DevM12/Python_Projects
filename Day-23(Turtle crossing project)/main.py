import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player=Player()
car_manager=CarManager()
score=Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.score()
    car_manager.move()
    for car in car_manager.cars:
        if car.distance(player)<16:
            player.game_over()
            screen.update()
            game_is_on=False
    if player.ycor()>=280:
        player.next_level()
        car_manager.next_level()
        score.next_level()
    else:
        screen.onkeypress(player.move, 'Up')




screen.exitonclick()