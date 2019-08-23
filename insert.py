import re
import collections

def cleanValues(group_list):
    i = 0
    while (i < len(group_list)):
        group_list[i] = group_list[i].strip().strip("'").strip()
        i = i + 1
    return group_list

def getDict(lista1, lista2):
    i = 0
    dicti = dict()
    while(i < len(lista1)):
        dicti[lista1[i]] = lista2[i]
        i = i+1
    return dicti

insert_Regex = r"INSERT +INTO(.+)\((.+)\) *VALUES *\((.+)\) *;"

valid = re.compile(insert_Regex)

print ("ingrese INSERT: ")
statement = input()

tabla = cleanValues(re.split(r',', valid.match(statement).groups()[0]))
columnas = cleanValues(re.split(r',', valid.match(statement).groups()[1]))
values = cleanValues(re.split(r',', valid.match(statement).groups()[2]))

if(len(columnas) != len(values)):
    print("error de syntax")

else:
    items = getDict(columnas, values)
    print("dicc")
    print(items)
    #file test
    file = open(tabla[0] + ".csv", "r+")
    indices = []
    columnasFile = file.readline().split(",")

    for coso in columnas:
        if(coso in columnasFile):
            indices.append(columnasFile.index(coso))

    index = getDict(indices, columnas)
    output = []

    i = 0
    while(i < len(columnasFile.split(","))):
        output.append("")
        i = i+1
    for num in indices:
        output[num] = items[index[num]]
    file.write(",".join(output)+"\n")        
 
    file.close()