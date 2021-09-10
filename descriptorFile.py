def createFile():
    nameFile = input("Nombre del archivo:")
    file = open("files/" + nameFile + ".txt", "w+")

    writeData = None
    i = 0
    while (True):
        writeData = input("Linea " + str(i) + ":")
        if writeData == ":q":
            break
        file.write(writeData + "\n")
        i += 1
    file.close()


class descriptor:

    def __init__(self, nameFile):
        self.nameFile = nameFile

    def Getchar(self):
        pass

    def Peekchar(self):
        pass
