#!/usr/bin/env python

import os

import i3ipc

SWAYSOCK = os.environ['SWAYSOCK']
sway = i3ipc.Connection(socket_path=SWAYSOCK)

def on_window_focus(sway, e):
    focused = sway.get_tree().find_focused()
    print(focused.name)

sway.on(event=i3ipc.Event.WINDOW_FOCUS, handler=on_window_focus)

sway.main()
