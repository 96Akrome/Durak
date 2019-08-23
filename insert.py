import re
import collections

def removeWhiteSpaces(group_list):
    i = 0
    while (i < len(group_list)):
        group_list[i] = group_list[i].strip()
        i = i + 1
    return group_list

def getIndex(lista, value):
    i = 0
    for dato in lista:
        if(dato.strip() == value):
            return i
        i = i + 1
    return -1

def getDict(columnas, values):
    i = 0
    dicti = dict()
    while(i < len(columnas)):
        dicti[columnas[i]] = values[i]
        i = i+1
    return dicti

insert_Regex = r" *INSERT +INTO +(.+) *\( *(.+) *\) *VALUES *\( *( *.+ *) *\);"

valid = re.compile(insert_Regex)

print ("ingrese INSERT: ")
statement = input()

tabla = re.split(r',', valid.match(statement).groups()[0])
columnas = re.split(r',', valid.match(statement).groups()[1])
values = re.split(r',', valid.match(statement).groups()[2])

tabla = removeWhiteSpaces(tabla)
columnas = removeWhiteSpaces(columnas)
values = removeWhiteSpaces(values)

print("tabla: ")
print (tabla)
print("\ncolumnas")
print(columnas)
print("\nValues")
print(values)
print(tabla[0])
if(len(columnas) != len(values)):
    print("error de syntax")

else:
    items = getDict(columnas, values)
    print("dicc")
    print(items)
    #file test
    file = open(tabla[0] + ".csv", "r+")
    indices = []
    columnasFile = file.readline()
    print ("las columnas del archivo son:")
    print (columnasFile)
    for coso in columnas:
        indice = getIndex(columnasFile.split(","), coso)
        if(indice != -1):
            indices.append(indice)
    index = getDict(indices, columnas)
    print("indices")
    print(indices)
    print(index)
    output = []

    i = 0
    while(i < len(columnasFile.split(","))):
        output.append("")
        i = i+1
    for num in indices:
        output[num] = items[index[num]]
    file.write(",".join(output)+"\n")        
 
    file.close()