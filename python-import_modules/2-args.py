#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    num_args = len(argv) - 1  # Restamos 1 porque argv[0] es el nombre del script

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
