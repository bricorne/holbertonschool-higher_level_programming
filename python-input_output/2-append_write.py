#!/usr/bin/python3
"""append text"""


def append_write(filename="", text=""):
    """append text"""
    with open(filename, "a", encoding="utf8") as fichier:
        count = fichier.write(text)
    return count