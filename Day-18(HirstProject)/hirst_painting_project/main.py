import random
from turtle import Turtle,Screen,colormode
import colorgram

colormode(255)
colors = colorgram.extract('image.jpg',80)
all_colors=[]
for i in colors:
    red=i.rgb[0]
    green=i.rgb[1]
    blue=i.rgb[2]
    all_colors.append([red,green,blue])
print(all_colors)

timmy=Turtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(500)
timmy.setheading(0)
def random_rgb_color():
    random_color=tuple(random.choice(all_colors))
    print(random_color)
    return random_color
def dot_generator(tur):
    for _ in range(10):
        tur.dot(50,random_rgb_color())
        tur.penup()
        tur.forward(80)
    tur.penup()
    tur.left(90)
    tur.forward(80)
    tur.left(90)
    tur.forward(800)
    tur.left(180)
for _ in range(10):
    dot_generator(timmy)




screen=Screen()
screen.exitonclick()