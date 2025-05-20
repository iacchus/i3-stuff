#!/usr/bin/env python

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


sway = i3ipc.Connection(socket_path=SWAYSOCK)

root = sway.get_tree()
descendants = root.descendants()

existing_workspaces = [int(workspace.name) for workspace in descendants
                       if workspace.type == "workspace"
                       and workspace.name != SCRATCHPAD_NAME
                       and workspace.name != SCRATCHPAD_NAME2]

existing_workspaces.sort()

focused = root.find_focused()
workspace = focused.workspace()
#  windows = root.descendants()
#  focused_id = focused.id

if direction == "next":
    if int(workspace.name) == existing_workspaces[-1]:
        empty_workspace = get_next_empty_workspace(workspaces=existing_workspaces)
        to_workspace = empty_workspace
    else:
        current_workspace_index = existing_workspaces.index(int(workspace.name))
        to_workspace = existing_workspaces[current_workspace_index+1]

elif direction == "prev":
    #  existing_workspaces.reverse()
    if int(workspace.name) == existing_workspaces[0]:
        empty_workspace = get_next_empty_workspace(workspaces=existing_workspaces)
        to_workspace = empty_workspace
    else:
        current_workspace_index = existing_workspaces.index(int(workspace.name))
        to_workspace = existing_workspaces[current_workspace_index-1]

#  empty_workspace = get_next_empty_workspace(workspaces=existing_workspaces)

sway.command(f"move container to workspace number {to_workspace}, workspace number {to_workspace}")
#  sway.command(f"workspace number {empty_workspace}")

exit(0)
