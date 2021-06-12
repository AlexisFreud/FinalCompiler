"""
Este archivo permite leer en la consola las entradas
"""
from aLEXis_compiler import run


def execute_shell():
    while True:
        text = input("aLEXis Compiler > ")
        result, error = run(text)
        if error:
            print(error.as_string())
        else:
            print(result)


execute_shell()
