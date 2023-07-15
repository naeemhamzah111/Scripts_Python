#!/usr/bin/env python

import subprocess

uname = "uname"
uname_arg = "-a"
print("Gathering system information using uname command:\n") 
subprocess.call([uname, uname_arg])

print("\n")

diskspace = "df"
diskspace_arg = "-h"
print("Gathering hard disk information using %s command:\n") 
subprocess.call([diskspace, diskspace_arg])
