#include <stdio.h>
#include <stdlib.h>
#include "lista.h"


void init(struct lista *a){
  a = (struct lista*)malloc(sizeof(struct lista));
  a->actual = NULL;
  a->head = NULL;
  a->length = 0;
  a->tail = NULL;
  return;
}

//hay que probar para listas incrustadas, deberia funcionar
//es recursiva siempre y cuando el tipo es 'l'
//uso a->actual en vez de nodo loop_aux porque igual despues se asigna como NULL
//en realidad es un nodo inutil en struct sjsjjsjsjs como no hay ni next ni prev
void clear(struct lista *a){
  while(a->head != NULL){
    a->actual = a->head;
    if(a->actual->info.tipo != 'l'){
      //no es un nodo que es a la vez cabeza de una lista
      a->head = a->head->next;
      //se libera el contenido de datos
      free(a->actual->info.contenido);
      //se libera el nodo
      free(a->actual);
    }
    else{
      //recursion
      clear((struct lista*)a->actual);
    }
  }
  a->length = 0;
  a->actual = NULL;
  a->tail = NULL;
  //a->head queda como NULL en el loop.
  return;
}

void append(struct lista *a, struct dato d){
 struct nodo *aux = (struct nodo*)malloc(sizeof(struct nodo));
 aux->info = d;
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

void insert(struct lista *a, int i, struct dato d){
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
    printf("No se puede insertar,indice out of bounds.\n");
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

void remov(struct lista *a, int i){
  if((a->length == 0) | (i >= a->length) || (i < 0)){
    printf("La lista es vacia o el indice esta out of bounds.\n");
    return;
  }
  struct nodo *aux;
  //al inicio de la lista
  if(i == 0){
    printf("Se requiere borrar el primer elemento de la lista no vacia.\n");
    //reasigno la cabeza, pero guardo el puntero a esta en aux.
    aux = a->head;
    a->head = aux->next;
    //cualquier tipo no recursivo (entero o flotante)
    if(a->head->info.tipo != 'l'){
      //limpio el contenido
      free(aux->info.contenido);
      //libero el nodo
      free(aux);
    }
    else{
      //tipo recursivo, lista incrustada (posiblemente con otras incrustadas)
      clear((struct lista*)aux);
      //no tenemos que hacer mas frees, dado que clear lo hara solo.
    }
    a->length--;
    return;
  }
  struct nodo *loop_aux;
  loop_aux = a->head;
  int k;
  //recorre hasta i-1 para poder borrar la cola
  for(k = 0; k < i-1; k++){
    loop_aux = loop_aux->next;
  }
  //eliminar al final (largo es siempre +1 nodo, es cantidad y no total de posiciones.)
  if(i == a->length-1){
    printf("Se requiere borrar al final de la lista.\n");
    aux = loop_aux->next;
    loop_aux->next = NULL;
    a->tail = loop_aux;
    if(aux->info.tipo != 'l'){
      free(aux);
    }
    else{
      clear((struct lista*)aux);
    }
    a->length--;
    return;
  }
  //eliminar dentro pero no el el extremo
  else{
    printf("Se requiere borrar en la posicion %d\n",i );
    aux = loop_aux->next;
    loop_aux->next = loop_aux->next->next;
    if(aux->info.tipo != 'l'){
      free(aux);
    }
    else{
      clear((struct lista*)aux);
    }
    a->length--;
    return;
  }
  return;
}

int length(struct lista *a){
  return a->length;
}


struct dato* at(struct lista *a, int i){
  if((a->length == 0) | (i >= a->length) || (i < 0)){
    printf("La lista esta vacia o el dato esta fuera de rango.\n");
  }
  //caso 1: nodo en la cabeza, retorna directamente
  if(i == 0){
    return &(a->head->info);
  }
  struct nodo *loop_aux;
  loop_aux = a->head;
  int k;
  //recorre hasta posicion i en la lista.
  for(k = 0; k < i; k++){
    loop_aux = loop_aux->next;
  }
  return &(loop_aux->info);
}
