import random
from turtle import Turtle,Screen

screen=Screen()

screen.setup(1200,750)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
user_bet=screen.textinput('Make your bet','Which Turtle will win?').lower()
while user_bet not in colors:
    user_bet = screen.textinput(f'Make Your Bet!!', f'Choose between: {colors}').lower()


def create_turtles():
    turs=['red','orange','yellow','green','blue','purple']
    y_positions=[59,177,295,-59,-177,-295]
    i=0
    while i != 6:
        color = colors[i]
        y_axis=y_positions[int(i)]
        turs[i]=Turtle(shape='turtle')
        turs[i].color(color)
        turs[i].penup()
        turs[i].goto(-580,y_axis)
        turs[i].speed(0)
        i+=1
    return turs

turtles=create_turtles()

def run_turtles(bet):
    is_race_on=True
    while is_race_on:
        for tur in turtles:
            speed = random.randint(1, 20)
            tur.forward(speed)
            if tur.xcor()>=580:
                is_race_on=False

                answer = Turtle()
                if tur==bet:
                    answer.write('You Won!!!',font=("Verdana", 15, "normal"),align='center')
                else:
                    answer.write(f'You Lost!! {tur.color()[0].upper()} is the winner',font=("Verdana",15, "normal"),align='center')
                break


run_turtles(user_bet)







screen.exitonclick()