#!/usr/bin/env python

#!/home/iacchus/.venv/bin/python


import itertools
import os
import subprocess
import sys

import i3ipc

argc = len(sys.argv)

if argc == 2 and sys.argv[1] in ("prev", "next"):
    direction = sys.argv[1]
else:
    print(f"usage: {sys.argv[0]} <prev|next>")
    exit(1)

SWAYSOCK = os.environ['SWAYSOCK']

sway = i3ipc.Connection(socket_path=SWAYSOCK)

root = sway.get_tree()

focused = root.find_focused()
windows = root.descendants()

focused_id = focused.id
#  print("foc:", focused_id)
#  print("type:", focused.type)
#  print("windows:", windows)

window_id_list = [window.id for window in windows
                  if window.type in ("con", "floating_con")]

if direction == "prev":
    window_id_list.reverse()

window_gen = itertools.cycle(window_id_list)

for window_id in window_gen:
    #  print("LOOP:", window_id)
    if window_id == focused_id:
        break

focus_to_id = next(window_gen)

#  print("GO TO:", focus_to_id)

#  command = ["swaymsg", f"[con_id={focus_to_id}]", "focus"]
sway.command(f"[con_id={focus_to_id}] focus")

#  subprocess.run(args=command)

exit(0)
