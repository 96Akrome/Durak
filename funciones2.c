#include "funciones.h"

struct lista* map(struct lista *a, struct dato (*f)(struct dato)){
    return a;
}

float sum(struct lista *a){
    float suma = 0;
    if (a->length == 0){return suma;}
    a -> actual = a -> head;
    struct dato disp;
    int pos;
    for (pos = 0; pos < a->length; pos++){
        disp = *at(a, pos);
        if(strcmp(disp.tipo, "l") != 0){
            if(strcmp(disp.tipo, "i") == 0){suma = suma + *(int *)disp.contenido;}
            else{suma = suma + *(float *)disp.contenido;}
        }
        else{
            suma = suma + sum((struct lista *) disp.contenido);
        }
    }
    return suma;
}

void print(struct lista *a){
    //para lista normal imprimira al funcionar algo como  {1, 2.5, 0, NULL}
    //para incrustadas algo como {1, 2, {9, 0.9, NULL}, 9.99, NULL}
    if (a->length == 0){
        printf("{}");
        return;
    }
    a -> actual = a -> head;
    struct dato disp;
    printf("{");
    int pos;
    for (pos = 0; pos < a->length; pos++){
        disp = *at(a, pos);
        if(strcmp(disp.tipo, "l") != 0){
            if(strcmp(disp.tipo, "i") == 0){printf("%d, ", *(int *)disp.contenido);}
            else{printf("%f, ", *(float *)disp.contenido);}
        }
        else{
            print((struct lista *) disp.contenido);
            printf(", ");
        }
    }
    printf("NULL}");
    return;
}

float average(struct lista *a){
    if (a->length == 0){return 0;}
    float suma = 0;
    int cantElem = a -> length;
    a -> actual = a -> head;
    struct dato disp;
    int pos;
    for (pos = 0; pos < a->length; pos++){
        disp = *at(a, pos);
        if(strcmp(disp.tipo, "l") != 0){
            if(strcmp(disp.tipo, "i") == 0){suma = suma + *(int *)disp.contenido;}
            else{suma = suma + *(float *)disp.contenido;}
        }
        else{
            suma = suma + average((struct lista *) disp.contenido);
        }
    }
    return suma/cantElem;
}



// Boorraaaaar.
struct nodo* getList(struct lista *a, int pos){
    int k;
    a->actual = a->head;
    for(k = 0; k < pos; k++){a->actual = a->actual->next;}
    return a->actual;
}