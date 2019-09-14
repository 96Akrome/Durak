CC = gcc
FLAGS = -g -Wall 

all: Tarea2
Tarea2: funciones.o lista.o
	$(CC) -o Tarea2 funciones.o lista.o

funciones.o: funciones.c funciones.h lista.h
	$(CC) $(FLAGS) -c funciones.c
lista.o: lista.c lista.h
	$(CC) $(FLAGS) -c lista.c
	
clean:
	rm  funciones.o lista.o 
