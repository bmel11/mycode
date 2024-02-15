#!/usr/bin/env python3

import crayons

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.blue("Handshaking")}. .. ... connection with {ip}') # fstring
        # we will learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attmepting to send command --> {mycmds}')
            # we will learn to write code that sends cmds to device here
    
    return None

# start our main script
def main():
    """called at runetime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    devicecmd = {"10.1.000.1":["interface eth1/1", "no shutdown"], "10.2.0.1":["interface eth1/1", "showdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 

    print(f"Welcome to the {crayons.green('Network')} Device Command Pusher") # welcome message

    ## get data set
    print("\n Data set found\n") # replace with fx call that read data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices

# call our main fx
main()
