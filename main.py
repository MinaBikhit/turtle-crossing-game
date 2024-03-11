import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()                               # generating a screen object
screen.setup(width=600, height=600)             # adjusting the dimensions of the screen object
screen.title("Turtle Crossing")                 # choosing the title of the screen object
screen.tracer(0)                                # disabling the tracer function for smoother performance

player = Player()                               # creation of a player object
car_manager = CarManager()                      # creation of a car_manager object
scoreboard = Scoreboard()                       # creation of a scoreboard object

screen.listen()                                 # using the listen method to allow keyboard presses to affect the game
screen.onkey(player.move_up, "Up")         # using onkey method to assign right player move up method to the up key

game_is_on = True                               # the game on variable for the while loop
while game_is_on:
    time.sleep(0.1)                             # using the sleep method to control the refresh rate
    screen.update()                             # calling the update method to refresh the screen in every iteration
    car_manager.move_cars()
    car_manager.generate_cars()

    #Detect if the turtle crossed successfully
    if player.at_finish_line():
        player.reset()
        car_manager.increase_speed()
        scoreboard.increase_level()

    #detect collision with cars
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
screen.exitonclick()                          # exit on click method is called to avoid closing of the screen
