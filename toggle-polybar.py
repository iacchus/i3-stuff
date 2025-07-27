#!/data/data/com.termux/files/home/.venv/bin/python

import psutil
import subprocess

import i3ipc

NAME = "polybar"

i3 = i3ipc.Connection()

for proc in psutil.process_iter(["name"]):

    if proc.info["name"] == NAME:
        #  subprocess.run(args=["killall", NAME])
        i3.command(f"exec killall {NAME}")
        exit(0)

i3.command(f"exec {NAME} top")
#  subprocess.run(args=command)
