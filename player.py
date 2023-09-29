from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.left(90)
        self.start_position()

    def move(self):
        self.forward(20)

    def start_position(self):
        self.goto(0, -280)
