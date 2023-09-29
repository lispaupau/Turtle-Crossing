from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color('black')
        self.hideturtle()
        self.level_count()

    def level_count(self):
        self.goto(-220, 250)
        self.write(f'Level: {self.level}', align='center', font=('Courier', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Courier', 20, 'normal'))

    def level_up(self):
        self.clear()
        self.level += 1
        self.level_count()
