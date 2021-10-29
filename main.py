# -*- coding: utf-8 -*-
from Lexical.analyzerLexical import *
from ll1.parse import parse_tree


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
            analyze(nameFile)
            for token in analyze(nameFile):
                print(token)
            break

        elif option == "2":
            nameFile = "test2.txt"
            for token in analyze(nameFile):
                print(token)
            break
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


def use_ll1(tokens_input):
    descriptor_file = open("files/grammar.txt", "r")
    grammar = descriptor_file.read()
    parse_tree(grammar, tokens_input)



if __name__ == '__main__':
    # menu()

    nameFile = "test1.txt"
    tokens = analyze(nameFile)
    tokens_str = []
    for token in tokens:
        print(token.print())
        tokens_str.append(str(token))

    print(tokens_str)
    use_ll1(tokens_str)
