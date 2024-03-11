FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()           # hiding the turtle symbol
        self.penup()                # using penup to avoid drawing lines by the turtle
        self.color("black")         # defining text color as black
        self.level = 1              # level variable initialized at zero
        self.update_score()         # calling the update_score method to initially display the score when the object is created

    def update_score(self):
        """method that writes the score in the screen"""
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)


    def increase_level(self):
        """method that increases the level by 1 and displays the new level"""
        self.level += 1
        self.update_score()

    def game_over(self):
        """method that displays Game Over when the player loses"""
        self.home()
        self.write("Game Over!", True, align=ALIGNMENT, font=FONT)