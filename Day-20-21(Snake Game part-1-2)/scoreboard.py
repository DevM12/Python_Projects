from turtle import Turtle

FONT=('Arial', 24, 'normal')
ALIGNMENT='center'


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f'Score: {self.score}', False, ALIGNMENT, FONT)
    def game_over(self):
        print("\033[1;31;40m GAME OVER")
        self.update_scoreboard()
        self.goto(0,0)
        self.write('GAME OVER', False, ALIGNMENT, FONT)
        return False
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()