Integrantes		Rol               Paralelo
Anastasiia Fedorova	201873505-1        200
Ignacio Jorquera	201873561-2        200

=================================================================================
COMANDOS DE MAKEFILE:

make  - compila los archivos, creando un compilado Tarea2
make clean - borra los .o
(valgrind) ./Tarea2  - ejecuta el compilado Tarea2  (con valgrind opcional)
=================================================================================

El archivo funciones.c contiene el main, en el cual se asume que el usuario
hace el malloc de su lista base. (linea xx)

=================================================================================
INTERFAZ INTERACTIVA:

Ademas, en el main se invoca a la funcion opcional "interface", la cual, como lo
dice su nombre, es una interfaz, que permite facilmente hacer llamados a todas las funciones,
disponibles al usuario.

En caso de no quierer ocuparla, comentar la linea xx.

Una vez en ejecucion, al usuario se presentan las siguientes opciones :

Ingrese el número de la operacion que desea realizar:
-----------------------------------------------------
1: Insertar un elemento en una posición específica.
2: Remover un elemento en una posición específica.
3: Obtener el dato de una posición en específica de la lista.
4: Imprimir por pantalla la lista modificada por map.
5: Obtener la suma de todos los elementos de la lista.
6: Imprimir por pantalla la lista.
7: Obtener el promedio de todos los elementos de la lista.
8: Vaciar la lista.
9: Ingresar a una lista interna.
0: Salir de la lista actual (volver a la lista anterior/terminar).
-----------------------------------------------------
Ademas, con cada repeticion, se entrega la lista actual y su largo.

=================================================================================

INSTRUCCIONES PARA EL USO DE LA INTERFAZ:

=================================================================================
Opcion 1: permite insertar un elemento de tipo i,f o l. Una vez ingresada el character,
se pregunta donde se quiere insertar un dato y cual es su valor. Las listas se insertan,
por defecto, vacias. Si se ingresa algun char, distinto a i,f o l, se vuelve al loop.

Opcion 2: permite remover cualquier elemento en posicion valida, una vez que el usuario
ingrese la posicion por la consola.

Opcion 3:
