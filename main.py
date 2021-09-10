from analyzerLexical import *


def menu():
    print("Escoga una opción")
    print("1: Archivo de prueba escrito de manera correcta")
    print("2: Archivo de prueba escrito de manera incorrecta intencionalmente")
    print("3: Escribir un archivo nuevo")
    print("4: Poner el nombre del archivo ya creado")

    option = input("option: ")
    if option == "1":
        pass
    elif option == "2":
        pass
    elif option == "3":
        createFile()
    elif option == "4":
        pass
    else:
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
