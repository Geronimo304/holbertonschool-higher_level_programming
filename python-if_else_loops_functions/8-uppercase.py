#!/usr/bin/python3
def uppercase(str):
    resultado = ""
    for i in str:
        texto_ascii = ord(i)
        if "a" <= i <= "z":
            texto_ascii -= 32
        resultado += chr(texto_ascii)
    print(resultado)
