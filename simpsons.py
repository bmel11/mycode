#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

eyes = challenge[2][1]
goggles = challenge[2][0]
nothing = challenge[3]
phrase =(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}")
print(phrase)

#From trial list, pull eyes, goggles, and nothing.
eye = trial[2]["goggles"]
goggle = trial[2]["eyes"]
nada = trial[-1]
phrase = (f"My {eye}! The {goggle} do {nada}")
print(phrase)

#From the nightmare list do the same thing

eye = nightmare[0]["user"]["name"]["first"]
goggle = nightmare[0]["kumquat"]
nada = nightmare[0]["d"]
phrase = (f"My {eye}! The {goggle} do {nada}")
print(phrase)
