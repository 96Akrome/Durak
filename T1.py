import re


#parseador de statement,revisa si existe un match completo con regex o no.
def line_parser():
    for key,rx in SQL_REGEX.items():
        match = rx.search(statement)
        if match:
            return key,match
        else:
            #sin ningun match
            None,None


def insert(valid):
    # Descomprime los grupos ingresados, eliminano caracteres molestos al inicio y al final de cada valor.
    Tabla = [name.strip(" ' ’ ") for name in re.split(r',', valid.match(statement).groups()[0])]

    print("Nombre de tabla es: "+Tabla[0])
    
    # Abre el archivo de la Tabla correspondiente en modo r+ (lectura + append).
    try:
        file = open(Tabla[0] + ".csv", "r+", encoding='utf-8')
    except FileNotFoundError:
        print('Tabla indicada no existe. Intente de nuevo.')
        return

    Columnas = [name.strip(" ' ’ ") for name in re.split(r',', valid.match(statement).groups()[1])]
    Values = [name.strip(" ' ’ ") for name in re.split(r',', valid.match(statement).groups()[2])]

    print("\nTabla: ")
    print(Tabla)
    print("\nColumnas: ")
    print(Columnas)
    print("\nValues: ")
    print(Values)

    #unico caso de sintax invalida
    if (len(Columnas) != len(Values)):
        print("Error de syntax! La cantidad de valores no coincide con la cantidad de columnas")
        return

    inputs = dict()
    i = 0;
    while (i < len(Columnas)):
        inputs[Columnas[i]] =  Values[i]
        i = i + 1

    print("\nDiccionario:")
    print(inputs)

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
    print("Se ha insertado 1 fila.")
    file.close()

#corre infinitamente,anotar en readme que se puede salir, ingresando EXIT.
while(True):
    #recepcion de input
    print ("Ingrese su query: ")
    statement = input()
    #condicion de salida de loop infinito
    if(statement == 'EXIT'):
        print('Se recibio comando de salida.Terminando la ejecucion.')
        break;
    #un diccionario con posibles llaves de expresiones completas
    SQL_REGEX = {
    'UPDATE_Key' : re.compile(r'UPDATE( +.+)SET( +.+)WHERE( +.+);'),
    'SELECT_Key' : re.compile(r'SELECT(.+)FROM(.+(?=WHERE)|.+(?=ORDER BY)|.+)(?:WHERE(.+(?=ORDER BY)|.+))?(?:ORDER BY(.+))?;'),
    'INSERT_Key' : re.compile(r'INSERT +INTO(.+)\((.+)\) +VALUES +\((.+)\) *;'),
    }
    #tupla key-match
    result_tuple = line_parser()
    #isinstance verifica que la llave no es null para no generar error de
    #noneType error.
    if isinstance(result_tuple,type(None)):
        #si la llave o match son None,no habia match. Es decir, fallo la sintaxis.
        print('Error de sintaxis: No se reconoce el comando. Intente de nuevo.')
        continue
    else:
        key = result_tuple[0];
        if key == 'UPDATE_Key':
            print('La exp corresponde al update')
            #llamar a la funcion de update
        elif key == 'SELECT_Key':
            print('La exp corresponde al select')
            #llamar a la funcion de select
        elif key == 'INSERT_Key':
            print('La exp corresponde al insert')
            insert(SQL_REGEX['INSERT_Key'])
