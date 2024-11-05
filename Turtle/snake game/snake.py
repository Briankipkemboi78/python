import turtle
from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


x_positions = [-60, -40, -20]

# Create turtles and position them on the screen
all_turtles = []
for index in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")  # Set color using hex code
    new_turtle.penup()
    new_turtle.goto(x_positions[index], 0)
    all_turtles.append(new_turtle)




















screen.exitonclick()