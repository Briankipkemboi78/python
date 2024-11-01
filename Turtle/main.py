from turtle import Turtle, Screen

timmy = Turtle()

num_sides = 4
while num_sides <= 10:

    angle = 360 / num_sides

    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)
        timmy.color("cyan")

    num_sides += 1

screen = Screen()
screen.exitonclick()
 