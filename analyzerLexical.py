from descriptorFile import *
from enum import Enum

operatorsTag = ["OP-SUM", "OP-RESTA", "OP-DIV", "OP-INTDIV", "OPC-L", "OPC-G", "OP-MULT", "OP-POWER", "OPL-N", "OP-MOD",
                "OP-ASSIGN",
                "OPC-E", "OPC-LE", "OPC-GE"]
delimitersTag = ["R-ENDIF", "R-ENDWHILE", "R-ENDFOR", "R-ENDFUNCTION", "R-ENDELSE", "D-C", "D-PL", "D-PR"]
keywordsTag = ["R-IF", "R-WHILE", "R-FOR", "R-FUNCTION", "R-ELSE", "R-RETURN", "R-VOID"]
typeDataTag = ["ID", "NUM", "STR"]

typeToken = operatorsTag + delimitersTag + keywordsTag + typeDataTag
valueToken = list(range(len(typeToken)))

typeTokenDict = dict(zip(typeToken, valueToken))

EnumTypeToken = Enum('EnumTypeToken', typeTokenDict)

keywords = ["if", "while", "for", "function", "else", "return", "void"]
delimters = ["endif", "endwhile", "endfor", "endfunction", "endelse", ",", "(", ")"]
ids = []


class tokenClass:
    type = None
    lexema = None

    def __str__(self):
        return "(type : " + colored(str(self.type)[14:], 'green') + " lexema : " + colored(self.lexema, 'green') + ")"

    def __init__(self, type, lexema):
        self.type = type
        self.lexema = lexema


def identifyOperator(descriptor, char, setTokens):
    Bool = False

    nextChar = None
    if char == "+":
        token = tokenClass((EnumTypeToken['OP-SUM']), "+")
        setTokens.append(token)
        Bool = True
    elif char == "-":
        token = tokenClass((EnumTypeToken['OP-RESTA']), "-")
        setTokens.append(token)
        Bool = True
    elif char == "/":
        if descriptor.Peekchar() == "/":
            token = tokenClass((EnumTypeToken['OP-INTDIV']), "//")
            char = descriptor.Getchar()
            setTokens.append(token)
            Bool = True
        else:
            token = tokenClass((EnumTypeToken['OP-DIV']), "/")
            setTokens.append(token)
            Bool = True
    elif char == "<":
        nextChar = descriptor.Peekchar()
        if nextChar == "=":
            token = tokenClass((EnumTypeToken['OPC-LE']), "<=")
            char = descriptor.Getchar()
            setTokens.append(token)
            Bool = True
        else:
            token = tokenClass((EnumTypeToken['OPC-L']), "<")
            setTokens.append(token)
            Bool = True
    elif char == ">":
        if descriptor.Peekchar() == "=":
            token = tokenClass((EnumTypeToken['OPC-GE']), ">=")
            char = descriptor.Getchar()
            setTokens.append(token)
            Bool = True
        else:
            token = tokenClass((EnumTypeToken['OPC-G']), ">")
            setTokens.append(token)
            Bool = True
    elif char == "^":
        token = tokenClass((EnumTypeToken['OP-POWER']), "^")
        setTokens.append(token)
        Bool = True
    elif char == "*":
        if descriptor.Peekchar() == "*":
            token = tokenClass((EnumTypeToken['OP-POWER']), "**")
            char = descriptor.Getchar()
            setTokens.append(token)
            Bool = True
        else:
            token = tokenClass((EnumTypeToken['OP-MULT']), "*")
            setTokens.append(token)
            Bool = True
    elif char == "!":
        token = tokenClass((EnumTypeToken['OPL-N']), "!")
        setTokens.append(token)
        Bool = True
    elif char == "=":
        nextChar = descriptor.Peekchar()
        if nextChar == "=":
            token = tokenClass((EnumTypeToken['OPC-E']), "==")
            char = descriptor.Getchar()
            setTokens.append(token)
            Bool = True
        else:
            token = tokenClass((EnumTypeToken['OP-ASSIGN']), "=")
            setTokens.append(token)
            Bool = True
    return Bool


def identifyNumber(descriptor, storeChar, setTokens):
    char = storeChar[0]
    Bool = False

    if char.isnumeric():
        nextChar = descriptor.Getchar()

        while nextChar.isnumeric():
            char += nextChar
            nextChar = descriptor.Getchar()

        if nextChar == " " or nextChar == "\n":
            token = tokenClass((EnumTypeToken['NUM']), char)
            setTokens.append(token)
            storeChar[0] = nextChar
            Bool = True

        elif nextChar.isalpha():
            error("Error en la linea " + str(descriptor.line))
            nextChar = descriptor.Getchar()
            while nextChar != " " and nextChar != "\n":
                nextChar = descriptor.Getchar()
            storeChar[0] = nextChar
            Bool = True

        # ?detector float
        elif nextChar == ".":
            char += nextChar
            nextChar = descriptor.Getchar()
            minimuDecimal = False

            while nextChar.isnumeric():
                char += nextChar
                nextChar = descriptor.Getchar()
                minimuDecimal = True

            if (nextChar == " " or nextChar == "\n") and minimuDecimal:
                token = tokenClass((EnumTypeToken['NUM']), char)
                setTokens.append(token)
                storeChar[0] = descriptor.Getchar()
                Bool = True

            # Error ejemplo : var = 33.
            elif (nextChar == " " or nextChar == "\n") and not minimuDecimal:
                error("Error en la linea " + str(descriptor.line))
                storeChar[0] = nextChar
                Bool = True

            elif nextChar.isalpha():
                error("Error en la linea " + str(descriptor.line))
                nextChar = descriptor.Getchar()
                while nextChar != " " and nextChar != "\n":
                    nextChar = descriptor.Getchar()
                storeChar[0] = nextChar
                Bool = True
    return Bool


def identifyStr(descriptor, storeChar, setTokens):
    char = storeChar[0]
    Bool = False
    token = None
    if char == "\"":
        nextChar = descriptor.Getchar()

        while nextChar != "\"":
            if nextChar == "\n":
                break
            # *Detector de comillas dentro string
            if nextChar == "\\":
                if descriptor.Peekchar() == "\"":
                    char += "\""

                    nextChar = descriptor.Getchar()
                    nextChar = descriptor.Getchar()
                    continue

            char += nextChar
            nextChar = descriptor.Getchar()

        char += nextChar
        if nextChar == "\"":
            token = tokenClass((EnumTypeToken['STR']), char)
            setTokens.append(token)
            storeChar[0] = descriptor.Getchar()
            Bool = True
        elif nextChar == "\n":
            error("Error en la linea " + str(descriptor.line))
            storeChar[0] = nextChar
            Bool = True

    return Bool


def identifyDelimSymbol(descriptor, char, setTokens):
    try:
        indexToken = delimters.index(char)
        token = tokenClass((EnumTypeToken[delimitersTag[indexToken]]), char)
        setTokens.append(token)
        return True
    except ValueError:
        return False


def identifyKeyboards(descriptor, storeChar, setTokens):
    char = storeChar[0]
    if char.isalpha():
        nexChar = descriptor.Getchar()
        while nexChar != "" and nexChar != "\n" and nexChar != " " and nexChar != "\t":
            char += nexChar
            nexChar = descriptor.Getchar()
        try:
            indexToken = keywords.index(char)
            token = tokenClass((EnumTypeToken[keywordsTag[indexToken]]), char)
            setTokens.append(token)
            storeChar[0] = descriptor.Getchar()
            return True
        except ValueError:
            storeChar[0] = char
            return False


def identifyDelimLetters(descriptor, storeChar, setTokens):
    char = storeChar[0]
    try:
        indexToken = delimters.index(char)
        token = tokenClass((EnumTypeToken[delimitersTag[indexToken]]), char)
        setTokens.append(token)
        storeChar[0] = descriptor.Getchar()
        return True
    except ValueError:
        storeChar[0] = char
        return False


def identifyId(descriptor, storeChar, setTokens):
    char = storeChar[0]
    try:
        id


def analyze(nameFile):
    descriptor = descriptorClass(nameFile)
    char = descriptor.Getchar()

    token = None
    setTokens = []
    storeChar = [None]
    wholeWord = [None]

    while char != '':
        storeChar[0] = char
        # print("Linea", descriptor.line, printChar(char))

        if char == '\n':
            descriptor.addCountLine()
            char = descriptor.Getchar()

        elif char == ' ' or char == '\t':
            char = descriptor.Getchar()

        # --detector comentarios
        elif char == '#':
            char = descriptor.Getchar()
            while char != '\n':
                char = descriptor.Getchar()

        # --detector delitimitadores simbolos como : ( , )
        elif identifyDelimSymbol(descriptor, char, setTokens):
            char = descriptor.Getchar()
            continue

        elif identifyOperator(descriptor, char, setTokens):
            # print(descriptor.fileDescriptor.tell())
            char = descriptor.Getchar()
            # print(descriptor.fileDescriptor.tell())
            continue

        elif identifyNumber(descriptor, storeChar, setTokens):
            char = storeChar[0]
            continue

        elif identifyStr(descriptor, storeChar, setTokens):
            char = storeChar[0]
            continue

        elif identifyKeyboards(descriptor, storeChar, setTokens):
            char = storeChar[0]
            continue

        elif identifyDelimLetters(descriptor, storeChar, setTokens):
            char = storeChar[0]
            continue

        else:
            char = descriptor.Getchar()

    return setTokens
