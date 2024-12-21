import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


def position_car(car):
    rand_y = float(random.randint(-230, 280))
    if rand_y%20==0:
        car.goto(280, rand_y)
        car.setheading(180)
    else:
        position_car(car)

class CarManager:
    def __init__(self):
        self.cars=[]
        self.cars_generator()
        self.speed=STARTING_MOVE_DISTANCE
    def cars_generator(self):
        for _ in range(0,20):
            rand_color=random.randint(0,5)
            color=COLORS[rand_color]
            car=Turtle('square')
            car.color(color)
            car.shapesize(stretch_len=2)
            car.penup()
            rand_x = float(random.randint(100, 280))
            rand_y = float(random.randint(-250, 280))
            car.goto(rand_x, rand_y)
            car.setheading(180)
            self.cars.append(car)
    def next_level(self):
        self.speed+=MOVE_INCREMENT
    def move(self):
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor()<=-280:
                position_car(car)
    pass
