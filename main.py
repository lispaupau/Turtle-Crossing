from turtle import Screen
from player import Player
from cars import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)

player = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    screen.update()
    # Spawn and move cars
    car_manager.spawn_car()
    car_manager.move_car()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

    # Level up
    if player.ycor() > 280:
        player.start_position()
        score.level_up()
        car_manager.speed_increase()

screen.exitonclick()
