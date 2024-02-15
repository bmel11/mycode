#!/usr/bin/env python3

# Create a script that executes commands on your behalf

from subprocess import call

call(["ip", "link", "show", "up"])
print("This program will check you interfaces.")
interface = input("Enter an interface, like, ens3: ")
call(["ip", "route", "show", "dev", interface])
call(["ip", "route", "show", "dev", interface])

