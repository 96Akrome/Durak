Integrantes		Rol               Paralelo
Anastasiia Fedorova	201873505-1        200
Ignacio Jorquera	201873561-2        200

=================================================================================
COMANDOS DE MAKEFILE:

make  - compila los archivos, creando un compilado Tarea2
make clean - borra los .o
(valgrind) ./Tarea2  - ejecuta el compilado Tarea2  (con valgrind opcional)
=================================================================================

El archivo funciones.c contiene el main, en el cual se asume que la asignacion de memoria se realizara mediante malloc antes de inicializar la lista con la funcion init. (linea xx)

=================================================================================
INTERFAZ INTERACTIVA:

Ademas, en el main se invoca a la funcion opcional "interface", la cual, como lo
dice su nombre, es una interfaz, que permite facilmente hacer llamados a todas las funciones,
disponibles al usuario.

En caso de no querer ocuparla, comentar la linea XX.

Una vez en ejecucion, al usuario se presentan las siguientes opciones :

Ingrese el número de la operacion que desea realizar:
-----------------------------------------------------
1: Insertar un elemento en una posición específica.
2: Remover un elemento en una posición específica.
3: Obtener el dato de una posición en específico de la lista.
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
Opcion 1: permite insertar un elemento de tipo i,f o l. Una vez ingresada el caracter,
se pregunta cual es su valor (en caso de ser i o f) y en que posicion se quiere insertar el dato (la funcion append esta contenida dentro de esta opcion y sera llamada al elegir como posicion el largo de la lista). Las listas se insertan, por defecto, vacias. Si se ingresa algun char, distinto a i,f o l, se devuelve al loop.

Opcion 2: permite remover cualquier elemento en posicion valida, una vez que el usuario
ingrese la posicion por la consola.

Opcion 3: le pide una posicion al usuario para retornar el elemento (int, float o lista) que se encuentre en dicha posicion dentro de la lista.

Opcion 4: le pide al usuario ingresar el numero de la funcion que desea ingresar como parametro de map. A modo de prueba se incluyeron 2 funciones, la funcion 1 es triplicado (triplica el valor que almacena un struct dato) y la funcion 2 es halved (divide en 2 el valor que almacena un struct dato). Si desea agregar mas funciones basta con agregarlas al archivo funciones.c (antes de la funcion interface) y luego, hacer el llamado correspondiente en la linea (XX) de la interface siguiendo el siguiente esquema:

if(func == n){
   mapeada = map(l, (*IngreseSuFuncion));
}

Donde IngreseSuFuncion es el nombre de la funcion que desea llamar y n el numero que se le asignara, distinto a los ya asignados.

Opcion 5: llama a la funcion sum entregando la lista actual como parametro e imprime por consola el resultado de la suma de todos los elementos de la lista, incluyendo las listas internas. Si desea ingresar una lista interna como parametro de la funcion sum basta con ingresar a dicha lista con la Opcion 9 y luego elegir la Opcion 5.

Opcion 6: imprime todos los elementos de la lista ordenados por posicion como si se tratase de una lista de python, incluyendo todas las listas internas y sus respectivos elementos (aunque el programa lo hace de manera automatica con cada iteracion, por lo que esta opcion es un poco redundante).

Opcion 7: imprime por pantalla el promedio de todos los elementos de la lista segun las instrucciones dadas tanto en el pdf como en las consultas de moodle. Si hay listas sin elementos numericos (de la forma [] o [[]] o [[...[]...]] ) no se consideraran en el calculo del promedio. Si la lista en su totalidad no contiene elementos numericos imprimira por pantalla un mensaje señalando que no es posible realizar el calculo (debido a que el resultado de este sera NaN).

Opcion 8: reinicializa la lista, llama a la funcion clear y devuelve la lista a su estado inicial como una lista vacia (de la forma [] ) liberando la memoria utilizada por sus elementos.

Opcion 9: abre la interfaz con una de la listas internas de la lista principal, cuya posicion es pedida por consola. Es posible ingresar a listas internas de listas internas.

Opcion 0: sale del loop principal de la funcion de la interface, lo que provoca que, en caso de estar en una lista interna devuelve la interface a la lista que la contenia, en caso de estar en la lista principal sale de la funcion interface, volviendo al main, donde las siguientes lineas procederan a limpiar la lista (clear) y liberar la memoria que esta utilizaba (free), poniendole fin al programa.



=================================================================================
EJEMPLO:

1, i, 90, 0  			// crea un entero 90 en pos 0
1, f, 4.9 			// crea un float 4.9 en pos 1
1, l, 1 			// crea una lista en pos 1
9, 1 				// entra en una lista en pos 1
1, l, 0 		        // crea una lista vacia en pos 0 
1, l, 0  			// crea otra lista vacia en pos 0
2, 0 				// borra una lista en pos 0
1, f, 7, 0 			// crea un float en pos 0
0				 // sale a la lista principal
 
Lista final: [90, [7.000000,[]], 4.900000]

0 //termina la ejecucion





