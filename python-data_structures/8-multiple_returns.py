#!/usr/bin/python3
def multiple_returns(sentence):
        longitud = len(sentence)

        if sentence == "":
            first = None

        else:
            first = sentence[0]

        return(longitud, first)
