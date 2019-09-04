import re

"""
line_parser
——————–
Entradas:
Sin entradas.Se ocupa variables globales.
...
——————–
Salida:
(Tuple) Output: tupla de 2 valores, primero corresponde a la llave de diccionario
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
        else:
            None,None

"""
reviseReservedWords
——————–
Entradas:
(string) Un string, que puede ser un nombre de la tabla, de columna,etc.
...
——————–
Salida:
(Int) Output: Se retorna un 0 o un 1.
——————–
La función contiene un conjunto local reservedWords con las palabras reservadas.
Una vez recibido el string, se usa funciones de set para revisar si este string pertenece
al conjunto. Si es asi, se retorna un 0 (Caso de Error de Sintaxis). Si no, se retorna 1.
"""

def reviseReservedWords(string):
    reservedWords = {'INSERT','ASC','DESC','INTO','VALUES','SELECT','FROM','WHERE','ORDER BY','UPDATE','SET'}
    if string in reservedWords:
        return 0
    return 1

"""
insert
——————–
Entradas:
(...) ...
——————–
Salida:
(void) Sin retorno.
——————–
....
"""
def update(valid):
    Tabla = valid.match(statement).groups()[0].strip(" ' ’ ")
    Set = [name2.strip(" ' ’ ") for name in re.split(r',', valid.match(statement).groups()[1]) for name2 in name.split("=")]
    Tabla = valid.match(statement).groups()[0].strip(" ' ’ ")
    Set = [name2.strip(" ' ’ ") for name in re.split(r',', valid.match(statement).groups()[1]) for name2 in name.split("=")]
    Where = [name.strip(" ' ’ ").split("AND") for name in re.split(r'OR', valid.match(statement).groups()[2])]

    # Diccionario para guardar los valores en Set, cada key es un valor a modificar en el archivo csv
    largo = 0
    Set_dict = dict()
    while (largo < len(Set) and largo + 1 < len(Set)):
        Set_dict[Set[largo]] = Set[largo + 1]
        largo = largo + 2

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
            if reviseReservedWords(col) == 0:
                print('Error de Sintaxis! (pal reserv update col)')
                return;
            value = value.strip(" ' ’ ")
            if reviseReservedWords(val) == 0:
                print('Error de Sintaxis! (pal reserv update col)')
                return;
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

def insert(valid):
    # Descomprime los grupos ingresados, eliminano caracteres molestos al inicio y al final de cada valor.
    Tabla = valid.match(statement).groups()[0]

    #Ningun grupo capturado puede coincidir con palabras reservadas
    if reviseReservedWords(Tabla)== 0:
        print()
        print('Error de Sintaxis!')
        print()
        return

    # Abre el archivo de la Tabla correspondiente en modo r+ (lectura + append).
    try:
        file = open(Tabla + ".csv", "r+", encoding='utf-8')
    except FileNotFoundError:
        print()
        print('Tabla indicada no existe. Intente de nuevo.')
        print()
        return

    Columnas = [name.strip(" ' ") for name in re.split(r',', valid.match(statement).groups()[1])]
    Values = [name.strip(" ' ") for name in re.split(r',', valid.match(statement).groups()[2])]

    #unico caso de sintax invalida.
    if (len(Columnas) != len(Values)):
        print()
        print("Error de Sintaxis!")
        print()
        return

    inputs = dict()
    i = 0;
    while (i < len(Columnas)):
        #Revisa que ninguna columna ni valor coincidan con palabras reservadas.
        if (reviseReservedWords(Columnas[i]) & reviseReservedWords(Values[i])):
            inputs[Columnas[i]] =  Values[i]
            i = i + 1
        else:
            print()
            print('Error de Sintaxis!')
            print()
            return

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

    # Agrega los valores según su indice en la lista de salida.
    for ind in indices:
        output[ind] = inputs[columnasFile[ind]]

    # Agrega el output al archivo csv separando cada valor con una coma.
    file.write(",".join(output)+"\n")
    print()
    print("Se ha insertado 1 fila.")
    print()
    file.close()

def select(valid):

    Tablas = [] # [ tabla 1, tabla 2], Tablas puede tener largo 1 o 2, dependiendo si se incluye INNER JOIN
    # Descomprime los grupos ingresados, eliminano caracteres molestos al inicio y al final de cada valor.
    Select = [name.strip() for name in re.split(r',', valid.match(statement).groups()[0])] # [[Columna1] , [columna2]]
    Tablas.append(valid.match(statement).groups()[1].strip()) # Tablas = [tabla 1], agrega la primera tabla a Tablas
       # Ingresos opcionales:
    if(valid.match(statement).groups()[2] != None): # Pregunta si se incluye el comando INNER JOIN
        Tablas.append(valid.match(statement).groups()[2].strip().strip("'")) # Tablas = [tabla 1, tabla 2], agrega tabla 2 a Tablas
    if(valid.match(statement).groups()[3] != None ):
        Where = [name.split("AND") for name in re.split(r'OR', valid.match(statement).groups()[3])] # [[cond11 = value11 , cond12 = value12], [cond21 = val21]] [[And, And] OR [And]], OR = ","
    else:
        Where = "" # Se deja como string vacio dado que no fue ingresado
    if(valid.match(statement).groups()[4] != None ): # Pregunta si se incluye el comando ORDER BY
        Order = valid.match(statement).groups()[4].strip() # Columna que se quiere usar para ordenar los datos mostrados en pantalla
        By = valid.match(statement).groups()[5].strip() # ASC | DESC
    else:
        Order = ""
        By = "" # Se dejan como strings vacios dado que no fueron ingresados

    #Revision de tablas y su existencia.
    archivos = dict()
    i = 0
    archivosNoExistentes = []
    while(i < len(Tablas)):
        try:
            if(reviseReservedWords(Tablas[i]) == 1):
                f = open(Tablas[i] + ".csv", "r", encoding = 'utf-8')
                lineas = f.readlines()
                cont = 0
                while(cont < len(lineas)):
                    lineas[cont] = lineas[cont].strip().split(",")
                    cont += 1
                archivos[Tablas[i]] = lineas
                f.close()
            else:
                print()
                print('Error de Sintaxis!')
                return
        except FileNotFoundError:
            archivosNoExistentes.append(Tablas[i] + ".csv")
        i += 1
# El diccionario archivos queda de la forma:
    # archivos = { Tabla1 : [[col1, col2, ..., coln],
    #                        [col1, col2, ..., coln],
    #                        [         ...         ]],
    #
    #              Tabla2 : [[col1, col2, ..., colm],
    #                        [col1, col2, ..., colm]
    #                        [         ...         ]]}
    # donde cada indice de archivos[Tabla] contiene una fila del archivo asociado a su respectiva tabla
    # * La llave Tabla2 y sus respectivos valores solo existen cuando se utiliza la expresión INNER JOIN en el input

    # Caso de error por inexistencia de archivos
    if(len(archivosNoExistentes) > 0):
        print()
        print ("No existe/n el/los archivo/s " + ", ".join(archivosNoExistentes))
        return
    else:
        # Select2 es una lista que contiene la union de las columnas de ambos archivos
        i = 0
        Select2 = []
        while(i < len(Tablas)):
            for colu in archivos[Tablas[i]][0]:
                if (colu not in Select2):
                    Select2.append(colu)
            i = i + 1

        # Si el usuario ingreso SELECT *, se asignarán todas las columnas de los archivos en el orden que estos tengan, sin repetir elementos.
        if(len(Select) == 1 and Select[0] == '*'):
            Select = Select2
        # Separa las condiciones planteadas en WHERE haciendo un split en el caracter '='
        i = 0

        # Hasta aquí ya están las siguientes variables obligatorias:
        # Tablas = [Tabla1 (FROM), Tabla2(opcional, INNER JOIN)]
        # Select = [Columna1, columna2, ..., columnan] Columnas ingresadas
        # archivos = {tabla1 : [filas], tabla2(opcional): [filas]}
        # Opcional: Select2 = [columna1, columna2 , .... , columna m] almacena todas las columnas de ambos archivos sin repetir
        indiceOutput = 0
        columnasRepetidas = list() # lista que almacena las columnas repetidas ingresadas por el usuario
        Select_dict = dict() # diccionario que tiene como llave una columna y como valor otro diccionario.

        for columna in Select:
            if(reviseReservedWords(columna) == 1):
                if (columna in Select_dict.keys()): # Si la columna ya era llave del diccionario se agrega a la lista de columnas repetidas y gatilla un error.
                    columnasRepetidas.append(columna)
                else:
                    # Construye un diccionario de la forma:
                    # Select_dict = {Columna1 : {Tabla1 : indiceDeColumna1EnTabla1,
                    #                            Tabla2 : indiceDeColumna1EnTabla2},
                    #                Columna2 : ....... }
                    Select_dict[columna] = dict() # diccionario cuya llave es una tabla y su valor es el indice en donde se encuentra la columna en dicha tabla
                    # Empieza a obtener los indices realizando comparaciones con el o los archivos.
                    for archivo in archivos.keys():
                        if (columna in archivos[archivo][0]): # archivo[0] corresponde a la primera linea del archivo csv (almacena el nombre de sus columnas)
                            Select_dict[columna][archivo] = archivos[archivo][0].index(columna)
                            indiceOutput = indiceOutput + 1 # cuentas las columnas ingresadas con SELECT que efectivamente existen en uno o más archivos

                        else:
                            Select_dict[columna][archivo] = -1
                    # El objetivo del diccionario es saber si la columna existe en algun archivo o no, lo que es representado por
                    # el indice, el cual, si es -1 significa que no existe en la tabla consultada y si es cualquier otro número,
                    # significa que existe y que ese número es el indice que tiene en dicha tabla
            else:
                print()
                print("Error de Sintaxis!")
                print()
                return;

        # Se asume que el programa debe imprimir los datos de las columnas ingresadas que existan en alguno de los archivos.
        # Junta las columnas que no existen en una lista para posteriormente imprimirlas en pantalla
        columnasNoEncontradas = []
        for columna in Select_dict.keys():
            i = 0
            verificador = 0 # si el verificador es -1 * len(archivos) significa que la columna no pertenece a ninguna tabla
            while(i < len(Tablas)):
                verificador = verificador + Select_dict[columna][Tablas[i]]
                i = i + 1
            if (verificador == -1 * len(archivos)):
                columnasNoEncontradas.append(columna)

        if (len(columnasNoEncontradas) > 0): # Si hay columnas que no pertenecen a ningun archivo, se imprimen por pantalla.
            print ("La/s columna/s "+ ", ".join(columnasNoEncontradas) + " no pertenece/n a la tabla " + " ni a la tabla ".join(Tablas) + ".")
            return

        if(indiceOutput == 0 or len(columnasRepetidas) > 0 or (len(Order) != 0 and Order not in Select)): # Casos de error.
            if (indiceOutput == 0): # Verifica si no existe ninguna columna de las que se desea mostrar.
                print("No existen las columnas solicitadas en la tabla " + " ni en la tabla ".join(Tablas) + ".")
            elif (len(Order) != 0 and Order not in Select): # Se intenta hacer Sort by con una columna que no fue ingresada.
                print("La columna en la que desea utilizar la expresión SORT BY no existe dentro de las columnas ingresadas en SELECT.")
            else: # Se ingresaron columnas repetidas y explota.
                print("Error de Sintaxis !, las siguientes columnas estan repetidas en el input: " + ", ".join(list(set(columnasRepetidas))) + ".")

        else:

            # Empieza la magia.
            # Caso 0: Select blah from tabla
            OutputMatch = [] # Contiene la información que se mostrará por pantalla al obtener los datos de la/s tabla/s
            if(Where == ""): # Si where es vacio, tampoco hay inner join -> statement = SELECT columnas FROM tabla1, order by no importa por ahora

                fila = 1
                tabla = archivos[Tablas[0]].copy()
                while(fila < len(tabla)):
                    OutputMatch.append(tabla[fila])
                    fila = fila + 1



            else:
                # Where quedará como se muestra en la siguiente línea:
                # Where = [[[columna1, cosa1]], [[columna2, cosa2], [columna3, cosa3]]], quedando los datos unidos por un AND en una misma lista
                # reemplazando columna1, 2 o 3 por Tabla.columna1, 2 o 3 según corresponda.
                while(i < len(Where)):
                    j = 0

                    while (j < len(Where[i])):
                        col, value = Where[i][j].split("=")
                        col = col.strip() # col puede ser de la forma Columna o de la forma Tabla.Columna
                        value = value.strip()
                        if(reviseReservedWords(col) == 1 & reviseReservedWords(val) == 1):
                            Where[i][j] = [col, value]
                            j = j + 1
                        else:
                            print('Error de Sintaxis! (columnas de where)')
                            return

                    i = i + 1

                # Iteración para analizar las condiciones en Where
                cont = 0
                while(cont < len(Where)): # la cantidad de iteraciones depende de la cantidad de OR en el input
                    matchColumnas = 0 # Representa la cantidad de columnas en Where que coinciden con las existentes en los archivos
                    OutputMatch = [] # Almacena las filas que cumplen las condiciones señaladas
                    cont2 = 0
                    blend = [] # Guarda la o las columnas que se deben unir para juntar tablas
                    inputValidation = 0 # su valor cambiará entre 0 y 1 para verificiar si al incluir INNER JOIN también
                    # se incluye una condición del tipo tabla.columna = tabla2.columna, condición que permitirá unir ambas tablas.

                    # Búsqueda de columnas
                    while (cont2 < len(Where[cont])): # la cantidad de iteraciones depende de la cantidad de AND en el input separados por un OR

                        tabCol, value = Where[cont][cont2].split("=")
                        matchRow = [] # matchRow es una lista para almacenar las filas que cumplan las condiciones del WHERE
                        value = value.strip()
                        tabCol = tabCol.strip()
                        # Casos posibles:
                        # Caso 1: len(Tablas) = 1 -> el usuario no ingresó INNER JOIN, por lo tanto las columnas son de la forma columna
                        # Caso 2: len(Tablas) = 2 -> el usuario ingresó INNER JOIN, por lo tanto las columnas son de la forma tabla.columna

                        # Caso 1: len(Tablas) = 1
                        if (len(Tablas) == 1): # No hay inner join
                            # Casos posibles:
                            # Caso 1.1: value es un valor de la forma 'string' o un número entero|flotante
                            # Caso 1.2: value es una columna

                            # Caso 1.1:
                            # Consulta si value es un string que empieza y termina con comilla simple o si es un numero, de ambas formas será un valor
                            if (value.isnumeric() or (len(value) > 2 and value[0] == "'" and value[-1] == "'")):

                                # Columna = Valor -> TabCol = value
                                value = value.strip("'") # si es un string quedarán solo los caracteres, si es un numero quedará igual

                                if(tabCol in archivos[Tablas[0]][0]):
                                    indice = archivos[Tablas[0]][0].index(tabCol)
                                    # el valor de una columna de una fila de la tabla coincide con value
                                    # agrega la fila completa a matchRow
                                    fila = 1
                                    tabla = archivos[Tablas[0]]
                                    while(fila < len(tabla)):
                                        if(tabla[fila][indice] == value):
                                            matchRow.append(tabla[fila])
                                        fila = fila + 1
                                    # Al final del programa hay un if que se encarga de intersectar las listas de matchRow
                                    # generadas por los AND


                                # Caso 1.2:
                                # value es una columna
                            else:

                                # Columna = Columna2

                                if(tabCol in archivos[Tablas[0]][0] and value in archivos[Tablas[0]][0]):
                                    indice1 = archivos[Tablas[0]][0].index(tabCol)
                                    indice2 = archivos[Tablas[0]][0].index(value)
                                    # el valor de una columna de una fila de la tabla coincide con el valor de otra columna de la misma fila
                                    # agrega la fila completa a matchRow
                                    fila = 1
                                    tabla = archivos[Tablas[0]]
                                    while(fila < len(tabla)):
                                        if(tabla[fila][indice1] == tabla[fila][indice2]):
                                            matchRow.append(tabla[fila])
                                        fila = fila + 1
                                    # Al final del programa hay un if que se encarga de intersectar las listas de matchRow
                                    # generadas por los AND

                        # Caso 2:
                        else: # len(Tablas != 1) En el caso de haber incluido INNER JOIN en el input
                            tabCol = tabCol.split(".") # tabla.columna -> [tabla, columna]
                            if(len(tabCol) > 1): # si no es > 1 quiere decir que no se ingresó como corresponde (ej: columna en vez de tabla.columna)
                                # tabla1 y columna1 son los valores de tabla.columna por separados.
                                tabla1 = tabCol[0].strip()
                                columna1 = tabCol[1].strip()
                                if (len(columna) == 0):
                                    print("Error de Sintaxis !")
                                else:
                                    if(columna1 in archivos[tabla1][0]): # Verifica si la columna ingresada existe en el archivo ingresado.
                                        indice1 = archivos[tabla1][0].index(columna1) # Posición de la columna ingresada en la tabla ingresada

                                        # Casos posibles:
                                        # Caso 2.1: value es de la forma 'string' or numero (en escencia, un valor cualquiera)
                                        # Caso 2.2: value es de la forma Tabla.Columna

                                        # Caso 2.1:

                                        if (value.isnumeric() or (len(value) > 2 and value[0] == "'" and value[-1] == "'")): # Si no comienza y termina con '
                                            # no es un string, es un número.

                                            # Columna = Valor -> Tabla.Col = value, tabla1 = tabla, columna1 = columna
                                            value = value.strip("'") # si es un string quedarán solo los caracteres, si es un numero quedará igual

                                            if(columna1 in archivos[tabla1][0]):
                                                indice1 = archivos[tabla1][0].index(columna1)
                                                # el valor de una columna de una fila de la tabla coincide con value
                                                # agrega la fila completa a matchRow2
                                                fila = 1
                                                tabla = archivos[tabla1]
                                                while(fila < len(tabla)):
                                                    if(tabla[fila][indice1] == value):
                                                        item1 = tabla[fila]
                                                        for key in archivos.keys():
                                                            if (key != tabla1):
                                                                fila2 = 1
                                                                while(fila2 < len(archivos[key])):
                                                                    item2 = archivos[key][fila2]
                                                                    matchRow.append((item1, item2))
                                                                    fila2 = fila2 + 1
                                                    fila = fila + 1


                                                # Al final del programa hay un if que se encarga de intersectar las listas de matchRow
                                                # generadas por los AND

                                        # Caso 2.2
                                        else:

                                            # TODO inputValidation = 1 si se cumple tabla1.columna = tabla2.columna
                                            # en su totalidad pierde la opción de ser valor, por lo que value sería una columna
                                            value = value.split(".") # -> [tabla, columna]
                                            if(len(value) > 1): # si no es mayor a 1, mismo error de tabCol
                                                if(value[1].strip() in archivos[value[0].strip()][0]): # verifica si la columna de value
                                                    # existe en la tabla ingresada en value

                                                    tabla2 = value[0].strip() # Tabla ingresada en values
                                                    columna2 = value[1].strip() # Columna ingresada en values
                                                    indice2 = archivos[tabla2][0].index(columna2) # Posición de la columna a comparar en la tabla ingresada

                                                    if(columna1 == columna2 and tabla1 != tabla2): # tabla1.columna = tabla2.columna, hay un punto de union
                                                        inputValidation = 1
                                                        blend.append(columna1)
                                                    Archivo2 = archivos[tabla2].copy()
                                                    Archivo1 = archivos[tabla1].copy()
                                                    fila1 = 1 # Iterador de la tabla que contiene a indice1, parte desde 1 para omitir la fila con nombres de columnas
                                                    while (fila1 < len(archivos[tabla1])):
                                                        fila2 = 1
                                                        while(fila2 < len(Archivo2)):
                                                            if (Archivo1[fila1][indice1] == Archivo2[fila2][indice2]):

                                                                matchRow.append((Archivo1[fila1], Archivo2[fila2]))
                                                                Archivo2.remove(Archivo2[fila2])
                                                            else:
                                                                fila2 = fila2 + 1
                                                        fila1 = fila1 + 1

                        if(cont2 == 0):
                            OutputMatch = matchRow.copy() # Si es la primera iteración, OutputMatch toma el mismo valor que matchRow

                        else:
                            OutputMatch = [value for value in matchRow if value in OutputMatch] # Intersecta la lista matchRow con la lista OutputMatch
                            # Si no es la primera iteración, OutputMatch toma el valor de la intersección entre OutputMatch y matchRow para asegurar
                            # que se cumplan las condiciones unidas por un AND


                        cont2 = cont2 + 1
                        """
                        if(len(OutputMatch) > 0):
                            cont2 = len(Where[cont])
                        else:
                            OutputMatch = [] """
                    if(len(OutputMatch) > 0):
                        cont = len(Where)
                    cont = cont + 1
                # En este momento se tienen: OutputMatch = [[fila1], [fila2], ...] para los casos 1,
                #                            OutputMatch = [(fila1 tabla1, fila1 tabla2), (fila 2 tabla1, fila2 tabla2),....] para los casos 2

            if(len(OutputMatch) >0):
                # Código para ORDER BY // Aqui hice tab
                if(len(Order) > 0):
                    if(len(Tablas) == 1):
                        indice = Select_dict[Order][Tablas[0]]
                        if(indice != -1):
                            OutputMatch.sort(key=lambda x: x[indice])# Función Lambda,
                            # permite aplicar sort usando un indice en particular como pivote.
                            if (By.strip() == "DESC"): # Si pide desceniente basta con invertir la lista.
                                OutputMatch.reverse()
                        else:
                            print()
                            print("La columna que ingresó después del comando ORDER BY no existe en la tabla.")
                    else: # Considerando inner join
                        indice = -1
                        i = 0
                        while (i < len(Tablas)):
                            if (Order in archivos[Tablas[i]][0]):
                                indice = archivos[Tablas[i]][0].index(Order)
                                tabla = i
                            i = i + 1
                        if (indice == -1):
                            print()
                            print("La columna que ingresó después del comando ORDER BY no existe en las tablas.")
                        else:
                            OutputMatch.sort(key=lambda x: x[tabla][indice])# Función Lambda,
                            # permite aplicar sort usando un indice en particular como pivote.
                            if (By.strip() == "DESC"): # Si pide desceniente basta con invertir la lista.
                                OutputMatch.reverse()






                # Código para mostrar solo las columnas pedidas en SELECT
                if(len(Tablas) == 1): # sin inner join
                    listaAux = OutputMatch.copy() # se iterara para ordenar los elementos
                    OutputMatch = [] # Guarda los elementos finales listos para imprimir
                    listaIndices = [] # guarda los indices de las columnas solicitaas
                    listaAux2 = [] # guarda una fila individual (ordenada) de la lista OutputMatch
                    for elemento in Select:
                        listaIndices.append(Select_dict[elemento][Tablas[0]])
                    for fila in listaAux:
                        listaAux2 = []
                        for indice in listaIndices:
                            listaAux2.append(fila[indice])
                        OutputMatch.append(listaAux2)

                    lens = []
                    for col in zip(*OutputMatch):
                        lens.append(max([len(v) for v in col]))
                    format = "     ".join(["{:<" + str(l) + "}" for l in lens])
                    print()
                    for row in OutputMatch:
                        print(format.format(*row))


                else: # Se usó inner join
                    # blend = [coluna1, columna2...], donde las columnas son las columnas que deben fusionarse en ambas tablas
                    indiceBlend = [] # lista de lista de tuplas, indiceBlend = [ [ (indice1, tabla1), (indice2, tabla2) ] , [ (indice3, tabla1), (indice4, tabla2) ] ]
                    # (indice1, tabla1) representa el indice que tiene el elemento 1 de blend en la tabla 1
                    for elemento in blend:
                        if elemento in archivos[Tablas[0]][0]:
                            i0 = archivos[Tablas[0]][0].index(elemento)
                        else:
                            i0 = -1
                        if elemento in archivos[Tablas[1]][0]:
                            i1 = archivos[Tablas[1]][0].index(elemento)
                        else:
                            i1 = -1
                        indiceBlend.append([(i0,0),(i1,1)])
                    BlendedOutput = []
                    listaIndices =[] # Misma mecánica que indiceBlend
                    for elemento in Select:
                        if elemento in archivos[Tablas[0]][0]:
                            i0 = archivos[Tablas[0]][0].index(elemento)
                        else:
                            i0 = -1
                        if elemento in archivos[Tablas[1]][0]:
                            i1 = archivos[Tablas[1]][0].index(elemento)
                        else:
                            i1 = -1
                        listaIndices.append([(i0,0),(i1,1)])

                    for fila in OutputMatch:
                        listaAux = []
                        for indices in listaIndices:
                            if (indices not in indiceBlend): # Si indices no esta en indice blend, no hay nada que diga que hay que mezclar
                                # las columnas, por lo que basta con agregarlas de manera contigua TODO en caso contrario,
                                # basta cambiar el segundo if por eli
                                if (indices[0][0] != -1):
                                    listaAux.append(fila[0][indices[0][0]])
                                elif (indices[1][0] != -1):
                                    listaAux.append(fila[1][indices[1][0]])
                            else: # indices in indiceBlend
                                # Si esta en indiceBlend hay que agregar una sola, ya que es la columna que mezcla las tablas
                                if (indices[0][0] != -1):
                                    listaAux.append(fila[0][indices[0][0]])
                                elif (indices[1][0] != -1):
                                    listaAux.append(fila[0][indices[1][0]])
                        BlendedOutput.append(listaAux)

                    lens = []
                    for col in zip(*BlendedOutput):
                        lens.append(max([len(v) for v in col]))
                    format = "     ".join(["{:<" + str(l) + "}" for l in lens])
                    print()
                    for row in BlendedOutput:
                        print(format.format(*row))
                    print()



                    #Cerrar por aca?
            else:
                print("La información solicitada no existe")


while(True):
    #recepcion de input

    print ("Ingrese su query:")
    statement = input()
    #condicion de salida de loop infinito
    if(statement == 'EXIT'):
        print()
        print('Se recibio comando de salida.Terminando la ejecucion.')
        print()
        break;
    #un diccionario con posibles llaves de expresiones completas
    SQL_REGEX = {
    'UPDATE_Key' : re.compile(r'^UPDATE\s+([^\s;,]+)\s+SET\s+((?:[^\s\.\'=*,;]+\s*=(?:\s*\'\s*[^\']+\s*\'|\s*-?\d+(?:\.\d+)?)(?:\s*,\s*[^\s\.\'=*,;]+\s*=(?:\s*\'\s*[^\']+\s*\'|\s*-?\d+(?:\.\d+)?))*))\s+WHERE\s+((?:[^\s\.\'=*,;]+\s*=(?:\s*\'\s*[^\']+\s*\'|\s*-?\d+(?:\.\d+)?)(?:\s*(?:AND|OR)\s*[^\s\.\'=*,;]+\s*=(?:\s*\'\s*[^\']+\s*\'|\s*-?\d+(?:\.\d+)?))*));{1}$'),
    'SELECT_Key' : re.compile(r'^SELECT\s+((?:\s*[^\s,;=\']+)(?:(?:\s*,\s*[^\s,*=;\']+)*))\s+FROM\s+([^\s;,]+)(?:(?:\s+INNER\sJOIN\s+([^\s;]+))?(?:(?:\s+WHERE\s+((?:[^\s.\'=*,;]+(?:.[^\s.\'=*,;]+)?\s*=(?:(?:\s*\'\s*[^\']+\s*\'|\s*-?\d+(?:.\d+)|\s*[^\s.\'=*;,]+(?:.[^\s.\'=*,;]+)?))(?:(?:\s+(?:AND|OR)\s+[^\s.\'=,;*]+(?:.[^\s.\'=,*;]+)?\s*=(?:(?:\s*\'\s*[^\']+\s*\'|\s*-?\d+(?:.\d+)|\s*[^\s.\'=,;*]+(?:\.[^\s.\'=;,*]+)?)))*)?)))))?(?:\s+ORDER\sBY\s+([^*\s=\';,]+)\s+(ASC|DESC))?;{1}$'),
    'INSERT_Key':re.compile(r'^INSERT\sINTO\s+([^\s,]+)\s+\(\s*((?:\s*[^\s,=*\';]+)(?:(?:\s*,\s*[^\s,=*\';]+\s*)*))\)\s+VALUES\s+\(((?:\s*\'[^\']+\s*\'\s*|\s*-?\d+|(?:\.\d+))(?:(?:,\s*\'\s*[^\']+\s*\'\s*|\s*,\s*-?\d+|(?:\.\d+)\s*)*))\);{1}$'),
    }
    #tupla key-match
    result_tuple = line_parser()
    #isinstance verifica que la llave no es null para no generar error de
    #noneType error.
    if isinstance(result_tuple,type(None)):
        #si la llave o match son None,no habia match. Es decir, fallo la sintaxis.
        print()
        print('Error de Sintaxis!')
        print()
        continue
    else:
        key = result_tuple[0];
        if key == 'UPDATE_Key':
            update(SQL_REGEX['UPDATE_Key'])
        elif key == 'SELECT_Key':
            select(SQL_REGEX['SELECT_Key'])
        elif key == 'INSERT_Key':
            insert(SQL_REGEX['INSERT_Key'])
