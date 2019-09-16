#include <stdio.h>
#include <stdlib.h>
#include "funciones.h"
#include "lista.h"

int main(){
printf("Hello world\n");
return 0;
}


/*float sum
float sum = 0
-if a->leght == 0, return sum (lista vacia -> suma 0)

algoritmo:
  recorrer la lista usando un dummy (ver remov o dato *at)
  cada vez que nodo no sea lista, sumar al sum usando coercion de C
  si es una lista, la funcion debe ser recursiva, llamando a sum() con casteo (ver recursividad de tda)
*/

/*float average
- if a-> leght == 0 ; no se que cresta retornar (segun pdf no se considera para el calculo de promedio???)
- basicamente el mismo algoritmo de sum pero "se calcula promedio de listas internas aparte y el resultado es usado para el calculo de promedio total" (no cache como es, haria sumador y contador comun para todo, pantufla qlo)
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

/*map
mismo algoritmo de recorrido con dummy como en tda,pero aplicando el casteo para la nueva lista (usando init,insert con un pos de TDA). Retorna un puntero
*/
