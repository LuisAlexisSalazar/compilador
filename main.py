from analyzerLexical import *


def menu():
    print("Escoga una opción")
    print("1: Archivo de prueba escrito de manera correcta")
    print("2: Archivo de prueba escrito de manera incorrecta intencionalmente")
    print("3: Escribir un archivo nuevo")
    print("4: Poner el nombre del archivo ya creado")
    nameFile = None
    # option = input("option: ")
    option = "1"
    if option == "1":
        nameFile = "test1.txt"
        descriptor = descriptorClass(nameFile)

        char = descriptor.Getchar()

        while char != '':

            if char == '\n':
                descriptor.addCountLine()
                char = descriptor.Getchar()

            if char == ' ' or char == '\t':
                char = descriptor.Getchar()

            # --detectar comentario
            if char == '#':
                descriptor.addCountLine()
                char = descriptor.Getchar()

            # --detectar simbolos
            if char == ">":
                if descriptor.Peekchar() == '=':
                    print("TOKEN >=")
                else:
                    print("TOKEN >")

            char = descriptor.Getchar()
            # if char == "\"":
            #     print("STR")


    elif option == "2":
        pass
    elif option == "3":
        createFile()
    elif option == "4":
        nameFile = input("Nombre del archivo a abrir")
    else:
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(EnumTypeToken['OP-MOD'])
    # print(EnumTypeToken.ID)
    # for senum in EnumTypeToken:
    #     print('{:15} = {}'.format(senum.name, senum.lexema))
    menu()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
