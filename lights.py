#!/usr/bin/python
"""This module controls my Philips Hue lights."""

import logging           # import logging
from phue import Bridge  # import Bridge from phue.py

logging.basicConfig()    # initates console logging
BRIDGE = Bridge('10.0.0.215') # connects to the philips hue bridge

print 'Connected to Philips Hue Bridge\n'

WHICH = raw_input('Which lights? (Both, Landing, or Bedroom) ')
STATE = raw_input('On or off? ')

if STATE == 'on': # if on, ask for brightness
    BRIGHTNESS = int(raw_input('Brightness? (1-255) '))

    if WHICH == 'both':
        for LIGHT in BRIDGE.lights:
            LIGHT.on = True
            LIGHT.brightness = BRIGHTNESS

    elif WHICH == 'bedroom':
        BRIDGE.lights[0].on = True
        BRIDGE.lights[0].brightness = BRIGHTNESS

    elif WHICH == 'landing':
        BRIDGE.lights[1].on = True
        BRIDGE.lights[1].brightness = BRIGHTNESS

elif STATE == 'off':
    if WHICH == 'both':
        for LIGHT in BRIDGE.lights:
            LIGHT.on = False

    elif WHICH == 'bedroom':
        BRIDGE.lights[0].on = False

    elif WHICH == 'landing':
        BRIDGE.lights[1].on = False
