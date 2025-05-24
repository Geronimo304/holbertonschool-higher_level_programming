#!/usr/bin/python3
no = "e"
no1 = "q"
for juan in range(97, 123):
    character = chr(juan)
    if character != no and character != no1:
        print(character, end="".format(character))
