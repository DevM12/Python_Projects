from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.back(10)
def move_clockwise():
    tim.right(10)
def move_counterclockwise():
    tim.left(10)
def clear_screen():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()




screen.listen()
screen.onkey(key='w',fun=move_forward)
screen.onkey(key='s',fun=move_backward)
screen.onkey(key='d',fun=move_clockwise)
screen.onkey(key='a',fun=move_counterclockwise)
screen.onkey(key='c',fun=clear_screen)



screen.exitonclick()