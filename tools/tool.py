from termcolor import colored
import os


def error(message):
    print(colored(message, 'red'))


def existFile(path):
    return os.path.exists(path)


# ? blank line = '\n'
def createFile():
    nameFile = input("Nombre del archivo con extension txt:")
    file = open("files/" + nameFile + ".txt", "w+")

    writeData = None
    i = 0
    print("Para cerrar y guardar el archivo puedes escribir ':q' ")

    while True:
        writeData = input("Linea " + str(i) + ":")
        if writeData == ":q":
            break
        file.write(writeData + "\n")
        i += 1
    file.close()
    return nameFile


def printChar(str):
    if str == "\n":
        return "Char:" + "Salto de linea"
    elif str == " ":
        return "Char:" + "Blanco"
    elif str == "\t":
        return "Char:" + "Tab"
    else:
        return "Char:" + str
