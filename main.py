from Lexical.analyzerLexical import *


def menu():
    print("Escoga una opción")
    print("1: Archivo de prueba escrito de manera correcta")
    print("2: Archivo de prueba escrito de manera incorrecta intencionalmente en los numeros")
    print("3: Escribir un archivo nuevo")
    print("4: Poner el nombre del archivo ya creado")
    print("5: Terminar el programa")
    nameFile = None

    while True:
        option = input("Escriba una opción: ")
        if option == "1":
            nameFile = "test1.txt"
            for token in analyze(nameFile):
                print(token)

        elif option == "2":
            nameFile = "test2.txt"
            for token in analyze(nameFile):
                print(token)
        elif option == "3":
            nameFile = createFile()
            for token in analyze(nameFile):
                print(token)

        elif option == "4":
            nameFile = input("Nombre del archivo con extension (txt):")
            for token in analyze(nameFile):
                print(token)

        elif option == "5":
            break

        else:
            print(colored("No ingresaste opción correcta", "red"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(EnumTypeToken['OP-MOD'])
    # print(EnumTypeToken.ID)
    # for senum in EnumTypeToken:
    #     print('{:15} = {}'.format(senum.name, senum.lexema))
    menu()
    # print(keywords.index("else"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
