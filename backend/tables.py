import openpyxl

# table_operation
equivalent_operation = '^'
list_Types_data = ["INT", "DECIMAL", "IMAGE", "STRING", "BOOL"]
list_operations = ['+', '-', '/', '//', '<', '>', '*', '**', '%', '==', '>=', '<=']


def operation_accept(reg1, reg2, operation):
    if operation == equivalent_operation:
        operation = equivalent_operation
    sheet_name = "Hoja" + str(list_operations.index(operation) + 1)
    book = openpyxl.load_workbook('TablasTipos.xlsx', data_only=True)
    sheet = book[sheet_name]
    cells = sheet['B2':'F6']

    matrix = []
    for row in cells:
        matrix.append(row)

    Type1 = list_Types_data.index(reg1.Type)
    Type2 = list_Types_data.index(reg2.Type)
    if matrix[Type1][Type2] == "ERROR":
        print("Error")
        return ValueError
    else:
        return matrix[Type1][Type2]


# table_register
class register:
    def __init__(self, name=None, value=None, type=None):
        name = name
        value = value
        type = type


table_register = {}


def insert_NewRegister(name, value, type):
    if table_register.get(name) is not None:
        table_register[name] = register(name, value, type)
    else:
        return ValueError


def modify_Register(name, value, type):
    if table_register.get(name) is not None:
        table_register[name].value = value
        table_register[name].type = type

    else:
        return ValueError
