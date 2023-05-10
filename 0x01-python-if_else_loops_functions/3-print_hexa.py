#!/usr/bin/python3
for figure in range(ord('a'), ord('z') + 1):
    if chr(figure) != 'q' and chr(figure) != 'e':
        print('{}'.format(chr(figure)), end='')
