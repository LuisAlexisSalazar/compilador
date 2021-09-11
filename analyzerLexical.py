from descriptorFile import descriptorClass, createFile
from enum import Enum

operators = ["OP-SUM", "OP-RESTA", "OP-DIV", "OP-INTDIV", "OPC-L", "OPC-G", "OP-POWER", "OPL-N", "OP-MOD", "OP-ASSIGN",
             "OPC-E", "OPC-LE", "OPC-GE"]
delimiters = ["R-ENDIF", "R-ENDWHILE", "R-ENDFOR", "R-ENDFUNCTION", "R-ENDELSE", "D-PC", "D-P"]
keywords = ["R-IF", "R-WHILE", "R-FOR", "R-FUNCTION", "R-ELSE", "R-RETURN", "R-VOID"]
identifier_TypeData = ["ID", "NUM", "STR"]

typeToken = operators + delimiters + keywords + identifier_TypeData
valueToken = list(range(len(typeToken)))

typeTokenDict = dict(zip(typeToken, valueToken))

EnumTypeToken = Enum('EnumTypeToken', typeTokenDict)

class token:
    type = None
    lexema = None


def analyze(nameFile):
    descriptor(nameFile)
