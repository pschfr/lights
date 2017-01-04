#!/usr/bin/python
"""This module controls my Philips Hue lights."""

import logging           # import logging
from phue import Bridge  # import Bridge from phue.py

logging.basicConfig()    # initates console logging
B = Bridge('10.0.0.215') # connects to the philips hue bridge

for L in B.lights:       # loops through the lights
    print L.name         # prints the name
    L.on = True          # gotta turn it on first
    L.brightness = 255   # 0-255
