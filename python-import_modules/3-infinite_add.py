#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_c = len(sys.argv)
    r = 0
    for i in range(1, arg_c):
        r += int(sys.argv[i])
    print("{}".format(r))
