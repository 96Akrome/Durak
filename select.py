import re

select_Regex = r" *SELECT +(.+?) +FROM +(.+?)(?: +INNER JOIN +(.+?))?(?: +WHERE +(.+?))?(?: +ORDER BY +(.+?) (ASC|DESC))?;"

valid = re.compile(select_Regex)

# Recepción de input
print ("Ingrese SELECT: ")
statement = "SELECT * FROM Estudiantes INNER JOIN Notas WHERE Estudiantes.Rol = Notas.Rol AND Estudiantes.Nombre = 'Clemente Aguilar' AND Notas.Rol = '201773580-3' OR Notas.Nota = 80 AND Estudiantes.Nombre = 'Gonzalo Fernandez' ORDER BY Nota ASC;"

# Validación de syntax en el input
if(valid.match(statement) == None):
    print("invalid syntax")

else:
    Tablas = [] # [ tabla 1, tabla 2], Tablas puede tener largo 1 o 2, dependiendo si se incluye INNER JOIN
    # Descomprime los grupos ingresados, eliminano caracteres molestos al inicio y al final de cada valor.
    Select = [name.strip() for name in re.split(r',', valid.match(statement).groups()[0])] # [[Columna1] , [columna2]]
    Tablas.append(valid.match(statement).groups()[1].strip()) # Tablas = [tabla 1], agrega la primera tabla a Tablas
    Where = [name.split("AND") for name in re.split(r'OR', valid.match(statement).groups()[3])] # [[cond11 = value11 , cond12 = value12], [cond21 = val21]] [[And, And] OR [And]], OR = ","
    if(valid.match(statement).groups()[4] != None ): # Pregunta si se incluye el comando ORDER BY
        Order = valid.match(statement).groups()[4].strip() # Columna que se quiere usar para ordenar los datos mostrados en pantalla
        By = valid.match(statement).groups()[5].strip() # ASC | DESC
    else:
        Order = By = "" # Se dejan como strings vacíos para futuras consultas TODO puede cambiar en el futuro
    if(valid.match(statement).groups()[2] != None): # Pregunta si se incluye el comando INNER JOIN
        Tablas.append(valid.match(statement).groups()[2].strip().strip("'")) # Tablas = [tabla 1, tabla 2], agrega tabla 2 a Tablas

    print("Select:\n",Select,"\nFrom:\n",Tablas[0],"\nInner Join:\n",Tablas[-1],"\nWhere:\n",Where,"\nOrder By", Order, By)

    archivos = dict()
    i = 0
    archivosNoExistentes = []
    # Lee el o los archivos, dependiendo del largo de Tablas y almacena sus contenidos en el diccionario archivos
    while (i < len(Tablas)):
        # Test para ver si existen los archivos ingresados como nombres de tablas
        FileExists = 0
        try:
            f = open(Tablas[i] + ".csv", "r", encoding='utf-8')
            f.close()
        except FileNotFoundError:
            FileExists = 1
        if (FileExists != 1):
            File = open(Tablas[i] + ".csv", "r", encoding='utf-8')
            lineas = File.readlines()
            cont = 0
            while(cont < len(lineas)):
                lineas[cont] = lineas[cont].strip().split(",")
                cont = cont + 1
            File.close()
            archivos[Tablas[i]] = lineas

        else:
            archivosNoExistentes.append(Tablas[i] + ".csv")
        i = i + 1
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

    if(len(archivosNoExistentes) > 0): # Caso de error por inexistencia de archivos
        print ("No existe/n el/los archivo/s " + ", ".join(archivosNoExistentes))
    else:
        # Select2 es una lista que contiene la union de las columnas de ambos archivos
        i = 0
        Select2 = []
        while(i < len(Tablas)):
            for colu in archivos[Tablas[i]][0]:
                if (colu not in Select):
                    Select.append(colu)
            i = i + 1
        # Si el usuario ingreso SELECT *, se asignarán todas las columnas de los archivos en el orden que estos tengan, sin repetir elementos.
        if(len(Select) == 1 and Select[0] == '*'):
            Select = Select2
        # Separa las condiciones planteadas en WHERE haciendo un split en el caracter '='
        i = 0
        
        while(i < len(Where)):
            j = 0
            while (j < len(Where[i])):
                col, value = Where[i][j].split("=")
                col = col.strip() # col puede ser de la forma Columna o de la forma Tabla.Columna

                value = value.strip()
                Where[i][j] = [col, value]
                j = j + 1

            i = i + 1
        indiceOutput = 0
        # Finalmente, si las condiciones tienen la forma: columna1 = cosa1 OR columna2 = cosa2 AND columna3 = cosa3
        # Where quedará como se muestra en la siguiente línea:
        # Where = [[[columna1, cosa1]], [[columna2, cosa2], [columna3, cosa3]]], quedando los datos unidos por un AND en una misma lista
        # reemplazando columna1, 2 o 3 por Tabla.columna1, 2 o 3 según corresponda.

        columnasRepetidas = list() # lista que almacena las columnas repetidas ingresadas por el usuario
        Select_dict = dict() # diccionario que tiene como llave una columna y como valor otro diccionario.

        for columna in Select:
            if (columna in Select_dict.keys()): # Si la columna ya era llave del diccionario se agrega a la lista de columnas repetidas y gatilla un error.
                columnasRepetidas.append(columna)
            else:
                Select_dict[columna] = dict() # diccionario cuya llave es una tabla y su valor es el indice en donde se encuentra la columna en dicha tabla
                # Empieza a obtener los indices realizando comparaciones con el o los archivos.
                for archivo in archivos.keys():
                    if (columna in archivos[archivo][0]): # archivo[0] corresponde a la primera linea del archivo csv (almacena el nombre de sus columnas)
                        Select_dict[columna][archivo] = archivos[archivo][0].index(columna) 
                        indiceOutput = indiceOutput + 1 # cuentas las columnas ingresadas con SELECT que efectivamente existen en uno o más archivos
                        
                    else:
                        Select_dict[columna][archivo] = -1

        print("\n\n Select_dict \n\n",Select_dict)

        if(indiceOutput == 0 or len(columnasRepetidas) > 0 or Order not in Select): # Casos de error.
            if (indiceOutput == 0): # Verifica si no existe ninguna columna de las que se desea mostrar.
                print("No existen las columnas solicitadas en la tabla " + " ni en la tabla ".join(Tablas) + ".")
            elif (Order not in Select):
                print("La columna en la que desea utilizar la expresión SORT BY no existe dentro de las columnas ingresadas en SELECT.")
            else: # Se ingresaron columnas repetidas y explota.
                print("Error de sintaxis !, las siguientes columnas estan repetidas en el input: " + ", ".join(list(set(columnasRepetidas))) + ".")
        
        else:
            # Se asume que el programa debe imprimir los datos de las columnas ingresadas que existan en alguno de los archivos.
            # Imprime en pantalla las columnas solicitadas que no existen en ningun archivo.
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
            
            
            # Empieza la magia.
            cont = 0
            while(cont < len(Where)): # la cantidad de iteraciones depende de la cantidad de OR en el input
                matchColumnas = 0 # Representa la cantidad de columnas en Where que coinciden con las existentes en los archivos             
                outputPrint = [] # Almacena las filas que se mostrarán en pantalla
                cont2 = 0
                print("\n\nLinea 148 where[cont]", Where[cont])
                # Búsqueda de columnas
                while (cont2 < len(Where[cont])): # la cantidad de iteraciones depende de la cantidad de AND en el input separados por un OR
                    print("Where[cont][cont2] = ", Where[cont][cont2])
                    tabCol = Where[cont][cont2][0]
                    value = Where[cont][cont2][1]
                    if(len(Tablas) > 1): # En el caso de haber incluido INNER JOIN en el input
                        tabCol = tabCol.split(".") # tabla.columna -> [tabla, columna]
                        if(len(tabCol) > 1): # si no es > 1 quiere decir que no se ingresó como corresponde (ej: columna en vez de tabla.columna)
                            # tabla1 y columna1 son los valores de tabla.columna por separados.
                            tabla1 = tabCol[0].strip()
                            columna1 = tabCol[1].strip()
                            if(columna1 in archivos[tabla1][0]):
                                indice1 = archivos[tabla1][0].index(columna1) # Posición de la columna a comparar en la tabla ingresada
                                if(value[0] != "'" and not value.isnumeric()): # Si no comienza con ' no es un string, si no comienza con un digito no es número
                                    # por lo que value pasaría a ser una columna.
                                    value = value.split(".") # misma forma que tabCol.split(".")
                                    if(len(value) > 1): # mismo caso de tabCol
                                        if(value[1].strip() in archivos[value[0].strip()][0]):
                                            matchColumnas = matchColumnas + 1 # Suma 1 al contador de columnas
                                            # Caso 1: 2 tablas, Columna = Columna
                                            # tabla2 y columna2 son los valores de tabla.columna ingresados en value
                                            print("caso 1:")
                                            tabla2 = value[0].strip()
                                            columna2 = value[1].strip()
                                            indice2 = archivos[tabla2][0].index(columna2) # Posición de la columna a comparar en la tabla ingresada

                                            fila1 = 1 # Iterador de la tabla que contiene a indice1, parte desde 1 para omitir la fila con nombres de columnas
                                            while (fila1 < len(archivos[tabla1])):
                                                fila2 = 1
                                                while(fila2 < len(archivos[tabla2])):
                                                    Output = [] # auxiliar para la lista outputPrint
                                                    if(archivos[tabla1][fila1][indice1] == archivos[tabla2][fila2][indice2]): # si columna de tabla 1 = columna de tabla 2
                                                        print("\nIF\n", )
                                                        # si el valor en fila1 de tabla1.columna1 es igual al valor en fila2 de tabla2.columna2
                                                        for columnas in Select: # Columnas en Select son las que el usuario ingreso para imprimir en pantalla
                                                            # Obtiene el valor de la columna
                                                            if (Select_dict[columnas][tabla1] != -1):
                                                                Output.append(archivos[tabla1][fila1][Select_dict[columnas][tabla1]])
                                                            elif (Select_dict[columnas][tabla2] != -1):
                                                                Output.append(archivos[tabla2][fila2][Select_dict[columnas][tabla2]])
                                                                       
                                                    if(len(Output) > 0): # Si Output no esta vacio, agrega dicha lista en outputPrint, que contiene los datos a imprimir en pantalla
                                                        if(Output not in outputPrint):
                                                            outputPrint.append(Output)

                                                    fila2 = fila2 + 1
                                                fila1 = fila1 + 1

                                # Caso 2: 2 tablas, Columna = Valor
                                else: # value comienza con ' o con un digito, por lo que es un string o un numero y se trabaja como valor.
                                    matchColumnas = matchColumnas + 1 # Suma 1 al contador de columnas
                                    print("Caso 2")
                                    # Mismo procedimiento que en caso 1, usando el formato columna = valor
                                    fila1 = 1 # Iterador de la tabla que contiene a indice1, parte desde 1 para omitir la fila con nombres de columnas
                                    while (fila1 < len(archivos[tabla1])):
                                        Output = [] # lista que guardara la fila que coincida con la condición señalada
                                        if(archivos[tabla1][fila1][indice1] == value.strip("'")):
                                            # si el valor en fila1 de tabla1.columna1 es igual al valor en fila2 de tabla2.columna2
                                            for columnas in Select:
                                                for keys in Select_dict[columnas].keys():
                                                    if(Select_dict[columnas][keys] != -1):
                                                        # Agrega los atos a la lista Output
                                                        row = fila1
                                                        if(archivos[keys][row][Select_dict[columnas][keys]] not in Output):
                                                            Output.append(archivos[keys][row][Select_dict[columnas][keys]])
                                                        # No creo que eliminar los clonados este mal, de lo contrario, borrar el if que esta sobre este comentario
                                                        # y quitar el comentario de la linea que esta abajo de este comentario.
                                                        #Output.append(archivos[keys][row][Select_dict[columnas][keys]])
                                                                       
                                            if(len(Output) > 0): # Si Output no esta vacio, agrega dicha lista en outputPrint, que contiene los datos a imprimir en pantalla
                                                if(Output not in outputPrint):
                                                    outputPrint.append(Output)     
                                            
                                        fila1 = fila1 + 1                                                                    

                    else: # len(Tablas) == 1
                        if(Where[cont][cont2][0].strip() in archivos[Tablas[0]][0]): # Si la columna ingresada en WHERE existe en la tabla
                            if(value[0] != "'" and not value[0].isdigit()): # si value es una columna.
                                matchColumnas = matchColumnas + 1 # Suma 1 al contador de columnas
                                # Caso 3: 1 tabla, Columna = Columna
                            else: # value es un string o un numero
                                matchColumnas = matchColumnas + 1 # Suma 1 al contador de columnas
                                # Caso 4: 1 tabla, Columna = Valor
                    
                    cont2 = cont2 + 1
                for lista in outputPrint:
                    print(lista)
                # Verifica cuantas de las columnas ingresadas en WHERE existen dentro del archivo.
                # Si existen X columnas = len(Where[cont]) (lista con las condiciones concatenadas con un AND) quiere decir
                # que el conjunto de condiciones puede pasar a la fase 2: búsqueda de fila.
                if (matchColumnas > 0 and matchColumnas == len(Where[cont]) and len(outputPrint) == len(Where[cont])):
                    print("whoooosh")
                    
                cont = cont + 1  
            
