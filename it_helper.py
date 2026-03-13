#!/usr/bin/env python3
# IT Helper - shows date and a simple menu

import datetime

import datetime

name = input("Enter your name: ")
print(f"Hello {name}, today's date is", datetime.datetime.now().strftime("%Y-%m-%d"))

while True:
    print("\nIT Helper Menu:")
    print("1. Show date")
    print("2. Exit")
    choice = input("Pick 1 or 2: ")
    
    if choice == "1":
        print("Today's date:", datetime.datetime.now().strftime("%Y-%m-%d"))
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice - pick 1 or 2")

