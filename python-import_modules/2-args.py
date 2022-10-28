#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv) - 1) != 1:
        print("{} arguments".format(len(sys.argv) - 1), end="")
    else:
        print("{} argument".format(len(sys.argv) - 1), end="")
    if len(sys.argv) == 1:
        print(".")
    else:
        print(":")
    for i, arg in enumerate(sys.argv):
        if(i == 0):
            continue
        print("{}: {}".format((i), arg))

