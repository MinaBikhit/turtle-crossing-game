COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()                               # hiding the turtle symbol
        self.penup()                                    # using penup to avoid drawing lines by the turtle
        self.car_speed = STARTING_MOVE_DISTANCE         # car speed variable initialized at STARTING_MOVE_DISTANCE
        self.cars = []                                  # cars list that will contain the generated cars

    def generate_car(self):
        """method that generates a car object based on the turtle class and appends it to the cars list"""
        random_ycor = random.randint(-250, 250)
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.goto(300, random_ycor)
        self.cars.append(car)

    def generate_cars(self):
        """method that calls the generate car method based on random chance in order to generate a flow of cars"""
        chance = random.randint(1, 6)
        if chance == 1:
            self.generate_car()

    def increase_speed(self):
        """method that increase the car speed by MOVE_INCREMENT"""
        self.car_speed += MOVE_INCREMENT

    def move_cars(self):
        """method that moves the car objects across the screen and then removes them to save memory"""
        for car in self.cars:
            if car.xcor() < -420:
                self.cars.remove(car)
            else:
                car.backward(self.car_speed)
