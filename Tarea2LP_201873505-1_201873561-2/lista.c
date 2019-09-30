#include "lista.h"
#include <stdio.h>
#include <stdlib.h>


void init(struct lista *a){
    a->actual = NULL;
    a->head = NULL;
    a->length = 0;
    a->tail = NULL;
    return;
}

void clear(struct lista *a){
    while(a->head != NULL){
        a->actual = a->head;
        a->head = a->head->next;
        if(a->actual->info.tipo == 'l'){
          clear((struct lista*)a->actual->info.contenido);
        }
        free(a->actual->info.contenido); // Se libera el contenido de datos
        free(a->actual); // Se libera el nodo
    }
    init(a);
    return;
}

void insert(struct lista *a, int i, struct dato d){
    if (i == 0 && length(a) == 0){
        //"La lista esta vacia. Llamando al append.
        append(a, d);
        return;
    }
    if(i == length(a)){
        //Se requiere insertar al final de la lista.
        append(a, d);
        return;
    }
    if (i > length(a) || i < 0){
        printf("No se puede insertar,indice out of bounds.\n");
        return;
    }
    struct nodo *aux = (struct nodo*)malloc(sizeof(struct nodo));
    aux->info = d;
    if(i == 0 && length(a) != 0){
        //Se requiere insertar al inicio en lista no vacia.
        aux->next = a->head;
        a->head = aux;
        a->length++;
    }
    else{
        //Se requiere insertar en posicion %d de la lista no vacia.
        int k;
        a->actual = a->head;
        for(k = 0; k < i-1; k++){
          a->actual = a->actual->next;
        }
        aux->next = a->actual->next;
        a->actual->next = aux;
        a->length++;
    }
    return;
}

void append(struct lista *a, struct dato d){
    struct nodo *aux = (struct nodo*)malloc(sizeof(struct nodo));
    aux->info = d;
    aux->next=NULL;
    if (length(a) == 0){
        a->head = aux;
        a->tail = aux;
        a->actual = aux;
    }
    else{
        a->tail->next = aux;
        a->tail = aux;
    }
    a->length++;
}

void remov(struct lista *a, int i){
    if((a->length == 0) | (i >= a->length) || (i < 0)){
        printf("La lista es vacia o el indice esta out of bounds.\n");
        return;
    }
    struct nodo *aux;
    //al inicio de la lista
    if(i == 0){
        //Se requiere borrar el primer elemento de la lista no vacia.
        aux = a->head;
        a->head = a->head->next;
        //cualquier tipo no recursivo (entero o flotante)
        printf("%c\n\n", aux->info.tipo);
        if(aux->info.tipo == 'l'){
            //tipo recursivo, lista incrustada (posiblemente con otras incrustadas)
            clear((struct lista*)aux->info.contenido);
        }
        //limpio el contenido
        free(aux->info.contenido);
        //libero el nodo
        free(aux);
        a->length--;
        return;
    }
    struct nodo *loop_aux;
    loop_aux = a->head;
    int k;
    //recorre hasta i-1 para poder borrar la cola
    for(k = 0; k < i - 1; k++){
      loop_aux = loop_aux->next;
    }
    //Largo es siempre +1 nodo, es cantidad y no total de posiciones.)
    if(i == a->length - 1){
        //Se requiere borrar al final de la lista.
        aux = loop_aux->next;
        loop_aux->next = NULL;
        a->tail = loop_aux;
        if(aux->info.tipo == 'l'){
            clear((struct lista*)aux->info.contenido);
        }
        free(aux->info.contenido);
        free(aux);
        a->length--;
        return;
    }
    //eliminar dentro pero no el del extremo
    else{
        //Se requiere borrar en la posicion especifica
        aux=loop_aux->next;
        loop_aux->next = loop_aux->next->next;
        if(aux->info.tipo == 'l'){
            clear((struct lista*)aux->info.contenido);
        }
        free(aux->info.contenido);
        free(aux);
        a->length--;
        return;
    }
    return;
}

int length(struct lista *a){
    return a->length;
}

struct dato* at(struct lista *a, int i){
    if((length(a) == 0) | (i >= length(a)) || (i < 0)){
        //caso base: falla
        printf("La lista esta vacia o el dato esta fuera de rango.\n");
        struct dato *fail = NULL;
        return fail;
    }
    //caso 1: nodo en la cabeza, retorna directamente
    if(i == 0){
        return &(a->head->info);
    }
    a->actual = a->head;
        int k;
    //recorre hasta posicion i en la lista.
    for(k = 0; k < i; k++){
        a->actual = a->actual->next;
    }
    return &(a->actual->info);
}

/*
char getTipo
Recibe un dato de la lista, y retorna el tipo de este.
================================================================================
Inputs:
- struct dato data - un struct de tipo dato.
================================================================================
Outputs:
- char - el tipo de dato, guardado en su campo de struct.
*/
char getTipo(struct dato dato){
    return dato.tipo;
}

/*
struct dato getContenido
Recibe un dato de la lista, y retorna su contenido, guardado en el campo "contenido".
================================================================================
Inputs:
- struct dato data - un struct de tipo dato, que se requiere cambiar.
================================================================================
Outputs:
- puntero void* al contenido de dato
*/
void* getContenido(struct dato dato){
    return dato.contenido;
}

/*
struct dato makeDato
Crea un struct dato con la informacion, que ingresa el usuario.
================================================================================
Inputs:
- void *contenido - puntero void al contenido, que debe tener el dato
- char tipo - el tipo, asignado al dato a crear
================================================================================
Outputs:
- struct dato makeDato
*/
struct dato makeDato(void* contenido, char tipo){
    struct dato dato;
    dato.tipo = tipo;
    if(tipo == 'l'){
        dato.contenido = (struct lista*)malloc(sizeof(struct lista));
        *(struct lista*)dato.contenido = *(struct lista*)contenido;
    }
    else if(tipo == 'i'){
        dato.contenido = (int*)malloc(sizeof(int));
        *(int*)dato.contenido = *(int*)contenido;
    }
    else if(tipo == 'f'){
        dato.contenido = (float*)malloc(sizeof(float));
        *(float*)dato.contenido = *(float*)contenido;
    }
    return dato;
}
