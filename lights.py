#!/usr/bin/python3
"""This module controls my Philips Hue lights."""

import sys               # import system functions
from phue import Bridge  # import Bridge from phue

BRIDGE = Bridge('10.0.0.215') # connects to the philips hue bridge

# If no arguments, print intro
if len(sys.argv) == 1:
    print('\033[94m\033[1mConnected to Philips Hue Bridge\033[0m\n')

    # Check light status, display right info
    if BRIDGE.get_light(1, 'on') is False and BRIDGE.get_light(2, 'on') is False:
        print('None of your lights are on.\n')
    elif BRIDGE.get_light(1, 'on') and BRIDGE.get_light(2, 'on') is False:
        print('Your seahorse light is on.\n')
    elif BRIDGE.get_light(1, 'on') is False and BRIDGE.get_light(2, 'on'):
        print('Your bedroom light is on.\n')
    elif BRIDGE.get_light(1, 'on') and BRIDGE.get_light(2, 'on'):
        print('All your lights are on.\n')

    # Ask for lights to modify and how
    WHICH = input('\033[1mWhich lights? (Both, Bedroom, or Seahorse) \033[0m')
    STATE = input('\033[1mOn or off? \033[0m')
elif len(sys.argv) == 2: # if it has arguments, set them
    STATE = sys.argv[1]
    WHICH = 'both'
    BRIGHTNESS = 255
elif len(sys.argv) > 2:
    WHICH = sys.argv[1]
    STATE = sys.argv[2]
    try:
        BRIGHTNESS = int(sys.argv[3])
    except IndexError:
        BRIGHTNESS = 255
    except ValueError:
        BRIGHTNESS = 255

if STATE == 'on' or STATE == '1' or STATE == '': # if on, ask for brightness
    if len(sys.argv) == 1:
        BRIGHTNESS = input('Brightness? (1-255) ')
        if BRIGHTNESS == '':
            BRIGHTNESS = 255

    if WHICH == 'both' or WHICH == '2' or WHICH == '':
        BRIDGE.set_light([1, 2], 'on', True)
        BRIDGE.set_light([1, 2], 'bri', int(BRIGHTNESS))

    elif WHICH == 'seahorse' or WHICH == 'sea' or WHICH == 's' or WHICH == '1':
        BRIDGE.set_light(1, 'on', True)
        BRIDGE.set_light(1, 'bri', int(BRIGHTNESS))

    elif WHICH == 'bedroom' or WHICH == 'bed' or WHICH == 'b' or WHICH == '2':
        BRIDGE.set_light(2, 'on', True)
        BRIDGE.set_light(2, 'bri', int(BRIGHTNESS))

elif STATE == 'off' or STATE == '0':
    if WHICH == 'both' or WHICH == '3' or WHICH == '':
        BRIDGE.set_light([1, 2], 'on', False)

    elif WHICH == 'seahorse' or WHICH == 'sea' or WHICH == 's' or WHICH == '0':
        BRIDGE.set_light(1, 'on', False)

    elif WHICH == 'landing' or WHICH == 'bed' or WHICH == 'b' or WHICH == '1':
        BRIDGE.set_light(2, 'on', False)
