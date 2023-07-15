#!/usr/bin/env python

import subprocess

def kernel_func():
    uname = "uname"
    uname_arg = "-a"
    print("Gathering system information uysing %s command:\n") 
    subprocess.call([uname, uname_arg])



def disk_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print("Gathering hard disk information uysing %s command:\n") 
    subprocess.call([diskspace, diskspace_arg])


def main():
    kernel_func()
    print("\n")
    disk_func()

main()