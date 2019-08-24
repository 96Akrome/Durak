import re

insert_Regex = r"INSERT INTO (.+)\((.+)\) +VALUES +\((.+)\) *;"

valid = re.compile(insert_Regex)

# Recepción de input
print ("Ingrese INSERT: ")
statement = input()

# Validación de syntax en el input
if(valid.match(statement) == None):
    print("invalid syntax")

else:
    # Descomprime los grupos ingresados, eliminano caracteres molestos al inicio y al final de cada valor.
    Tabla = [name.strip(" ' ’ ") for name in re.split(r',', valid.match(statement).groups()[0])]
    Columnas = [name.strip(" ' ’ ") for name in re.split(r',', valid.match(statement).groups()[1])]
    Values = [name.strip(" ' ’ ") for name in re.split(r',', valid.match(statement).groups()[2])]
    # Quizas podria reducir espacios dentro de cada columna y dentro de Tabla, en caso de existir (ver linea 33)
    # Validación de syntax según la cantidad de Columnas y valores.
    if (len(Columnas) != len(Values)):
        print("error de syntax, la cantidad de valores no coincide con la cantidad de Columnas")
    
    else:
        # Genera un diccionario para ordenar bien los datos ingresados en input, eliminando caracteres molestos
        # según la estructura de las Tablas entregadas.
        inputs = dict()
        i = 0
        while (i < len(Columnas)):
            # Si es Nombre o Ramo puede tener espacios en blanco entre palabras, lo que hace la línea 34
            # es encargarse de que el espacio que exista entre palabras sea solo uno.
            if(Columnas[i] == "Nombre" or Columnas[i] == "Ramo"):
                inputs[Columnas[i]] = re.sub(r"\s+"," ", Values[i], flags = re.I)
            # Si no es Nombre o Ramo, significa que es Sigla o algún número, por lo que no necesita
            # tener espacios en blanco entre caracteres.
            else:
                inputs[Columnas[i]] = re.sub(r"\s+","", Values[i], flags = re.I)
            i = i + 1

        # Abre el archivo de la Tabla correspondiente en modo r+ (lectura + append).
        file = open(Tabla[0] + ".csv", "r+")

        # Lee la primera línea del archivo, elimina el salto de línea al final y separa el string
        # según las comas para obtener una lista con las Columnas del archivo.
        columnasFile = file.readline().strip().split(",")

        # Prepara la lista que se añadirá al final del archivo csv usando join.
        output = []
        [output.append("") for name in columnasFile]

        # Lista que almacenará los indices de las Columnas ingresadas por el usuario que coincidan 
        # con las Columnas del archivo csv.
        indices = []
        [indices.append(columnasFile.index(col)) for col in Columnas if col in columnasFile ]

        # Pensé en agregar una condición para no escribir en el archivo en caso de que el 
        # len(indices) == 0, pero el pdf dice que si hay menos Columnas que en la Tabla
        # (0 es menor que x Columnas en Tabla) se debe llenar con string vacio "", por lo que
        # quizás sea válido ingresar una fila llena de strings vacíos, preguntar a pantufla.
        
        # Agrega los valores según su indice en la lista de salida.
        for ind in indices:
            output[ind] = inputs[Columnas[ind]]
        
        # Agrega el output al archivo csv separando cada valor con una coma.
        file.write(",".join(output)+"\n")
        # Se ha insertado 1 fila.
        file.close()
