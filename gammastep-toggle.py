#!/usr/bin/env python

#!/home/iacchus/.venv/bin/python


import itertools
import os
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

SWAYSOCK = os.environ['SWAYSOCK']

sway = i3ipc.Connection(socket_path=SWAYSOCK)

for proc in psutil.process_iter():
    print(proc.name)
    if proc._name == sys.argv[1]:
        subprocess.run(args=["killall", sys.argv[1]])
        exit(0)

#  command = ["swaymsg", f"[con_id={focus_to_id}]", "focus"]
#  sway.command(f"[con_id={focus_to_id}] focus")
#  sway.command(command)
subprocess.run(args=command)

#  subprocess.run(args=command)
