#!/data/data/com.termux/files/home/.venv/bin/python

#!/usr/bin/env python

#!/home/iacchus/.venv/bin/python

# TODO: NOT TESTED

import psutil
import subprocess
import sys

import i3ipc

argc = len(sys.argv)

if argc > 1:
    command = sys.argv[1:]
else:
    print(f"usage: {sys.argv[0]} <command> [args]")
    exit(1)

i3 = i3ipc.Connection()

for proc in psutil.process_iter(["name"]):

    if proc.info["name"] == sys.argv[1]:
        subprocess.run(args=["killall", sys.argv[1]])
        exit(0)

i3.command(f"exec {command}")
