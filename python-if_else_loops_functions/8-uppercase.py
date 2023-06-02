#!/usr/bin/python3
def uppercase(str):
    output = ""
    for c in str:
        if 'a' <= c <= 'z':
            output += chr(ord(c) - 32)
        else:
            output += c
    print(output)
