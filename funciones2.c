#include "funciones.h"

struct lista* map(struct lista *a, struct dato (*f)(struct dato)){
    return a;
}
float sum(struct lista *a){
    float suma = 0;
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
    float promedio = 0;
    return promedio;
}