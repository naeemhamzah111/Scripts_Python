#!/usr/bin/env python

import subprocess

# Desired_Num = int(input("Enter Range of Num: "))
touch_command = "touch"

i = 1
a = 5

while i < a:
    subprocess.call("touch", "test")
    # print(i)
    i += 1
