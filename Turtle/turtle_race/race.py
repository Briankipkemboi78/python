import turtle
import random
from turtle import Turtle, Screen

# Initialize race settings
is_race_on = False
screen = Screen()
screen.setup(width=700, height=500)

# Define color names and hex codes
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-150, -90, -30, 30, 90, 150]

# Create turtles and position them on the screen
all_turtles = []
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])  # Set color using hex code
    new_turtle.penup()
    new_turtle.goto(-300, y_positions[index])
    all_turtles.append(new_turtle)


user_bet = screen.textinput(
    title="Make Your Bet",
    prompt=f"Which turtle will win the race? Enter a color from the options below:\n{colors}"
).lower()

# Start the race if the user made a bet
if user_bet:
    is_race_on = True

# Run the race
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 300:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
            is_race_on = False  # Stop the race
            break  # Exit the for loop once we have a winner

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# Keep the window open until clicked
screen.exitonclick()
