#!/usr/bin/python3
"""write in a file"""


def write_file(filename="", text=""):
    """write in a file"""
    with open(filename, "w", encoding="utf8") as fichier:
        count = fichier.write(text)
    return count