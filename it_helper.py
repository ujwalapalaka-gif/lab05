#!/usr/bin/env python3
# IT Helper - shows date and a simple menu

import datetime

name = input("Enter your name: ")
print(f"Hello {name}! Today is {datetime.datetime.now().strftime('%Y-%m-%d')}")

print("1) Show help")
print("2) Exit")
choice = input("Choose (1-2): ")

if choice == "1":
    print("Help: This is an IT helper tool!")
else:
    print("Goodbye!")
