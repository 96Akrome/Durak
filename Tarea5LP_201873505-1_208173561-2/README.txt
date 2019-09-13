Integrantes		Rol               Paralelo
Anastasiia Fedorova	201873505-1        200
Ignacio Jorquera	201873561-2        200

El programa fue probado en las versiones 3.6.8 y 3.7.4 de python
Instrucciones para el funcionamiento del programa:

- Tener una de las versiones de python nombradas al inicio del documento, al utilizar otra no garantizamos su funcionamiento.
- Los archivos con extensión .csv deben estar en la misma carpeta que el programa con extensión .py .

- Especificaciones de expresiones regulares (regex):

-- El formato de las oraciones ingresadas por consola deben seguir el mismo formato de las oraciones explicadas en el pdf Tarea_1_Python, donde comienzan con una palabra reservada en específico (SELECT, INSERT INTO, UPDATE) y terminan con un punto y coma (;). Cualquier oración que no cumpla el formato específico descrito en el pdf (ingresar dos o más querys al mismo tiempo, ingresar menos (o más) palabras reservadas de las requeridas, ingresarlas en un orden distinto, entre otros) se traducirá en un error de sintaxis al no realizar match por parte de la expresión regular.

-- Si las palabras reservadas (INSERT INTO, VALUES, UPDATE, SET, WHERE, AND, OR, SELECT, FROM, INNER JOIN, ORDER BY, ASC, DESC) se escriben de una manera distinta a la señalada en el paréntesis (sin mayúsculas o con más de un espacio entre palabras en el caso de las que tienen más de dos palabras, como INSERT INTO o INNER JOIN o pegadas a alguna otra palabra (SELECTcolumna)) regex detectará error de sintaxis y será notificado por consola.

-- Si se incluye la palabra reservada "INNER JOIN" en una oración se deberá incluir la palabra reservada "WHERE" y sus respectivas condiciones, de lo contrario regex no realizará un match, lo que se traduce en un error de sintaxis por consola.

-- Tanto las columnas como las tablas no pueden tener los siguientes caracteres como parte de su nombre:
---   (espacio en blanco)
--- . (punto)
--- ' (comilla simple)
--- = (signo igual)
--- * (asterisco)
--- , (coma)
--- ; (punto y coma)
de lo contrario se detectará como error de sintaxis por parte del regex.


- Especificaciones de código:

-- Si una columna o tabla toma como valor una palabra reservada el programa imprimira por pantalla error de sintaxis, señalando los datos ingresados por el usuario que provocaron el error.

-- Si se incluye la palabra reservada "INNER JOIN" en una oración, las condiciones que siguen al "WHERE" deberan ser de la forma "tabla.columna" en el caso de referirse a una columna. De estas, al menos una debe ser obligatoriamente de la forma "tabla1.columna1 = tabla2.columna2", donde "tabla1" es distinto de "tabla2" y "columna1" es igual a "columna2". De lo contrario el programa imprimirá error de sintaxis por consola, esto último se debe a que el programa necesita saber con que columna debe mezclar las tablas, al no incluir esta condición pierde el sentido del "INNER JOIN" (en caso de encontrar innecesaria esta condición, se puede eliminar cambiando el (0) por un (-1) en el if de la linea 481 del programa con extensión .py, esta restricción nació de una respuesta en Moodle.).

-- Si se incluye la palabra reservada "INNER JOIN" en una oración y además se incluye la palabra reservada "ORDER BY", la columna que recibe la instrucción "ORDER BY" deberá ir acompañada con su respectiva tabla, siguiendo el mismo formato que "WHERE" al momento de incluir "INNER JOIN" (tabla.columna).
--
