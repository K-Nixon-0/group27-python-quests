#!/usr/bin/python3

def age_entry():
    age = int(input("Enter your age: "))
    return age


def vote_eligibility(age):
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")


age_entry = ask_for_age()
vote_eligibility(user_age)
