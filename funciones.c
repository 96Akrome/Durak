#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lista.h"
#include "funciones.h"

int main(){
printf("Hello world\n");
return 0;
}

struct lista* map(struct lista *a, struct dato (*f)(struct dato)){
  return a;
}
/*map
mismo algoritmo de recorrido con dummy como en tda,pero aplicando el casteo para la nueva lista (usando init,insert con un pos de TDA). Retorna un puntero
*/


float sum(struct lista *a){
  float sum = 0
}

// if a->length == 0, return sum (lista vacia -> suma 0)
if (a->length == 0){return sum;}

/*
algoritmo:
  recorrer la lista usando un dummy (ver remov o dato *at)
  cada vez que nodo no sea lista, sumar al sum usando coercion de C
  si es una lista, la funcion debe ser recursiva, llamando a sum() con casteo (ver recursividad de tda)
*/

/*float average
- if a-> leght == 0 ; no se que cresta retornar (segun pdf no se considera para el calculo de promedio???)
- recursiva
- al recorrer, si el nodo no es 'l' - sumar su valor casteado, si es 'l' , sumar += average(este nodo, casteado a lista) 
*/

/*
borrador de printeo recursivo, recordar que contenido es un puntero void
asi que hay que castearlo, tal cual no funcionara

para lista normal imprimira al funcionar algo como  {1 -> 2.5 -> 0 -> NULL}
para incrustadas algo como {1->2-> {9->0.9->NULL} -> 9.99 -> NULL}

void print(struct lista *a){
  if (a->length == 0){
    printf("{}\n");
    return;
  }
  struct nodo *aux;
  aux = a->head;
  printf("{");
  while (aux != NULL){
    if(aux->info.tipo == 'i'){
      printf("%d->",aux->info.contenido);
      aux = aux->next;
    }
    else if (aux->info.tipo == 'f'){
      print("%f->",aux->info.contenido)
    }
    else{
    //recursividad
    print((struct lista*)aux)
    }
  }
  printf("NULL}\n");
}
*/

