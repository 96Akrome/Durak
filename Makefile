CC = gcc
FLAGS = -g -Wall 
OBJ = lista.o funciones.o

all: Tarea2
Tarea2: funciones.o lista.o
	$(CC) -o Tarea2 $(OBJ)

funciones.o: funciones.c funciones.h lista.h
	$(CC) $(FLAGS) -c funciones.c
lista.o: lista.c lista.h
	$(CC) $(FLAGS) -c lista.c
	
clean:
	rm $(OBJ) Tarea2
	
