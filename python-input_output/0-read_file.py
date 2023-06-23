#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "r", encoding="utf8") as fichier:
        for ligne in fichier:
            print(ligne, end="")