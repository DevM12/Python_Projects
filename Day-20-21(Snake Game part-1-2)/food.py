import random
from turtle import Turtle
FOOD_SIZE=1

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.food_cor=[]
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x_cor = float(random.randint(-260, 260))
        while x_cor==0:
            x_cor = float(random.randint(-260, 260))
        y_cor = float(random.randint(-260, 260))
        while y_cor==0:
            y_cor = float(random.randint(-260, 260))
        self.goto(x_cor, y_cor)