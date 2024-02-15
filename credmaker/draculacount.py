#!/usr/bin/python3

# Write a script that count the number of times vampire is written in the book.

counter = 0

with open("dracula.txt","r") as foo: # read content in Dracula novel
    with oper("dracula.txt","r", "w") as fang:
        for line in foo:  # loop over every line in Dracula, print # of times "vampire" appears
            if "vampire" in line.lower():
            counter += 1 # this is the same as counter = count + 1
            fang.write(line)

print(counter)
