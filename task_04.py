#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A single if statement."""

MYINPUT = raw_input('Tell me a story! ')
MAX_LENGTH = 80
LONGSTR = 'short'

if len(MYINPUT) < MAX_LENGTH:
    print MYINPUT.replace('short', 'long')

# You code goes here

OUTPUT = 'That certainly was a {} story!'.format(LONGSTR)
print OUTPUT
