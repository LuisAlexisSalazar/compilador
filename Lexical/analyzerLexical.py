from .tokens import *


def analyze(nameFile):
    setTokens = []
    storeChar = [None]

    try:
        descriptor = descriptorClass(nameFile)
    except FileNotFoundError:
        return setTokens

    char = descriptor.Getchar()
    while char != '':
        storeChar[0] = char
        # --detector Salto de linea
        if char == '\n':
            descriptor.addCountLine()
            char = descriptor.Getchar()
        # --detector espacios y tabulador
        elif char == ' ' or char == '\t':
            char = descriptor.Getchar()

        # --detector comentarios
        elif char == '#':
            char = descriptor.Getchar()
            while char != '\n':
                char = descriptor.Getchar()

        # --detector delitimitadores simbolos : ( , )
        elif identifyDelimSymbol(descriptor, char, setTokens):
            char = descriptor.Getchar()
            continue

        # --detector Operadores : + - / // >= <= ..
        elif identifyOperator(descriptor, char, setTokens):
            char = descriptor.Getchar()
            continue
        # --Numeros : 3 3.3 5.43 ...
        elif identifyNumber(descriptor, storeChar, setTokens):
            char = storeChar[0]
            continue
        # --Valor-String  : "Hola" " "un" comentario " ...
        elif identifyStr(descriptor, storeChar, setTokens):
            char = storeChar[0]
            continue
        # --keywords  : if else while ...
        elif identifyKeyboards(descriptor, storeChar, setTokens):
            char = storeChar[0]
            continue
        # --keywords  : endif endelse endwhile ...
        elif identifyDelimLetters(descriptor, storeChar, setTokens):
            char = storeChar[0]
            continue
        # --id
        elif identifyId(descriptor, storeChar, setTokens):
            char = storeChar[0]
            continue
        else:
            error("Error en la linea " + str(descriptor.line + 1) + " : Error de simbolo no reconocidoo -> " + char)
            char = descriptor.Getchar()

    return setTokens
