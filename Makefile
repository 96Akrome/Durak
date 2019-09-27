CC = gcc
FLAGS = -g -Wall 
OBJ = lista.o funciones.o

all: Tarea2
Tarea2: $(OBJ)
	$(CC) -o Tarea2 funciones.o

lista.o: lista.h lista.c 
	$(CC) $(FLAGS) -c lista.c
funciones.o: funciones.h funciones.c
	$(CC) $(FLAGS) -c funciones.c

clean:
	rm $(OBJ) Tarea2 
	
