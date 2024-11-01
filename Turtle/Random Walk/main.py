import random
from turtle import Turtle, Screen

timmy = Turtle()

# List of colors
colors = [
    "red", "blue", "green", "orange", "purple", "yellow",
    "brown", "pink", "cyan", "magenta", "lime", "maroon",
    "navy", "olive", "teal", "coral", "gold", "turquoise"
]

# Create a loop for the turtle's random movement with color changes
for _ in range(100):
    timmy.pensize(5)
    timmy.color(random.choice(colors))  # Choose a random color from the list
    timmy.forward(30)
    angle = random.choice([0, 90, 180, 270])  # Choose a random 90-degree angle
    timmy.right(angle)












screen = Screen()
screen.exitonclick()