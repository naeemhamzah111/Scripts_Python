#!/usr/bin/env python

from sysinfo4 import disk_func
from sysinfo4 import kernel_func

import subprocess

def tmp_space():
    sudo = "sudo"
    tmp_usage = "du"
    tmp_arg = "-hs"
    path ="/tmp"
    print("\n")
    print("Total space used by /tmp directory")
    subprocess.call([sudo, tmp_usage, tmp_arg, path])


def main():
    disk_func()
    tmp_space()

if __name__ == "__main__":
    main()