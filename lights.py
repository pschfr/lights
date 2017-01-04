#!/usr/bin/python
# pylint: disable=C0103
"""This module controls my Philips Hue lights."""

import logging
from phue import Bridge

logging.basicConfig()
br = Bridge('10.0.0.215')

# this only needs to be run once
# br.connect()

lights = br.lights

# print lights[0].name
# lights[0].on = True
# lights[0].brightness = 255

# print lights[1].name
# lights[1].on = True
# lights[1].brightness = 255

# Loop through lights, turning them on
for l in lights:
    print l.name
    l.on = True
    l.brightness = 255
