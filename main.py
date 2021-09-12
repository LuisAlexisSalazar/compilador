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
        for token in analyze(nameFile):
            print(token)


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
    # print(keywords.index("else"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
