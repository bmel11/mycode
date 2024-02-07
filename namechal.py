#!/usr/bin/python3
# print question
print("What is your name?")
# pause and collect input (wait for ENTER)
name = input()
# print question
print("What day of the week is it?")
# pause and collect input (wait for ENTER)
weekday = input()
# This is an f-string
print(f"Hello, {name}!  Happy {weekday}!")

# This way is more complicated
#print("Hello, "  name + "Today is " + weekday + "Happy " + weekday!)
