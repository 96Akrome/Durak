import re
import collections

#parseador de statement,revisa si existe un match completo con regex o no.
def line_parser(statement):
    for key,rx in SQL_REGEX.items():
        match = rx.search(statement)
        if match:
            return key,match
        else:
            #sin ningun match
            None,None

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
    'INSERT_Key' : re.compile(r'INSERT +INTO(.+)\((.+)\) *VALUES *\((.+)\) *;'),
    }
    #tupla key-match
    result_tuple = line_parser(statement)
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
            #llamar a la funcion de insert
