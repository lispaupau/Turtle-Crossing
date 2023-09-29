from turtle import Turtle
import random

COLORS = ['purple', 'green', 'orange', 'black', 'blue']


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = 0.2

    def spawn_car(self):
        random_chance = random.randint(1, 100)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def speed_increase(self):
        self.speed += 0.1


