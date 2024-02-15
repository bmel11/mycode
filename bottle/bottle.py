#!/usr/bin/env python3

#Create a script that will output ALL 99 lines of the song 99 b ottles of beer on the wall.

def bottles(a):
    print(str(a) + "  bottles of beer on the wall,")
    print(str(a) + "  bottles of beer.")
    print("Take one down, pass it around")
    print(str(a) + "  bottles of beer on the wall.")

a = 5
if a > 1:
    bottles(a-1)
bottles = 5
