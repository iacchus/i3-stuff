#!/usr/bin/env python

#  import itertools
import os
#  import subprocess
import sys

import i3ipc

argc = len(sys.argv)

if argc == 2 and sys.argv[1] in ("prev", "next"):
    direction = sys.argv[1]
else:
    print(f"usage: {sys.argv[0]} <prev|next>")
    exit(1)

I3SOCK = os.environ['I3SOCK']
SCRATCHPAD_NAME = "__i3_scratch"
SCRATCHPAD_NAME2 = "scratchpad"


def get_next_empty_workspace(workspaces: list[int]):
    first = 1
    chosen = 0
    for number in range(first, 11):
        if number not in workspaces:
            chosen = number
            break
    return chosen


i3 = i3ipc.Connection(socket_path=I3SOCK)

root = i3.get_tree()
descendants = root.descendants()

existing_workspaces = [int(workspace.name) for workspace in descendants
                       if workspace.type == "workspace"
                       and workspace.name != SCRATCHPAD_NAME
                       and workspace.name != SCRATCHPAD_NAME2]

existing_workspaces.sort()

focused_window = root.find_focused()
focused_workspace = focused_window.workspace()
workspace_name = int(focused_workspace.name)
num_of_containers_in_focused_workspace = len(focused_workspace.descendants())

if direction == "next":
    if workspace_name == existing_workspaces[-1] \
            and num_of_containers_in_focused_workspace > 0:
                to_workspace = existing_workspaces[-1] + 1
    elif workspace_name == existing_workspaces[-1] \
            and num_of_containers_in_focused_workspace == 0:
                to_workspace = existing_workspaces[0]
    else:
        current_workspace_index = existing_workspaces.index(workspace_name)
        to_workspace = existing_workspaces[current_workspace_index+1]

elif direction == "prev":
    existing_workspaces.reverse()
    if workspace_name == existing_workspaces[-1] \
            and num_of_containers_in_focused_workspace > 0:
                to_workspace = existing_workspaces[0] + 1
    else:
        current_workspace_index = existing_workspaces.index(workspace_name)
        to_workspace = existing_workspaces[current_workspace_index+1]


i3.command(f"workspace number {to_workspace}")

exit(0)
