import re
import collections

'''
Nombre de la función: cleanValues
——————–
Entradas:
(lista group_list) Lista que contiene los valores obtenidos por el match entre el query y la expresión regular
——————–
Salida:
(lista group_list) Misma lista ingresada, pero sin espacios blancos ni apóstrofes al inicio y final de cada valor
——————–
Descripción de la función:  Itera con los valores de la lista ingresada limpiando los espacios blancos y
                            apóstrofes al inicio y al final de cada valor usando la concatenación
                            del comando value.strip().strip("'").strip()
'''
#Problema con esta función: si alguien decide trollear y decir que el nombre de algo es, por ejemplo
# columna = "col'", al usar strip("'") estaria modificando el nombre real y realizando una comparación
# erronea, TODO in the future.
def cleanValues(group_list):
    i = 0
    while (i < len(group_list)):
        group_list[i] = group_list[i].strip(" ’")
        i = i + 1
    return group_list 

def getDict(lista1, lista2):
    i = 0
    dicti = dict()
    while(i < len(lista1)):
        dicti[lista1[i]] = lista2[i]
        i = i+1
    return dicti

def splitLists(lista, string):
    i = 0
    while (i < len(lista)):
        lista[i] = cleanValues(lista[i].split(string))
        i = i + 1
    return lista

update_Regex = r"UPDATE(.+)SET(.+)WHERE(.+);"

valid = re.compile(update_Regex)

print ("ingrese UPDATE: ")
statement = input()

Tabla = valid.match(statement).groups()[0].strip().strip("'").strip()
Set = splitLists(cleanValues(re.split(r',', valid.match(statement).groups()[1])), "=")
Where = splitLists(cleanValues(re.split(r'OR', valid.match(statement).groups()[2])),"AND")

# asegura que los cosos unidos con AND queden en una lista propia mientras q los cosos unidos con OR
# quedan en una lista aparte

i = 0
while (i < len(Where)):
    Where[i] = splitLists(Where[i], "=")
    i = i + 1

print(Tabla)
print(Set)
print(Where)



file = open(Tabla + ".csv", "r+")


file.close()
