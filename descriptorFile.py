from utils import *


# ? blank line = '\n'
def createFile():
    nameFile = input("Nombre del archivo:")
    file = open("files/" + nameFile + ".txt", "w+")

    writeData = None
    i = 0
    print("Para cerrar y guardar el archivo puedes escribir ':q' ")

    while (True):
        writeData = input("Linea " + str(i) + ":")
        if writeData == ":q":
            break
        file.write(writeData + "\n")
        i += 1
    file.close()


class descriptorClass:
    buffer = 10
    pointer = 0
    line = 0

    def __init__(self, nameFile):
        self.nameFile = nameFile
        path = 'files/' + self.nameFile

        if existFile(path):
            self.fileDescriptor = open(path, 'r')
            self.countLines = len(open(path).readlines())

        else:
            error("No existe el archivo")

    def Getchar(self):
        self.fileDescriptor.seek(self.pointer)
        self.pointer += 1
        return self.fileDescriptor.read(1)

    def Peekchar(self):
        self.fileDescriptor.seek(self.pointer + 1)
        return self.fileDescriptor.read(1)

    def addCountLine(self):
        self.line += 1

    def close(self):
        self.fileDescriptor.close()
