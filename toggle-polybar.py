#!/data/data/com.termux/files/home/.venv/bin/python

import psutil
import subprocess

import i3ipc

NAME = "polybar"

i3 = i3ipc.Connection()

for proc in psutil.process_iter(["name"]):

    if proc.info["name"] == NAME:
        print(proc.info["name"])
        subprocess.run(args=["killall", NAME])
        exit(0)

i3.command(f"exec {NAME} top")
#  subprocess.run(args=command)
