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
(list) Una lista con strings que puede tener nombres de tablas, de columnas, etc.
——————–
Salida:
(int) Output: Se retorna un 0 o un 1 dependiendo del caso.
——————–
La función contiene un conjunto local reservedWords con las palabras reservadas.
Una vez recibida la lista compara los elementos de esta con los valores en el conjunto para ver
si la lista posee palabras reservadas como elementos. 
Si es asi, retorna un 0 (Caso de Error de Sintaxis). Si no, retorna 1.
"""
def reviseReservedWords(lista):
    reservedWords = {'INSERT','ASC','DESC','INTO','VALUES','SELECT','FROM','WHERE','ORDER BY','UPDATE','SET'}
    for string in lista:
        if string in reservedWords:
            return 0
    return 1

"""
checkColumns
——————–
Entradas:
(list) listaColumnasInput: lista con las columnas que ingreso el usuario en el query.
(list) listaColumnasArchivo: lista con las columnas que posee la tabla ingresada por el usuario en el query.
——————–
Salida:
(tuple) Output: Retorna una tupla con dos listas (listaPositiveMatch, listaNegativeMatch).
    (list) listaPositiveMatch: lista con las columnas ingresadas por el usuario que existen en la tabla.
    (list) listaNegativeMatch: lista con las columnas ingresadas por el usuario que no existen en la tabla.
——————–
La función guarda en una lista la intersección entre las columnas ingresadas por el usuario y las columnas existentes en la tabla.
Luego guarda en otra lista todas las columnas ingresadas que no pertenecen a la tabla.
"""
def checkColumns(listaColumnasInput, listaColumnasArchivo):
    listaPositiveMatch = [columna.strip() for columna in listaColumnasInput if columna in listaColumnasArchivo]
    listaNegativeMatch = [columna.strip() for columna in listaColumnasInput if columna not in listaColumnasArchivo]
    return (listaPositiveMatch, listaNegativeMatch)


"""
insert
——————–
Entradas:
(list) valid: lista con los grupos capturados por el match 
——————–
Salida: 
(void) No retorna
——————–
La función verifica que los valores ingresados cumplan las condiciones para poder así, finalmente, 
insertarlos en la tabla señalada por el usuario en el query.
"""
def insert(valid):
    # Descomprime los grupos ingresados, eliminano caracteres molestos al inicio y al final de cada valor.
    Tabla = valid[0].strip()

    #Ningun grupo capturado puede coincidir con palabras reservadas
    if (reviseReservedWords([Tabla]) == 0):
        print(); print('Error de Sintaxis !'); print()
        return 
    # Abre el archivo de la Tabla correspondiente en modo r+ (lectura + append).
    try:
        file = open(Tabla + ".csv", "r+", encoding='utf-8')
        Columnas = [name.strip() for name in re.split(r',', valid[1])]
        Values = [name.strip() for name in re.split(r',', valid[2])]

        # Si la cantidad de columnas es distinta a la cantidad de valores 
        # o si alguno de estos incluye palabras reservadas será error de sintaxis.
        if ((len(Columnas) != len(Values)) or (reviseReservedWords(Columnas) == 0)):
            print(); print("Error de Sintaxis !"); print()
            file.close()
            return
        
        # Lee la primera línea del archivo, elimina el salto de línea al final y separa el string
        # según las comas para obtener una lista con las Columnas del archivo.
        columnasFile = file.readline().strip().split(",")

        # Se reasigna la lista de columnas para que guarde solo las columnas ingresadas que existen en el archivo.
        # Adicionalmente se hace una variable que almacene las columnas ingresadas que no existen en el archivo.
        Columnas, colNotFound = checkColumns(Columnas, columnasFile)

        # Si se ingresan columnas que no existen en la tabla será error de sintaxis.
        if (len(colNotFound) != 0):
            print(); print("Error de Sintaxis !, las columnas "+ ", ".join(colNotFound) + " no pertenecen a la tabla."); print()
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
        print(); print("Se ha insertado 1 fila."); print()
        file.close()

    except FileNotFoundError:
        print(); print('Tabla indicada no existe. Intente de nuevo.'); print()
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
La función verifica que los valores ingresados cumplan las condiciones para poder así, finalmente, 
actualizar la tabla señalada por el usuario en el query con los valores ingresados.
"""
def update(valid):
    # Descomprime el nombre de la tabla ingresada.
    Tabla = valid[0].strip()
    
    #Ningun grupo capturado puede coincidir con palabras reservadas
    if (reviseReservedWords([Tabla]) == 0):
        print(); print('Error de Sintaxis 136!'); print()
        return 

    try:# Abre el archivo de la Tabla correspondiente en modo r+ (lectura + append).
        fileTable = open(Tabla + ".csv", "r+", encoding='utf-8')
        
        # Descomprime los cambios ingresados en SET, separándolos en una lista por comas (",") y después en otra por igual ("=").
        Set = [name.strip().split("=") for name in re.split(r',', valid[1])] 
        
        # Guarda las lineas del archivo en una lista de lista, donde cada lista interna es una fila.
        lineas = fileTable.readlines()
        cont = 0
        while(cont < len(lineas)):
            lineas[cont] = lineas[cont].strip().split(",")
            cont += 1
        fileTable.close()
            
        columnasFile = lineas[0] # Guarda las columnas que tiene la tabla.
        ColumnasSet = [Set[i][0].strip() for i in range(len(Set))] # Guarda las columnas que ingresó el usuario en SET.
        # Asigna una lista con las columnas que ingresó el usuario en SET que existen en la tabla
        # y una lista con las columnas que ingresó el usuario que no existen en la tabla.
        ColumnasSet , colNotFound = checkColumns(ColumnasSet ,columnasFile)
        
        # Si se ingresan columnas que no existen en la tabla o si las columnas en set incluyen 
        # palabras reservadas se imprimirá error de sintaxis y saldrá de la función
        if ((len(colNotFound) != 0) or (reviseReservedWords(ColumnasSet) == 0)):
            print(); print("Error de Sintaxis ! 163"); print()
            return
        
        # Descomprime las condiciones ingresadas en WHERE, separándolas por OR y luego por AND, manteniendo así la precedencia del segundo.
        Where = [name.strip().split("AND") for name in re.split(r'OR', valid[2])]

        # Separa las listas internas de WHERE haciendo split con el signo igual ("=") y revisa que la columna se encuentre en la tabla.
        # De no estar la columna en la tabla se imprimirá "Error de Sintaxis !" por consola.
        # Where quedará como se muestra en la siguiente línea:
        # Where = [[[columna1, cosa1]], [[columna2, cosa2], [columna3, cosa3]]], siendo los elementos en Where[i] las listas de condiciones
        # separadas por un OR, los elementos en Where[i][j] las condiciones separadas por un AND y los elementos en Where[i][j][k] 
        # las columnas con el valor que se desea buscar.
        i = 0
        while(i < len(Where)):
            j = 0

            while (j < len(Where[i])):
                col, value = Where[i][j].split("=")
                col = col.strip() # col puede ser de la forma Columna o de la forma Tabla.Columna
                value = value.strip().strip("'")
                Where[i][j] = [col, value]
                j = j + 1
            ColumnasWhere = [condicion[0] for condicion in Where[i]]
            # Asigna una lista con las columnas que ingresó el usuario en WHERE que existen en la tabla
            # y una lista con las columnas que ingresó el usuario que no existen en la tabla.
            ColumnasWhere , colNotFound = checkColumns(ColumnasWhere ,columnasFile)
            if((reviseReservedWords(ColumnasWhere) == 0) or (len(colNotFound) != 0)):
                print('Error de Sintaxis! (columnas de where)')
                return
            i = i + 1

        # # Diccionario donde valor = columnas de la tabla y llave = indice de la columna en la tabla
        # indices = { Columna : columnasFile.index(Columna) for Columna in columnasFile}
        # print(indices)

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
            print ("No se pudo actualizar la información con la información entregada.")
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
        print("Se ha actualizado " + str(len(indicesOutput)) + " fila")
        
        # UPDATE Notas SET Nota = -10 WHERE Nombre = 'ore ' OR Nombre = 'ore sama' OR Nombre = 'Clemente Aguilar'  AND Rol = '201773580-3' OR Rol = '201673557-4';

        return
    except FileNotFoundError:
        print(); print('Tabla indicada no existe. Intente de nuevo.'); print()
        return


# Main loop
while(True):
    #recepcion de input

    print ("Ingrese su query:")
    statement = input()
    #condicion de salida de loop infinito
    if(statement == 'EXIT'):
        print()
        print('Se recibió comando de salida.Terminando la ejecución.')
        print()
        break
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
        #si la llave o match son None,no había match. Es decir, fallo la sintaxis.
        print()
        print('Error de Sintaxis! 260')
        print()
        
    else:
        key = result_tuple[0]
        if key == 'UPDATE_Key':
            update(SQL_REGEX['UPDATE_Key'].match(statement).groups())
        elif key == 'SELECT_Key':
            print("lo")
            #select(SQL_REGEX['SELECT_Key'].match(statement).groups())
        elif key == 'INSERT_Key':
            insert(SQL_REGEX['INSERT_Key'].match(statement).groups())
