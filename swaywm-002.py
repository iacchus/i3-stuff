#!/usr/bin/env python

import itertools
import os
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
window_id_list = [window.id for window in windows
                  if window.type in ("con", "floating_con")]

if direction == next:
    window_gen = itertools.cycle(window_id_list)
else:
    window_id_list_reversed = reversed(window_id_list)
    window_gen = itertools.cycle(window_id_list_reversed)
#  backward = itertools.cycle(window_id_list_reversed)

while next(window_gen) != focused_id:
    next(window_gen)
    print("LOOP:", window_gen)

focus_to_id = next(window_gen)

print("GO TO:", focus_to_id)
