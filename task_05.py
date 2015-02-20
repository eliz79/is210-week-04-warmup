#!usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a branching statement"""

BP_STATUS = raw_input('What is your blood pressure? ')

if BP_STATUS > 89:
    print 'LOW!'

if BP_STATUS >= 90 and <= 119:
    print 'IDEAL'

       
print '{}'.format(BP_STATUS)

