#!usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a branching statement"""

BP_STATUS = raw_input('What is your blood pressure? ')
BP_STATUS = int(BP_STATUS)
#BLOOD_PRESSURE = raw_input('Your status is currently: ')
#LOW = 'LOW!'
#IDEAL = 'IDEAL!'
#WARNING = 'WARNING!'
#HIGH = 'HIGH'
#EMERGENCY = 'EMERGENCY'

if BP_STATUS <= 89:
    print 'Your status is currently: LOW!'

if 90 < BP_STATUS > 119:
    print 'Your status is currently: IDEAL'

if 120 < BP_STATUS < 139:
    print 'Your status is currently: WARNING!'

if 140 < BP_STATUS > 159:
    print 'Your status is currently: HIGH!'

else:
    BP_STATUS < 160
    print 'Your status is currently: EMERGENCY!'

print '{}'.format(BP_STATUS)
#print '{}'.format(LOW, IDEAL, WARNING, HIGH, EMERGENCY)

