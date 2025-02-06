#!/usr/bin/env python

import itertools
import os
import sys

import i3ipc

argc = len(sys.argv)

SWAYSOCK = os.environ['SWAYSOCK']

sway = i3ipc.Connection(socket_path=SWAYSOCK)

root = sway.get_tree()

focused = root.find_focused()
windows = root.descendants()

focused_id = focused.id
window_id_list = [window.id for window in windows
                  if window.type in ("con", "floating_con")]

window_id_list_reversed = reversed(window_id_list)

#  print(windows)

#  print(window_id_list)

#  print(focused)
#  print("FOCUSED:", focused.ipc_data, end="\n\n")

#  for window in windows:
#      if window.type in ("con", "floating_con"):
#          print("WINDOW:", window.ipc_data, end="\n\n")

#  sway.main()
