import re

update_Regex = r"UPDATE (.+) SET (.+) WHERE (.+);"

valid = re.compile(update_Regex)

# Recepción de input
print ("Ingrese UPDATE: ")
statement = input()

# Validación de syntax en el input
if(valid.match(statement) == None):
    print("invalid syntax")

else:
    # Descomprime los grupos ingresados, eliminano caracteres molestos al inicio y al final de cada valor.
    Tabla = valid.match(statement).groups()[0].strip(" ' ’ ")
    Set = [name.strip(" ' ’ ").split("=") for name in re.split(r',', valid.match(statement).groups()[1])]
    Where = [name.strip(" ' ’ ").split("AND") for name in re.split(r'OR', valid.match(statement).groups()[2])]

    #Tabla = valid.match(statement).groups()[0].strip().strip("'").strip()
    #Set = splitLists(cleanValues(re.split(r',', valid.match(statement).groups()[1])), "=")
    #Where = splitLists(cleanValues(re.split(r'OR', valid.match(statement).groups()[2])),"AND")
    
    # Elimina espacios y caracteres adicionales de los valores en Set y Where.
    i = 0
    j = 0
    while (i < len(Set)):
        while(j < len(Set[i])):
            Set[i][j] = Set[i][j].strip(" ' ’ ")
            j = j + 1
        i = i + 1
        j = 0

    i = 0
    j = 0
    k = 0
    while(i < len(Where)):
        while(j < len(Where[i])):
            Where[i][j] = Where[i][j].split("=")
            while(k < len(Where[i][j])):
                Where[i][j][k] = Where[i][j][k].strip(" ' ’ ")
                k = k + 1
            j = j + 1
            k = 0
        i = i + 1
        j = 0
        k = 0


    print("Tabla: ", Tabla)
    print("Set: ", Set)
    print("Where: ", Where)

    