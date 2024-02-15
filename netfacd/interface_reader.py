#!/usr/bin/env python3
"""Alta3 Research | Exploring interfaces library"""

import netifaces

def main():
    """runtime"""

    print(netifaces.interfaces())

    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try: # this is a new line, y ou also need to indent to code below this line
            print('MAC: ', end='') # This print statement will always print MAC without an end of line
            print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
            print('IP: ', end='')  # This print statement will always print IP without an end of line
            print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
        except:
            print('Could not collect adapter information') # print an error message

if __name__ == "__main__":
    main()


