import random
import turtle
from turtle import Turtle,Screen
turtle.colormode(255)
def random_rgb_color():
    color=[]
    for _ in range(3):
        color.append(random.randint(0,255))
    return tuple(color)
def random_turtle_color():
    colors=[
        'yellow','gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray', 'white'
            ]
    color = random.choice(colors)
    return color
def shapes(tur,sides,direction):
    tur.color(random_rgb_color())
    angle=360/sides
    if direction=='left':
        for _ in range(sides):
            tur.forward(100)
            tur.left(angle)
    if direction == 'right':
        for _ in range(sides):
            tur.forward(100)
            tur.right(angle)
def dotted_line(tur,distance):
    for _ in range(int(distance/10)):
        tur.forward(5)
        tur.penup()
        tur.forward(5)
        tur.pendown()
def random_walk(tur,steps):
   def rand_turn(t):
       directions=[90,180,270,360]
       turn=random.choice(['left','right'])
       if turn=='right':
           t.right(random.choice(directions))
       else:
           t.left(random.choice(directions))
   for _ in range(steps):
       tur.color(random_turtle_color())
       tur.forward(50)
       rand_turn(tur)
def spirograph(tur):
    for _ in range(50):
        tur.left(7.3)
        tur.color(random_rgb_color())
        tur.circle(100)

    for _ in range(7):
        tur.forward(100)
        for _ in range(50):
            tur.left(7.3)
            tur.color(random_rgb_color())
            tur.circle(50)
        tur.right(180)
        tur.forward(100)
        tur.right(135)


timmy=Turtle()
timmy.shape('turtle')
tom=Turtle()
tom.shape('turtle')


timmy.width(1)
timmy.speed(0)


spirograph(timmy)



# random_rgb_color()
# random_walk(timmy,100)


# for i in range(7):
#     shapes(timmy,i+3,'left')
# for i in range(7):
#     shapes(tom,i+3,'right')

# dotted_line(tom,100)

# tom.forward(50)
# square(timmy)




screen=Screen()
screen.exitonclick()