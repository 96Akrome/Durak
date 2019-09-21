#include "funciones.h"

struct lista* map(struct lista *a, struct dato (*f)(struct dato)){
    struct lista *b = (struct lista*)malloc(sizeof(struct lista));
    init(b);
    if(length(a) == 0){return b;}
    struct dato disp;
    struct dato aux;
    int pos;
    for (pos = 0; pos < length(a); pos++){
        disp = *at(a, pos);
        strcpy(aux.tipo, disp.tipo);
        if(strcmp(aux.tipo, "l") == 0){
            aux.contenido = (void *)malloc(sizeof(struct lista));
            *(struct lista*)aux.contenido = *map(disp.contenido, (*f));
            }
        if(strcmp(aux.tipo, "i") == 0){
            aux.contenido = (void *)malloc(sizeof(int));
            *(int *)aux.contenido = *(int *)disp.contenido;
            }
        if(strcmp(aux.tipo, "f") == 0){
            aux.contenido = (void *)malloc(sizeof(float));
            *(float *)aux.contenido = *(float *)disp.contenido;
            }
        append(b, (*f)(aux));            
    }
    return b;
}

float sum(struct lista *a){
    float suma = 0;
    if (length(a) == 0){return suma;}
    struct dato disp;
    int pos;
    for (pos = 0; pos < length(a); pos++){
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
    if (length(a) == 0){
        printf("{NULL}");
        return;
    }
    struct dato disp;
    printf("{");
    int pos;
    for (pos = 0; pos < length(a); pos++){
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
    if (length(a) == 0){return 0;}
    float suma = 0;
    int cantElem = length(a);
    struct dato disp;
    int pos;
    for (pos = 0; pos < length(a); pos++){
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