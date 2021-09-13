from .descriptorFile import *
from enum import Enum

operatorsTag = ["OP-SUM", "OP-RESTA", "OP-DIV", "OP-INTDIV", "OPC-L", "OPC-G", "OP-MULT", "OP-POWER", "OPL-N", "OP-MOD",
                "OP-ASSIGN",
                "OPC-E", "OPC-LE", "OPC-GE"]
delimitersTag = ["R-ENDIF", "R-ENDWHILE", "R-ENDFOR", "R-ENDFUNCTION", "R-ENDELSE", "D-C", "D-PL", "D-PR"]
functionsTag = ["F-ROT", "F-CUT", "F-RES", "F-BLUR", "F-GRAY", "F-PRINT"]
keywordsTag = ["R-IF", "R-WHILE", "R-FOR", "R-FUNCTION", "R-ELSE", "R-RETURN", "R-VOID", "STR", "NUM"]
keywordsTag += functionsTag
valueTag = ["V-STR", "V-NUM"]
idTag = ["ID"]
typeToken = operatorsTag + delimitersTag + keywordsTag + valueTag + idTag + functionsTag
valueToken = list(range(len(typeToken)))

typeTokenDict = dict(zip(typeToken, valueToken))

EnumTypeToken = Enum('EnumTypeToken', typeTokenDict)
functionsNames = ["rotate", "cut", "resize", "blur", "grayImg", "print"]
keywords = ["if", "while", "for", "function", "else", "return", "void", "str", "num"]
keywords += functionsNames
delimters = ["endif", "endwhile", "endfor", "endfunction", "endelse", ",", "(", ")"]
functionsNames = ["rotate"]
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
            token = tokenClass((EnumTypeToken['V-NUM']), char)
            setTokens.append(token)
            storeChar[0] = nextChar
            Bool = True

        elif nextChar.isalpha():
            error("Error en la linea " + str(descriptor.line) + ": Error de reconomiento de numero")
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
                error("Error en la linea " + str(descriptor.line) + ": Error de reconomiento de numero")
                storeChar[0] = nextChar
                Bool = True

            elif nextChar.isalpha():
                error("Error en la linea " + str(descriptor.line) + ": Error de reconomiento de numero")
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
            token = tokenClass((EnumTypeToken['V-STR']), char)
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
    pointerBefore = descriptor.fileDescriptor.tell()

    if char.isalpha():
        nexChar = descriptor.Getchar()
        # while nexChar != "" and nexChar != "\n" and nexChar != " " and nexChar != "\t":
        while nexChar.isnumeric() or (
                nexChar.isalpha() and nexChar != "" and nexChar != "\n" and nexChar != " " and nexChar != "\t"):
            char += nexChar
            nexChar = descriptor.Getchar()
        try:
            indexToken = keywords.index(char)
            token = tokenClass((EnumTypeToken[keywordsTag[indexToken]]), char)
            setTokens.append(token)
            # storeChar[0] = descriptor.Getchar()
            storeChar[0] = nexChar
            return True
        except ValueError:
            descriptor.fileDescriptor.seek(pointerBefore)
            # storeChar[0] = char
            return False


def identifyDelimLetters(descriptor, storeChar, setTokens):
    char = storeChar[0]
    pointerBefore = descriptor.fileDescriptor.tell()

    if char.isalpha():
        nexChar = descriptor.Getchar()
        while nexChar != "" and nexChar != "\n" and nexChar != " " and nexChar != "\t":
            char += nexChar
            nexChar = descriptor.Getchar()
        try:
            indexToken = delimters.index(char)
            token = tokenClass((EnumTypeToken[delimitersTag[indexToken]]), char)
            setTokens.append(token)
            storeChar[0] = descriptor.Getchar()
            return True
        except ValueError:
            descriptor.fileDescriptor.seek(pointerBefore)
            return False
    else:
        return False


def identifyId(descriptor, storeChar, setTokens):
    char = storeChar[0]
    # pointerBefore = descriptor.fileDescriptor.tell()

    if char.isalpha():
        nexChar = descriptor.Getchar()
        while nexChar.isnumeric() or (
                nexChar.isalpha() and nexChar != "" and nexChar != "\n" and nexChar != " " and nexChar != "\t"):
            char += nexChar
            nexChar = descriptor.Getchar()

        ids.append(char)
        token = tokenClass((EnumTypeToken["ID"]), char)
        setTokens.append(token)
        storeChar[0] = nexChar
        return True
    else:
        return False
