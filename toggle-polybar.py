#!/usr/bin/env python

#!/home/iacchus/.venv/bin/python


#  import itertools
#  import os
import psutil
import subprocess
#  import sys

#  import i3ipc

NAME = "polybar"
#  argc = len(sys.argv)

#  if argc > 1:
#      command = sys.argv[1:]
#  else:
#      print(f"usage: {sys.argv[0]} <command> [args]")
#      exit(1)

#  I3SOCK = os.environ['I3SOCK']

#  sway = i3ipc.Connection()

for proc in psutil.process_iter():

    if proc.name == NAME:
        subprocess.run(args=["killall", NAME])
        exit(0)

#  command = ["swaymsg", f"[con_id={focus_to_id}]", "focus"]
#  sway.command(f"[con_id={focus_to_id}] focus")
#  sway.command(command)
subprocess.run(args=NAME)

#  subprocess.run(args=command)
