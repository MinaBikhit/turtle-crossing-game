STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")                    # choosing the turtle shape as turtle
        self.color("black")                     # choosing color for the turtle object
        self.penup()                            # penup to avoid line drawing by turtle
        self.setheading(90)                     # set heading used to make the turtle face up
        self.goto(STARTING_POSITION)            # setting the initial position of the turtle based on the tuple

    def move_up(self):
        """method that moves the turtle up by MOVE_DISTANCE"""
        y_cor = self.ycor() + MOVE_DISTANCE       # alternately we can use self.forward(MOVE_DISTANCE)
        self.goto(self.xcor(), y_cor)


    def reset(self):
        """method that resets the turtle to the starting position"""
        self.goto(STARTING_POSITION)

    def at_finish_line(self):
        """method that detects if the turtle is at the finish line"""
        return self.ycor() > FINISH_LINE_Y
