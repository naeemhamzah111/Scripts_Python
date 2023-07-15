#!/usr/bin/env python

import datetime

print(datetime.date.today())

now = datetime.datetime.today()
start = datetime.datetime(2023,6,1,8)
time_difference = now-start

print("It has been: " + str(time_difference) + " since program start")

