print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = input("Do you want to go left or right?").lower()
if choice != "left":
    print("Fall into a hole.\nGame Over.")
else:
    mobility = input("Do you want to swim or wait").lower()
    if mobility != "wait":
        print("Attacked by trout\nGame Over.")
    else:
        door = input("Select a door: Red, Yellow, Blue").lower()
        if door == "red":
            print("Burned by fire.\nGame Over.")
        elif door == "yellow":
            print("You Win!")
        elif door == "blue":
            print("Eaten by beasts.\nGame Over.")
        else:
            print("Game Over.")
