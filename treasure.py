print("Welcome to treasure Island")
print("Your Mission is to find the treasure!")

direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n")
direction = direction.lower()

if direction == 'left':
    choice = input("You've come to a lake. There is an island in the middle of the lake.Type 'wait' to wait for a boat. Type 'swim' to swim acrossn\n")

    choice = choice.lower()

    if choice == 'wait':
        door = input("You arrived safely at the island. Which door do you want to go through? Type 'red' , 'blue', 'yellow'\n")

        door = door.lower()

        if door == 'yellow':
            print("You did it!. The treasure is yours")
        elif door == 'blue':
            print("Eaten by a beast: Game Over!")
        elif door == 'red':
            print("Ooops: You got burned")
        else:
            print("Game Over!")
    else:
        print("Attacked by a trout. Game over!")

else:
    print("Fall into a hole. Game Over!")