from turtle import Turtle,Screen,mainloop
import pandas

data=pandas.read_csv('50_states.csv')
states=data['state'].tolist()

screen=Screen()
screen.title('U.S. States game')

img='blank_states_img.gif'
screen.addshape(img)
tim=Turtle(img)


s=Turtle()
s.hideturtle()
s.penup()

guessed_states=[]
count=0
cont_game=True
while cont_game and len(guessed_states)<50:
    answer_state=screen.textinput(f'Guessed states:{count}/50','Write name of the state').title()
    if answer_state=='Exit':
        cont_game=False
    if (answer_state in states) and (answer_state not in guessed_states):
        state=data[data.state==answer_state]
        guessed_states.append(answer_state)
        x,y=state.x.item(),state.y.item()
        s.goto((x,y))
        s.write(answer_state)
        count+=1
if count<50:
    missed_states=[s for s in states if s not in guessed_states]
    new_data=pandas.DataFrame(missed_states)
    new_data.to_csv('states_to_learn.csv')
mainloop()