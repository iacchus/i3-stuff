#!/usr/bin/env python

import os

import i3ipc

SWAYSOCK = os.environ['SWAYSOCK']

sway = i3ipc.Connection(socket_path=SWAYSOCK)

root = sway.get_tree()
#  focused = sway.get_tree().find_focused()
focused = root.find_focused()
windows = root.descendants()

window_id_list = [window.id for window in windows]
print(focused)


