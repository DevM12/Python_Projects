from turtle import Turtle

INITIAL_POSITIONS=[(-200,280),(200,280)]

class Score:
    def __init__(self):
        self.player=0
        self.computer=0
        self.players=[]
        self.create_players()
        self.player_score=self.players[0]
        self.computer_score=self.players[1]
    def create_players(self):
        for position in INITIAL_POSITIONS:
            new_player=Turtle()
            new_player.color('white')
            new_player.penup()
            new_player.hideturtle()
            new_player.goto(position)
            self.players.append(new_player)
    def score_board(self):
        self.player_score.clear()
        self.computer_score.clear()
        self.player_score.write(f'Player Score: {self.player}')
        self.computer_score.write(f'Computer Score: {self.computer}')

