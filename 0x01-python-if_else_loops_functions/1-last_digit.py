#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit_num = abs(number) % 10
if number < 0:
    digit_num = -digit_num
    print("Last digit of {} is {} and is ".format(number, digit_num), end="")
if digit_num > 5:
    print("greater than 5")
elif digit_num == 0:
    print("0")
else:
    print("less than 6 and not 0")
