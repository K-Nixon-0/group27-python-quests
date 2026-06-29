#!/usr/bin/python3

def personalized_greeting(name, quest):
    print(f"Hello {name}, and your Quest is {quest}.")

name = input("What is your name? ")
quest = input("What is your quest? ")

personalized_greeting(name, quest)