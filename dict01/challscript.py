#!/usr/bin/env python3

def main():
    
    marvelchars= {
        "Starlord":
        {"real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"},

        "Mystique":
        {"real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"},

        "Hulk":
        {"real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"}
        }
    #Ask which character they want to learn about             
    
    char_name = input(" Which character do you want to know about? (Starlord, Mystique, Hulk): " )
    char_name = char_name.capitalize()
    
    #Ask what statistic they want to know about
    
    char_stat = input("Which statistic do you want to know?: ")
    char_stat = char_stat.lower()

    #Print a function that combines char name + stat
    print(f"{char_name}'s {char_stat} is: {marvelchars}")
