import turtle
import random
from turtle import Turtle, Screen


is_race_on = False
screen = Screen()
screen.setup(width=700, height=500)


# Define color names and hex codes
color_names = ["firebrick", "darkmagenta", "darkslateblue", "darkslategray", "maroon", "darkgreen"]
color_hex = ["#B22222", "#8B008B", "#483D8B", "#2F4F4F", "#800000", "#006400"]
y_position = [-150, -90, -30, 30, 90, 150]

# Create turtles and position them on the screen
turtles = []
for turtle_index in range(6):
    new_turt = Turtle(shape="turtle")
    new_turt.color(color_hex[turtle_index])  # Set color using hex code
    new_turt.penup()
    new_turt.goto(-300, y_position[turtle_index])
    turtles.append(new_turt)

# Display the list of color names to the user and prompt for bet
color_options = "\n".join(color_names)
user_bet = screen.textinput(
    title="Make your Bet",
    prompt=f"Which turtle will win the race? Enter a color from the options below:\n{color_options}"
).lower()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)





screen.exitonclick()
