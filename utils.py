from termcolor import colored
import os


def error(message):
    print(colored(message, 'red'))


def existFile(path):
    return os.path.exists(path)


def printChar(str):
    if str == "\n":
        return "Char:" + "Salto de linea"
    elif str == " ":
        return "Char:" + "Blanco"
    elif str == "\t":
        return "Char:" + "Tab"
    else:
        return "Char:" + str
