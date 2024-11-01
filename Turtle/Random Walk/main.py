import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
turtle.colormode(255)
timmy.speed("fastest")

# List of colors
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b)

directions = [0, 90, 180, 270]
# Create a loop for the turtle's random movement with color changes
for _ in range(100):
    timmy.pensize(8)
    timmy.color(random_color())  # Choose a random color from the list
    timmy.forward(30)
    angle = random.choice(directions)  # Choose a random 90-degree angle
    timmy.right(angle)







screen = Screen()
screen.exitonclick()