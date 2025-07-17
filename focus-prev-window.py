#!/usr/bin/env python

#!/home/iacchus/.venv/bin/python


#  import itertools
#  import os
#  import subprocess
#  import sys

import i3ipc

#  argc = len(sys.argv)
#
#  if argc == 2 and sys.argv[1] in ("prev", "next"):
#      direction = sys.argv[1]
#  else:
#      print(f"usage: {sys.argv[0]} <prev|next>")
#      exit(1)

#  I3SOCK = os.environ['I3SOCK']
#
#  i3 = i3ipc.Connection(socket_path=I3SOCK)
i3 = i3ipc.Connection()

root = i3.get_tree()

focused = root.find_focused()
windows = root.descendants()

#  focused_id = focused.id
focused_id = focused.window

#  window_id_list = [window.id for window in windows
window_id_list = [window.window for window in windows
                  if window.type in ("con", "floating_con")
                  if window.window
                  if not window.name.startswith("polybar")]

#  if direction == "prev":
window_id_list.reverse()  # because this is prev window

#  window_gen = itertools.cycle(window_id_list)

#  num_of_windows = len(window_id_list)
all_windows = window_id_list * 2

#  index = 0

#  for idx, window_id in enumerate(all_windows):
#      if window_id == focused_id:
#          index = idx + 1
#          break

#  focus_to_id = all_windows[index]
focus_to_id = all_windows[all_windows.index(focused_id)+1]

#  sway.command(f"[con_id={focus_to_id}] focus")
i3.command(f"[id={focus_to_id}] focus")

exit(0)
