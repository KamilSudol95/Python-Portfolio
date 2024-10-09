import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.new_car()
    car.move()
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            scoreboard.clear()
            scoreboard.game_over()
            time.sleep(1)
            game_is_on = False

    if player.finish():
        scoreboard.clear()
        scoreboard.update()
        player.restart()
        car.restart()

