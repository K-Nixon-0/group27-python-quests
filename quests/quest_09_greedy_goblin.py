#!/usr/bin/python3
gold_pieces = 27
friends = 4

each_friend_gets = gold_pieces // friends
goblin_keeps = gold_pieces % friends

print(f"Every friend will get {each_friend_gets} gold pieces, and goblin will keep {goblin_keeps}.")

