#!/usr/bin/python3

has_key = input("Do you have a key? (yes/no): ").lower()

if has_key == "yes":
    key_color = input("Is it the right color? (yes/no): ").lower()
    
    if key_color == "yes":
        print("You found the treasure!")
    else:
        print("Wrong color. Game over.")
else:
    direction = input("Do you go left or right? (left/right): ").lower()
    
    if direction == "left":
        action = input("Do you swim or wait? (swim/wait): ").lower()
        
        if action == "swim":
            print("You find a treasure!")
        else:
            print("Nothing happens. Game over.")
    else:
        print("You hit a dead end. Game over.")