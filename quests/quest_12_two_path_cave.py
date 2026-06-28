#!/usr/bin/python3
correct_password = "PassWord"
entered_password = input("Enter the password: ")

if entered_password == correct_password:
    print("Access Granted")
else:
    print("Access Denied")
