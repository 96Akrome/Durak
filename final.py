import re

"""
line_parser
——————–
Entradas:
Sin entradas. Se ocupa variables globales.
——————–
Salida:
(tuple) Output: tupla de 2 valores, primero corresponde a la llave de diccionario
de las expresiones regulares y el segundo a valor de rx.search
——————–
La función revisa si existe un match completo con el alguna expresión regular del
diccionario global SQL_REGEX.Si se encuentra un match, se retorna la llave de diccionario
y el valor de rx.search. En caso de que no se encuentra correspondencia entre el input
y alguna de las posibles expresiones regulares, se retorna una tupla (None,None).
"""
def line_parser():
    for key,rx in SQL_REGEX.items():
        match = rx.search(statement)
        if match:
            return key,match

"""
reviseReservedWords
——————–
Entradas:
(list) lista: Una lista con strings que puede tener nombres de tablas, de columnas, etc.
——————–
Salida:
(bool) Output: Retorna True si la lista ingresada contiene palabras reservadas, False si no.
——————–
La función contiene un conjunto local reservedWords con las palabras reservadas.
Una vez recibida la lista compara los elementos de esta con los valores en el conjunto para ver
si la lista posee palabras reservadas como elementos.
Si es asi, imprime un mensaje de error por pantalla y retorna True, de lo contrario, retorna False.
"""
def reviseReservedWords(lista):
    reservedWords = {'INSERT','ASC','DESC','INTO','VALUES','SELECT','FROM','WHERE','ORDER BY','UPDATE','SET','BY'}
    badStrings = []
    for string in lista:
        if string in reservedWords:
            badStrings.append(string)
    if (len(badStrings) > 0):
        if(len(badStrings) == 1):
            print('\nError de Sintaxis! La columna o tabla '+ ", ".join(badStrings)+' contiene una palabra reservada. linea 46 \n')
        else:
            print('\nError de Sintaxis! Las columnas o tablas '+", ".join(badStrings)+' contienen una o más palabras reservadas. linea 48 \n')
        return True
    else:
        return False

"""
checkCol
——————–
Entradas:
(list) listaInputs: Una lista con strings que puede tener nombres de tablas, de columnas, etc.
(list) listaFile: Una lista con los strings que se usaran como referencia para comparar la priera tabla.
(string) Tabla: Tabla que contiene los elementos de listaFile.
——————–
Salida:
(bool) Output: Retorna True si la lista ingresada no contiene algun string de la lista a comparar, False de lo contrario
——————–
La función revisa que esten todos los valores de la primera lista ingresada en la segunda, de no ser así, imprime los valores que no
coincidan junto a un mensaje de error para luego retornar True. Si estan todos los valores de la primera lista en la segunda, retorna False.
"""
def checkCol(listaInputs, listaFile, Tabla):
    colNotFound = [columna.strip() for columna in listaInputs if columna not in listaFile]
    if (len(colNotFound) != 0):
        if (len(colNotFound) == 1):
            print("\nError de Sintaxis! La columna " + ", ".join(colNotFound) + " no pertenece a la tabla " + Tabla + ". linea 71\n")
        else:
            print("\nError de Sintaxis! Las columnas " + ", ".join(colNotFound) + " no pertenecen a la tabla " + Tabla + ".linea 73\n")
        return True
    return False

"""
insert
——————–
Entradas:
(list) valid: lista con los grupos capturados por el match
——————–
Salida:
(void) No retorna
——————–
La función verifica que los valores ingresados cumplan las condiciones (las columnas deben existir en la tabla, no deben tener como nombre
palabras reservadas, que la tabla ingresada exista, es decir, que cuente con su respectivo archivo .csv y que la cantidad de
columnas ingresadas coincida con la cantidad de valores) para poder así, finalmente, insertarlos en la última fila de
la tabla señalada por el usuario en el query.
"""
def insert(valid):
    # Descomprime los grupos ingresados, eliminano caracteres molestos al inicio y al final de cada valor.
    Tabla = valid[0].strip()

    # Ninguna Tabla o Columna capturada puede coincidir con palabras reservadas
    if (reviseReservedWords([Tabla])):
        return
    # Abre el archivo de la Tabla correspondiente en modo r+ (lectura + append).
    try:
        file = open(Tabla + ".csv", "r+", encoding='utf-8')
        Columnas = [name.strip() for name in re.split(r',', valid[1])]
        Values = [name.strip() for name in re.split(r',', valid[2])]

        # Si la cantidad de columnas es distinta a la cantidad de valores
        # o si alguno de estos incluye palabras reservadas será error de sintaxis.
        if (len(Columnas) != len(Values)):
            print("\nError de Sintaxis !, la cantidad de columnas ingresadas no coincide con la cantidad de valores ingresados. linea 107\n")
            file.close()
            return
        if (reviseReservedWords(Columnas)):
            file.close()
            return

        # Lee la primera línea del archivo, elimina el salto de línea al final y separa el string
        # según las comas para obtener una lista con las Columnas del archivo.
        columnasFile = file.readline().strip().split(",")

        # Si se ingresan columnas que no existen en la tabla será error de sintaxis.
        if(checkCol(Columnas, columnasFile, Tabla)):
            file.close()
            return

        # Diccionario donde valor = columnas de la tabla y llave = indice de la columna en la tabla
        indices = { Columna : columnasFile.index(Columna) for Columna in columnasFile}

        # Lista con la nueva fila que se insertará en la tabla.
        output = ["" for columna in columnasFile] # Se rellena con strings vacíos para darle el largo que debe tener una fila en la tabla ingresada.
        # Se rellena Output con los valores en el indice correspondiente
        for i in range(len(Columnas)):
            output[indices[Columnas[i]]] = Values[i].strip("'")

        # Agrega el output al archivo csv separando cada valor con una coma.
        file.write(",".join(output)+"\n")
        print("\nSe ha insertado 1 fila.\n")
        file.close()

    except FileNotFoundError:
        print('\nLa tabla '+Tabla+' no existe, intente nuevamente.\n')
        return

"""
update
——————–
Entradas:
(list) valid: lista con los grupos capturados por el match
——————–
Salida:
(void) No retorna
——————–
La función verifica que los valores ingresados cumplan las condiciones (las columnas deben existir en la tabla, no deben tener como nombre
palabras reservadas, que la tabla ingresada exista, es decir, que cuente con su respectivo archivo .csv y que se cumpla al menos una
de las restricciones ingresadas en WHERE por el usuario) para poder así, finalmente, actualizar la tabla señalada por
el usuario en el query con los valores ingresados, imprimiendo por pantalla la cantidad de filas que fueron modificadas.
"""
def update(valid):
    # Descomprime el nombre de la tabla ingresada.
    Tabla = valid[0].strip()
    # Ninguna Fila o Columna capturada puede coincidir con palabras reservadas
    if (reviseReservedWords([Tabla])):
        return

    try:# Abre el archivo de la Tabla correspondiente en modo r (lectura).
        fileTable = open(Tabla + ".csv", "r", encoding='utf-8')

        # Descomprime los cambios ingresados en SET, separándolos en una lista por comas (",") y después en otra por igual ("=").
        Set = [name.strip().split("=") for name in re.split(r',', valid[1])]

        # Guarda las lineas del archivo en una lista de lista, donde cada lista interna es una fila.
        lineas = fileTable.readlines()
        cont = 0
        while(cont < len(lineas)):
            lineas[cont] = lineas[cont].strip().split(",") # Separa las filas usando la coma (",") para generar las columnas
            cont += 1
        fileTable.close()

        columnasFile = lineas[0] # Guarda las columnas que tiene la tabla.
        ColumnasSet = [Set[i][0].strip() for i in range(len(Set))] # Guarda las columnas que ingresó el usuario en SET.
        # Asigna una lista con las columnas que ingresó el usuario en SET que existen en la tabla
        # y una lista con las columnas que ingresó el usuario que no existen en la tabla.
        # Si se ingresan columnas que no existen en la tabla o si las columnas en set incluyen
        # palabras reservadas se imprimirá error de sintaxis y saldrá de la función
        if (checkCol(ColumnasSet, columnasFile, Tabla)):
            return
        if (reviseReservedWords(ColumnasSet)):
            return

        # Descomprime las condiciones ingresadas en WHERE, separándolas por OR y luego por AND, manteniendo así la precedencia del segundo.
        Where = [name.strip().split("AND") for name in re.split(r'OR', valid[2])]

        # Separa las listas internas de WHERE haciendo split con el signo igual ("=") y revisa que la columna se encuentre en la tabla.
        # De no estar la columna en la tabla se imprimirá "Error de Sintaxis !" por consola.
        # Where quedará como se muestra en la siguiente línea:
        # Where = [[[columna1, cosa1]], [[columna2, cosa2], [columna3, cosa3]]], siendo los elementos en Where[i] las listas de condiciones
        # separadas por un OR, los elementos en Where[i][j] las condiciones separadas por un AND y los elementos en Where[i][j][k]
        # las columnas con el valor que se desea buscar.
        for i in range(len(Where)):
            for j in range(len(Where[i])):
                col, value = Where[i][j].split("=")
                col = col.strip() # col puede ser de la forma Columna o de la forma Tabla.Columna
                value = value.strip().strip("'")
                Where[i][j] = [col, value]
            ColumnasWhere = [condicion[0] for condicion in Where[i]]
            # Asigna una lista con las columnas que ingresó el usuario en WHERE que existen en la tabla
            # y una lista con las columnas que ingresó el usuario que no existen en la tabla.
            if (checkCol(ColumnasWhere, columnasFile, Tabla)):
                return
            if (reviseReservedWords(ColumnasWhere)):
                return

        # Ya no quedan más casos de error, ahora hay que verificar si se cumple alguna condición para modificar los datos de la tabla.
        indicesOutput = set() # Almacena los indices de las filas a modificar.
        for condiciones in Where:
            matchCondiciones = set() # Conjunto para realizar intersección entre condiciones unidas por AND
            for i in range(len(condiciones)):
                j = 1
                filas = set()
                cont = 0
                while (j < len(lineas)):
                    if (condiciones[i][1] == lineas[j][columnasFile.index(condiciones[i][0])]): # Si valor en set = valor en tabla
                        filas.add(j) # Agrega el indice de la fila que cumple la condición ingresada
                    j = j + 1
                if (i == 0):
                    matchCondiciones = matchCondiciones.union(filas) # Si es la primera iteración se le asigna el mismo valor para que no se anule
                matchCondiciones = matchCondiciones.intersection(filas) # Intersección entre conjunto filas y matchCondiciones
            indicesOutput = indicesOutput.union(matchCondiciones) # Unión entre conjuntos separados por OR
        if (len(indicesOutput) == 0):
            print ("\nNo se pudo actualizar la tabla con la información entregada.\n")
            return

        # Modificación de las filas de la tabla:
        for indice in indicesOutput:
            for col, val in Set:
                lineas[indice][columnasFile.index(col.strip())] = val.strip().strip("'")

        # Actualización de la tabla en el archivo css
        file = open(Tabla + ".csv", "w", encoding='utf-8')
        for linea in lineas:
            file.write(",".join(linea)+"\n")
        file.close()
        if(len(indicesOutput) == 1):
            print("\nSe ha actualizado " + str(len(indicesOutput)) + " fila\n")
        else:
            print("\nSe han actualizado " + str(len(indicesOutput)) + " filas\n")

        return
    except FileNotFoundError:
        print('\nLa tabla indicada no existe, intente nuevamente.\n')
        return

"""
select
——————–
Entradas:
(list) valid: lista con los grupos capturados por el match
——————–
Salida:
(void) No retorna
——————–
La función verifica que los valores ingresados cumplan las condiciones (las columnas deben existir en la tabla, no deben tener como nombre
palabras reservadas, que las tablas ingresadas existan, es decir, que cuenten con sus respectivos archivos .csv (2 archivos en el caso de
incluir INNER JOIN), que se cumpla al menos una de las restricciones ingresadas en WHERE por el usuario, en caso de ser ingresado, y que
la columna ingresada en ORDER BY (en caso de ingresarlo) exista en la tabla) para poder así, finalmente, poder imprimir por
pantalla las columnas solicitadas de una o dos tablas con su respectivo orden o por el orden señalado por el usuario.
"""
def select(valid):

    Tablas = [] # [ tabla 1, tabla 2], Tablas puede tener largo 1 o 2, dependiendo si se incluye INNER JOIN
    Tablas.append(valid[1].strip()) # Tablas = [tabla 1], agrega la primera tabla a Tablas
       # Ingresos opcionales:
    if(valid[2] != None): # Pregunta si se incluye el comando INNER JOIN
        Tablas.append(valid[2].strip()) # Tablas = [tabla 1, tabla 2], agrega tabla 2 a Tablas
    # Ninguna tabla capturada puede coincidir con palabras reservadas
    if (reviseReservedWords(Tablas)):
        return

    try:
        archivos = dict()
        for tabla in Tablas:
            fileTable = open(tabla + ".csv", "r", encoding='utf-8') # Abre el archivo de la Tabla correspondiente en modo r (lectura).
            lineas = fileTable.readlines() # Guarda las lineas del archivo en una lista de lista, donde cada lista interna es una fila.
            cont = 0
            while(cont < len(lineas)):
                lineas[cont] = lineas[cont].strip().split(",") # Separa las filas usando la coma (",") para generar las columnas
                cont += 1
            archivos[tabla] = lineas # Agrega el archivo separado en filas y columnas al diccionario con llave = nombre tabla
            fileTable.close()

        colTablas = archivos[Tablas[0]][0] # Lista que guarda todas las columnas de las tablas ingresadas (sin repetir) para futuras comparaciones.
        if(len(Tablas) > 1):
            colTablas = colTablas + [columna for columna in archivos[Tablas[1]][0] if columna not in colTablas]

        Select = [name.strip() for name in re.split(r',', valid[0])] # Desempaqueta las columnas ingresadas en el query [[Columna1] , [columna2]]

        if (Select == ['*']): # Si se ingresó * en select, este tomará todas las columnas de las tablas ingresadas.
            Select = colTablas.copy()
        # Check de WHERE
        if(valid[3] != None ): # Revisa si el usuario ingreso WHERE en su input para desempaquetar sus datos
            Where = [name.split("AND") for name in re.split(r'OR', valid[3])] # [[cond11 = value11 , cond12 = value12], [cond21 = val21]] [[And, And] OR [And]], OR = ","
        else:
            Where = [] # Se deja como lista vacia dado que no fue ingresado

        # Check de ORDER BY
        if(valid[4] != None ): # Revisa si el usuario ingreso ORDER BY en su input para esempaquetar sus datos
            Order = [valid[4].strip()] # Columna que se quiere usar para ordenar los datos mostrados en pantalla
            By = valid[5].strip() # ASC | DESC
        else:
            Order = [] # Se deja como lista vacia dado que no fue ingresado
            By = "" # Se deja como string vacio dado que no fue ingresado

        # Casos de error, palabra reservada o columna not in tablas
        if (reviseReservedWords(Select)):
            return
        if (checkCol(Select, colTablas, " ni a la tabla ".join([tabla for tabla in Tablas]))):
            return

        Output = [] # Lista que almacena las OutputFila que cumplan las condiciones solicitadas
        blend = [] # Guarda la o las columnas que se deben unir para juntar tablas
        if (len(Where) != 0): # Si se ingresa WHERE
            # Separa las condiciones del WHERE haciendo split en el signo =
            for cont in range(len(Where)): # Condiciones separadas por OR

                OutputMatch = [] # Almacena las filas que cumplen las condiciones señaladas
                for cont2 in range(len(Where[cont])): # Condiciones separadas por AND
                    matchRow = [] # Lista que almacena la fila con los elementos solicitados
                    Where[cont][cont2] = Where[cont][cont2].split("=")
                    Where[cont][cont2][0] = Where[cont][cont2][0].strip().split(".") # Si es de la forma tabla.columna tendrá largo 2, else largo 1
                    Where[cont][cont2][1] = Where[cont][cont2][1].strip().split(".")
                    # Where[cont][cont2][0] -> lado izquierdo de la igualdad
                    # Where[cont][cont2][1] -> lado derecho de la igualdad
                    # Si el usuario ingresa INNER JOIN
                    if(len(Tablas) == 2):
                        if(len(Where[cont][cont2][0]) == 1): # Si la parte izquierda de la igualdad de alguna condición no es de la forma tabla.columna -> error sintaxis
                            print("\nError de Sintaxis! Use notacion Tabla.Columna al usar INNER JOIN.\n")
                            return
                        tabla1 = Where[cont][cont2][0][0].strip()
                        col1 = Where[cont][cont2][0][1].strip()

                        # Casos de error:
                        if (reviseReservedWords([tabla1]+[col1])):
                            return
                        if (tabla1 not in Tablas):
                            print('\nError de Sintaxis ! La tabla ' + tabla1+ ' es distinta de las tablas ingresadas. linea 342\n')
                            return
                        if (col1 not in archivos[tabla1][0]):
                            print('\nError de Sintaxis ! La columna '+col1+' no pertenece a la tabla '+ tabla1+'. linea 345\n')
                            return
                        indice1 = archivos[tabla1][0].index(col1)

                        if(len(Where[cont][cont2][1]) == 2): # Si la parte derecha de la igualdad es de la forma tabla.columna
                            tabla2 = Where[cont][cont2][1][0].strip() # tabla ingresada en la parte derecha de la igualdad
                            col2 = Where[cont][cont2][1][1].strip() # columna ingresada en la parte derecha de la igualdad
                            if(tabla1 != tabla2 and col1 == col2): # si tabla1.Columna = tabla2.Columna, columnas iguales
                                blend.append(col1) # agrega la columna a la lista blend

                            # Casos de error
                            if (reviseReservedWords([tabla2]+[col2])):
                                return
                            if (tabla2 not in Tablas):
                                print('\nError de Sintaxis ! La tabla ' + tabla2 + ' es distinta de las tablas ingresadas. linea 359\n')
                                return
                            if (col2 not in archivos[tabla2][0]):
                                print('\nError de Sintaxis ! La columna ' + col2 + ' no pertenece a la tabla ' + tabla2 + '. linea 362\n')
                                return

                            indice2 = archivos[tabla2][0].index(col2) # Indice de la columna ingresada en la parte derecha en su respectiva tabla

                            for fila1 in range(1, len(archivos[tabla1])): # Empieza a buscar las filas que cumplan la condición ingresada
                                for fila2 in range(1, len(archivos[tabla2])):
                                    if (archivos[tabla1][fila1][indice1] == archivos[tabla2][fila2][indice2]):
                                        for tabla in Tablas:
                                            if tabla != tabla1:
                                                ind1 = Tablas.index(tabla1)
                                                ind2 = Tablas.index(tabla) # Al fijar los indices se asegura de que no se alteren los ordenes al ingresar tabla.columna
                                        matchRowList = ["",""]
                                        matchRowList[ind1] = archivos[tabla1][fila1]
                                        matchRowList[ind2] = archivos[tabla2][fila2]
                                        matchRow.append(matchRowList.copy())
                                        #matchRow.append((archivos[tabla1][fila1], archivos[tabla2][fila2]))

                        else: # Si la parte derecha tiene largo = 1 y es de la forma value
                            # Código para tabla.columna = valor
                            val = Where[cont][cont2][1][0].strip()
                            # Si val no es un número ni un 'string' ni un número negativo -> error
                            if(val.isnumeric() or (val[0] == "'" and val[-1] == "'" and len(val) > 2) or (val[0] == "-" and val.count("-") == 1 and val.strip("-").isnumeric())):
                                val = val.strip("'")
                                
                                for fila in range(1, len(archivos[tabla1])): # Itera por cada fila de la tabla 1
                                    if(archivos[tabla1][fila][indice1] == val): # Encuentra una fila-columna que tiene el mismo valor que value
                                        item1 = archivos[tabla1][fila] # Guarda la fila completa en una variable
                                        for key in archivos.keys():
                                            if (key != tabla1): # Empieza a hacer matching con cada uno de los elementos de la otra tabla
                                                for fila2 in range(1, len(archivos[key])): # Al no tener restricción en la segunda tabla, toma todas sus filas
                                                    item2 = archivos[key][fila2]
                                                    for tabla in Tablas:
                                                        if tabla != tabla1:
                                                            ind1 = Tablas.index(tabla1)
                                                            ind2 = Tablas.index(tabla)
                                                    # Al fijar los indices se asegura de que no se alteren los ordenes al ingresar tabla.columna
                                                    matchRowList = ["",""]
                                                    matchRowList[ind1] = item1
                                                    matchRowList[ind2] = item2
                                                    matchRow.append(matchRowList.copy())
                                # Convierte los valores numericos en números para poder ejecutar sort más adelante
                                try:
                                    if ('.' in val):
                                        val = float(val)
                                    else:
                                        val = int(val)
                                except ValueError:
                                    val = val
                            else:
                                print('\nError de Sintaxis ! linea 410\n')
                                return

                    else: # Sin INNER JOIN
                        blend.append(1)
                        if(len(Where[cont][cont2][1]) > 1 or len(Where[cont][cont2][0]) > 1): # Si el lado izquierdo o el derecho incluye punto (.)
                            print("\nError de Sintaxis! No se permite el uso de notacion Tabla.Columna sin INNER JOIN.\n") # Al no haber inner join debe ser de la forma Columna = valor, sin puntos
                            return
                        col1 = Where[cont][cont2][0][0].strip()
                        val = Where[cont][cont2][1][0].strip()
                        # Casos de error, palabra reservada o palabra not in tabla
                        if (reviseReservedWords([col1])):
                            return
                        if (checkCol([col1], colTablas, Tablas[0])):
                            return
                        indice1 = archivos[Tablas[0]][0].index(col1)
                        # Columna = Valor
                        if(val.isnumeric() or (val[0] == "'" and val[-1] == "'" and len(val) > 2) or (val[0] == "-" and val.count("-") == 1 and val.strip("-").isnumeric())):
                            val = val.strip("'")
                            
                            for fila in range(1,len(archivos[Tablas[0]])): # Revisa todas las filas de la tabla ingresada
                                if(archivos[Tablas[0]][fila][indice1] == val): # Si la columna de la fila = valor ingresado, lo guarda en la lista
                                    matchRow.append([archivos[Tablas[0]][fila], archivos[Tablas[0]][fila]])
                            # Convierte los valores numericos en números para poder ejecutar sort más adelante
                            try:
                                if ('.' in val):
                                    val = float(val)
                                else:
                                    val = int(val)
                            except ValueError:
                                val = val

                        else: # Columna = Columna
                            # Casos de error (palabra reservada o palabra not in tabla)
                            if (reviseReservedWords([val])):
                                return
                            if (checkCol([val], colTablas, Tablas[0])):
                                return

                            indice2 = archivos[tabla1][0].index(val)
                            for fila in range(1,len(archivos[Tablas[0]])): # Revisa todas las filas de la tabla ingresada
                                if(archivos[Tablas[0]][fila][indice1] == archivos[Tablas[0]][fila][indice2]): # Si valor de columna1 = valor columna 2, guarda la fila en la lista
                                    matchRow.append([archivos[Tablas[0]][fila], archivos[Tablas[0]][fila]])
                    if(cont2 == 0):
                        OutputMatch = matchRow.copy() # Si es la primera iteración, OutputMatch toma el mismo valor que matchRow
                    else:
                        OutputMatch = [value for value in matchRow if value in OutputMatch] # Intersecta las condiciones separadas por un AND

                # Une las condiciones separadas por un OR
                for filas in OutputMatch:
                    if filas not in Output:
                        Output.append(filas)

        else: # Si no se ingresa WHERE
            blend.append(1)
            for fila in range(1, len(archivos[Tablas[0]])): # Si no hay WHERE, guarda todas las filas de la tabla ingresada
                for i in range(len(archivos[Tablas[0]][fila])):
                    # Convierte los valores numericos en números para poder ejecutar sort más adelante
                    try:
                        if ('.' in archivos[Tablas[0]][fila][i]):
                            archivos[Tablas[0]][fila][i] = float(archivos[Tablas[0]][fila][i])
                        else:
                            archivos[Tablas[0]][fila][i] = int(archivos[Tablas[0]][fila][i])
                    except ValueError:
                        archivos[Tablas[0]][fila][i] = archivos[Tablas[0]][fila][i]
                Output.append([archivos[Tablas[0]][fila],archivos[Tablas[0]][fila]])

        if(len(Output) > 0): # Si hay al menos una fila que cumpla las condiciones ingresadas y una condicion de la forma tabla.columna = tabla2.columna
            # Código para ORDER BY
            if(len(blend) == 0): # Reemplazar 0 por -1 para eliminar restriccion Tabla1.columna1 = tabla2.columna1
                print("\nError de Sintaxis! No se recibió comparación del tipo Tabla1.Columna1 = Tabla2.Columna1.")
                return
            else:
                if(len(Order) > 0): # Si se ingresa ORDER BY
                    if (len(Tablas) == 1 and len(Order[0].split(".")) == 1):
                        if(len(Order[0].split(".")) == 1):
                            Order.append(Tablas[0])
                            Order.reverse() # -> Order queda de la forma [tabla, columna]
                    else:
                        Order = Order[0].split(".") # -> [tabla, columna]
                        if(len(Order) == 1): # Si Order no es de la forma tabla.columna -> error
                            print("\nError de Sintaxis! Use notacion Tabla.Columna al usar INNER JOIN.\n")
                            return
                        if(Order[0] not in Tablas):
                            # Casos de error: Tabla inexistente, palabras reservadas, columna inexistente
                            print("\nError de Sintaxis ! La tabla "+Order[0]+" no coincide con las tablas ingresadas. linea 487\n")
                            return
                        if(reviseReservedWords(Order[0]) or reviseReservedWords(Order[1])):
                            return
                        if(checkCol([Order[1]], archivos[Order[0]][0], Order[0])):
                            return

                    indiceSort = archivos[Order[0]][0].index(Order[1])
                    Output.sort(key=lambda x: x[Tablas.index(Order[0])][indiceSort])# Función Lambda, permite aplicar sort usando un indice en particular como pivote.

                    if (By.strip() == "DESC"): # Si pide descendiente basta con invertir la lista.
                        Output.reverse()

                # Código para imprimir por pantalla las listas seleccionadas:
                # colTablas tiene las columnas de ambas tablas en orden y sin repetir.
                listaIndices = [] # guarda los indices de las columnas solicitadas (indice tabla, indice elemento en Tablas[indice])
                OutputPrint = [] # Lista final con todas las filas ordenadas
                for elemento in Select:
                    for indice in range(len(Tablas)-1,-1,-1): # Recorre los elementos desde la última posición hasta la primera
                        if elemento in archivos[Tablas[indice]][0]: # Guarda los indices de las columnas detectadas, (indice tab, indice col)
                            listaIndices.append((indice, archivos[Tablas[indice]][0].index(elemento)))
                            break

                for fila in range(len(Output)):
                    OutputMatch = [] # Guarda la fila ordenada
                    for tabla, columna in listaIndices:
                        OutputMatch.append(Output[fila][tabla][columna])
                    OutputPrint.append(OutputMatch)
                print()
                lens = [] # Código para darle formato a los datos que se imprimirán en pantalla
                for col in zip(*OutputPrint): # Llena una lista con los largos de cada elemento a imprimir para generar una distancia
                    lens.append(max([len(str(v)) for v in col])) # dinámica entre los elementos y que se vean con la misma separación
                format = "     ".join(["{:<" + str(l) + "}" for l in lens]) # Alinea los valores hacia la izquierda
                for row in OutputPrint:
                    print(format.format(*row))
                print()

        else:
            print("La información solicitada no existe.")


    except FileNotFoundError:
        if(len(Tablas) == 1):
            print("La tabla ingresada no existe.")
        else:
            print("Las tablas ingresadas no existen.")
        return

# Main loop
while(True):
    #Recepción de input
    print ("Ingrese su query:")
    statement = input()
    #condicion de salida de loop infinito
    if(statement == 'EXIT'):
        print('\nSe recibió comando de salida.Terminando la ejecución.\n')
        break
    #un diccionario con posibles llaves de expresiones completas
    SQL_REGEX = {
    'UPDATE_Key' : re.compile(r'^UPDATE\s+([^\s;,]+)\s+SET\s+((?:[^\s\.\'=*,;]+\s*=(?:\s*\'\s*[^\']+\s*\'|\s*-?\d+(?:\.\d+)?)(?:\s*,\s*[^\s\.\'=*,;]+\s*=(?:\s*\'\s*[^\']+\s*\'|\s*-?\d+(?:\.\d+)?))*))\s+WHERE\s+((?:[^\s\.\'=*,;]+\s*=(?:\s*\'\s*[^\']+\s*\'|\s*-?\d+(?:\.\d+)?)(?:\s*(?:AND|OR)\s*[^\s\.\'=*,;]+\s*=(?:\s*\'\s*[^\']+\s*\'|\s*-?\d+(?:\.\d+)?))*));{1}$'),
    'SELECT_Key' : re.compile(r'^SELECT\s+((?:\s*[^\s,;=\']+)(?:(?:\s*,\s*[^\s,*=;\']+)*))\s+FROM\s+([^\s;,]+)(?:(?:\s+INNER\sJOIN\s+([^\s;]+))?(?:(?:\s+WHERE\s+((?:[^\s.\'=*,;]+(?:\.[^\s.\'=*,;]+)?\s*=(?:(?:\s*\'\s*[^\']+\s*\'|\s*-?\d+(?:.\d+)|\s*[^\s.\'=*;,]+(?:\.[^\s.\'=*,;]+)?))(?:(?:\s+(?:AND|OR)\s+[^\s.\'=,;*]+(?:\.[^\s.\'=,*;]+)?\s*=(?:(?:\s*\'\s*[^\']+\s*\'|\s*-?\d+(?:.\d+)|\s*[^\s.\'=,;*]+(?:\.[^\s.\'=;,*]+)?)))*)?)))))?(?:\s+ORDER\sBY\s+([^*\s=\';,\.]+(?:\.[^\s\.\'=;,*]+)?)\s+(ASC|DESC))?;{1}$'),
    'INSERT_Key':re.compile(r'^INSERT\sINTO\s+([^\s,]+)\s+\(\s*((?:\s*[^\s,=*\';]+)(?:(?:\s*,\s*[^\s,=*\';]+\s*)*))\)\s+VALUES\s+\(((?:\s*\'[^\']+\s*\'\s*|\s*-?\d+|(?:\.\d+))(?:(?:,\s*\'\s*[^\']+\s*\'\s*|\s*,\s*-?\d+|(?:\.\d+)\s*)*))\);{1}$'),
    }
    #tupla key-match
    result_tuple = line_parser()
    #isinstance verifica que la llave no es null para no generar error de
    #noneType error.
    if isinstance(result_tuple,type(None)):
        #si la llave o match son None,no había match. Es decir, fallo la sintaxis.
        print('\nError de Sintaxis ! 556\n')

    else:
        key = result_tuple[0]
        if key == 'UPDATE_Key':
            update(SQL_REGEX['UPDATE_Key'].match(statement).groups())
        elif key == 'SELECT_Key':
            select(SQL_REGEX['SELECT_Key'].match(statement).groups())
        elif key == 'INSERT_Key':
            insert(SQL_REGEX['INSERT_Key'].match(statement).groups())