#!/usr/bin/python3

def write_file(filename="", text=""):
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1

    return
