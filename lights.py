#!/usr/bin/python
"""This module controls my Philips Hue lights."""

import logging           # import logging
from phue import Bridge  # import Bridge from phue.py

logging.basicConfig()    # initates console logging
BRIDGE = Bridge('10.0.0.215') # connects to the philips hue bridge

print 'Connected to Philips Hue Bridge\n'

WHICH = raw_input('Which lights? (Both, Landing, or Bedroom) ')
STATE = raw_input('On or off? ')

if STATE == 'on' or STATE == '1' or STATE == '': # if on, ask for brightness
    BRIGHTNESS = raw_input('Brightness? (1-255) ')
    if BRIGHTNESS == '':
        BRIGHTNESS = 255

    if WHICH == 'both' or WHICH == '2' or WHICH == '':
        for LIGHT in BRIDGE.lights:
            LIGHT.on = True
            LIGHT.brightness = int(BRIGHTNESS)

    elif WHICH == 'bedroom' or WHICH == 'bed' or WHICH == 'b' or WHICH == '0':
        BRIDGE.lights[0].on = True
        BRIDGE.lights[0].brightness = int(BRIGHTNESS)

    elif WHICH == 'landing' or WHICH == 'l' or WHICH == '1':
        BRIDGE.lights[1].on = True
        BRIDGE.lights[1].brightness = int(BRIGHTNESS)

elif STATE == 'off' or STATE == '0':
    if WHICH == 'both' or WHICH == '2' or WHICH == '':
        for LIGHT in BRIDGE.lights:
            LIGHT.on = False

    elif WHICH == 'bedroom' or WHICH == 'bed' or WHICH == 'b' or WHICH == '0':
        BRIDGE.lights[0].on = False

    elif WHICH == 'landing' or WHICH == 'l' or WHICH == '1':
        BRIDGE.lights[1].on = False
