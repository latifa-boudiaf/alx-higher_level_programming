#!/usr/bin/python3
def uppercase(s):
    for char in s:
        upper_char = char
        if ord('a') <= ord(char) <= ord('z'):
            upper_char = chr(ord(char) - 32)
        print("{:s}".format(upper_char), end="")
    print()
