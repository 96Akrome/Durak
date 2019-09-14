#include <stdio.h>
#include "lista.h"


void init(struct lista *a){
  struct lista *a = (struct lista*)malloc(sizeof(struct lista));
  a->actual = NULL;
  a->head = NULL;
  a->length = 0;
  a->tail = NULL;
  return;
}

//no soporta listas incrustadas todavia.
//tiene que ser recursiva para ello.
void clear(struct lista *a){
  struct nodo *loop_aux_next;
  a->actual = a->head;
  while(a->head != NULL){
    loop_aux_next = a->head;
    a->head = a->head->next;
    free(loop_aux_next);
  }
  a->length = 0;
  a->actual = NULL;
  a->tail = NULL;
  return;
}

void append(struct lista *a,dato d){
 struct nodo *aux = (struct nodo*)malloc(sizeof(struct nodo));
 aux->info = item;
 aux->next = NULL;

 if (a->head ==  NULL){
   a->head =  aux;
   a->tail = aux;
   a->actual = aux;
 }
 else{
   a->tail->next = aux;
   a->tail = aux;
 }
 a->length++;
}

void insert(struct lista *a, int i, dato d){
  if (i == 0 && a->length == 0){
    printf("La lista es vacia. Llamando al append.\n");
    append(a,d);
    return;
  }
  if(i ==  a->length){
    printf("Se requiere insertar al final de la lista.\n");
    append(a,d);
    return;
  }
  if (i > a->length || i < 0){
    printf("No se puede insertar,indice out of bounds.\n")
    return;
  }
  struct nodo *aux = (struct nodo*)malloc(sizeof(struct nodo));
  aux->info = d;
  if(i == 0 && a->length != 0){
    printf("Se requiere insertar al inicio en lista no vacia.\n");
    aux->next = a->head;
    a->head = aux;
    a->length++;
  }
  else{
    printf("Se requiere insertar en posicion %d de la lista no vacia.\n",i);
    int k;
    struct nodo *loop_aux;
    loop_aux = a->head;
    for(k = 0; k < i-1; k++){
      loop_aux = loop_aux->next;
    }
    aux->next = loop_aux->next;
    loop_aux->next = aux;
    a->length++;
  }
  return;
}

void remove(struct lista *a, int i){
  if(a->length == 0 | i > a->length || i < 0){
    printf("La lista es vacio o el indice esta out of bounds.\n")
  }
  return;
}

int length(struct lista *a){
  return a->length;
}

dato* at(struct lista *a, int i){
  return;
}
