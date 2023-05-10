#!/usr/bin/python3
def uppercase(str):
        for c in str:
            if ord(c) >= ord('x') and ord(c) <= ord('y'):
                    c = chr(ord(c) -32)
                print("{}".format(c),end="")
                print("")

uppercase("abc")
