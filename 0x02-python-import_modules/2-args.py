#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argcount = len(sys.argv) - 1

    if argcount == 0:
        print("{} arguments.".format(argcount))
    elif argcount == 1:
        print("{} argument:".format(argcount))
    else:
        print("{} arguments:".format(argcount))

    if argcount >= 1:
        argcount = 0
        for arg in sys.argv:
            if argcount != 0:
                print("{}: {}".format(argcount, arg))
            argcount += 1
