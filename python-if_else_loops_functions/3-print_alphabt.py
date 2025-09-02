#!/usr/bin/python3
for i in range(97, 123):
    print("{}".format(chr(i)) if chr(i) not in ('e', 'q')
          else "", end="")