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
    Set = [name2.strip(" ' ’ ") for name in re.split(r',', valid.match(statement).groups()[1]) for name2 in name.split("=")]
    Where = [name.strip(" ' ’ ").split("AND") for name in re.split(r'OR', valid.match(statement).groups()[2])]

    # Diccionario para guardar los valores en Set, cada key es un valor a modificar en el archivo csv
    largo = 0
    Set_dict = dict()
    while (largo < len(Set) and largo + 1 < len(Set)):
        # Si es Nombre o Ramo puede tener espacios en blanco entre palabras, lo que hace la línea 28
        # es encargarse de que el espacio que exista entre palabras sea solo uno.
        if(Set[largo] == "Nombre" or Set[largo] == "Ramo"):
            Set_dict[Set[largo]] = re.sub(r"\s+"," ", Set[largo + 1], flags = re.I)

        # Si no es Nombre o Ramo, significa que es Sigla o algún número, por lo que no necesita
        # tener espacios en blanco entre caracteres.
        else:
            Set_dict[Set[largo]] = re.sub(r"\s+","", Set[largo + 1], flags = re.I)
        #Set_dict[Set[largo]] = Set[largo + 1]
        largo = largo + 2
        # TODO: Preguntar por los espacios entre medio, ya que modifica la estructura de lo ingresado

    # Diccionario para guardar los valores en Where, cada key se una condición, las keys estan separadas
    # por un OR, es decir, debe ocurrir lo guardado en key 0 o lo guardado en key 1 o .... hasta llegar 
    # a un caso valido. Las keys que poseen mas de una condición se deben a los AND que las unian inicialmente
    largo = 0
    Where_dict = dict()
    while(largo < len(Where)):
        Where_dict[largo] = []
        for elem in Where[largo]:
            col, value = elem.split("=")
            col = col.strip(" ' ’ ")
            value = value.strip(" ' ’ ")
            # Si es Nombre o Ramo puede tener espacios en blanco entre palabras, lo que hace la línea 28
            # es encargarse de que el espacio que exista entre palabras sea solo uno.
            if(col == "Nombre" or col == "Ramo"):
                value = re.sub(r"\s+"," ", value, flags = re.I)

            # Si no es Nombre o Ramo, significa que es Sigla o algún número, por lo que no necesita
            # tener espacios en blanco entre caracteres.
            else:
                value = re.sub(r"\s+","", value, flags = re.I)

            Where_dict[largo].append((col.strip(" ' ’ "), value.strip(" ' ’ ")))

        largo = largo + 1

    # Almacena el archivo csv entregado por el usuario en una lista bidimensional, las listas internas almacenan
    # su respectiva linea en el archivo, es decir, la primera lista interna almacena la primera linea del archivo
    file = open(Tabla + ".csv", "r", encoding='utf-8')
    lineas = file.readlines()
    cont = 0
    while(cont < len(lineas)):
        lineas[cont] = lineas[cont].strip().split(",")
        cont = cont + 1
    file.close()

    indiceOutput =0
    # Verifica si existe al menos una columna de las que se desea modificar.
    for key in Set_dict.keys():
        if (key in lineas[0]):
            indiceOutput = indiceOutput + 1
    if(indiceOutput == 0):
        print("No existe la columna que desea modificar.")
    else:
        # Empieza la magia.
        cont = 0
        while(cont < len(Where_dict)):
            print(cont)
            indiceColumnas = 0
            # Verifica si existen todas las columnas que desea comparar.
            for condiciones in Where_dict[cont]:
                if (condiciones[0] in lineas[0]):
                    indiceColumnas = indiceColumnas + 1
            # Verifica si la cantidad de columnas a comparar coincide con la cantidad encontrada.
            if (indiceColumnas > 0 and indiceColumnas == len(Where_dict[cont])):
                # Ahora debe encontrar la fila que contiene dichos datos.
                # Para evitar que modifique el nombre de la columna, cambiar fila por fila + 1.
                fila = 0
                while (fila < len(lineas)):
                    flag = []
                    # Comprueba que lo almacenado en la columna de la respectiva fila 
                    # coincida con el valor ingresado.
                    for col, val in Where_dict[cont]:
                        indice = lineas[0].index(col)
                        #print(val, " == ", lineas[fila][indice])
                        if (val == lineas[fila][indice]):
                            flag.append(1)
                        else:
                            flag.append(0)
                    # Si todos los datos ingresados en where coinciden con los almacenados en la fila
                    # empieza la modificación.
                    if (0 not in flag):
                        cont = len(Where_dict) # No necesita seguir iterando el primer while
                        for key, value in Set_dict.items():
                            if key in lineas[0]:
                                indiceColumna = lineas[0].index(key)
                                lineas[fila][indiceColumna] = value
                        file = open(Tabla + ".csv", "w", encoding='utf-8')
                        for linea in lineas:
                            file.write(",".join(linea)+"\n")
                        file.close()
                        print("Se ha actualizado 1 fila")
                        fila = len(lineas)
                        cont = len(Where_dict)
                            
                    fila = fila + 1
            cont = cont + 1  
        print("No se ha encontrado la fila que desea actualizar")
         