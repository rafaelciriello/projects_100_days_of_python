#Treasure Island
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

# using nested conditional structures "if", "elif" e "esle"
left_right = input("Your plane just crashed on the island! You can choose whether to go 'right' or 'left'? ").lower()
if left_right == "left":
    swin_wait = input("You have come to a deep river. I would like to 'swim' or 'wait' for a boat? ").lower()
    if swin_wait == "wait":
        door = input("Which door, blue, yellow or red? ").lower()
        if door == "blue":
            print("Game over! You just freeze to death!")
        elif door == "red":
            print("Game over! You've just been burned alive!")
        else:
            print("You win! Sunflowers are yellow!")
    else:
        print("Game over! You've just been eaten by crocodiles!")
else:
    print("Game over! Wild jaguars live in this area. You got bad!")
