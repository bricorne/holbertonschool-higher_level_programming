#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """read file"""
    with open(filename, "r", encoding="utf8") as fichier:
        for ligne in fichier:
            print(ligne, end="")