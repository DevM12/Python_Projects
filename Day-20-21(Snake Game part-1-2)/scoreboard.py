from turtle import Turtle

FONT=('Arial', 24, 'normal')
ALIGNMENT='center'


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open('data.txt') as data:
            self.high_score=int(data.read())
        self.color('white')
        self.hideturtle()
        self.goto(0, 260)
        self.penup()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score={self.high_score}', False, ALIGNMENT, FONT)
    def game_over(self):
        if self.score>self.high_score:
            with open('data.txt',mode='w') as data:
                data.write(f'{self.score}')
        with open('data.txt') as data:
            self.high_score=int(data.read())
        self.score=0
        self.update_scoreboard()
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()