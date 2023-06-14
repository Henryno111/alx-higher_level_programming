#!/usr/bin/python3

import sys

if len(sys.argv) != 4:
    print("usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)

pid = sys.argv[1]
search_string = sys.argv[2]
replace_string = sys.argv[3] + "\0"

print("hacking a VM, eh? so you like to live dangerously... ")

print("  <> searching for PID heap {}... ".format(pid), end="")
address = ""
mapa_path = "/proc/" + pid + "/mapa"
try:
    with open(mapa_path, "r") as mapa_file:
        for line in mapa_file:
            if "[heap]" in line:
                print("the heap has been located.")

                if "r" not in line or "w" not in line:
                    print(" [ERROR] PID heap lacks read/write permission")
                    sys.exit(0)

                line = line.split()
                print("   
