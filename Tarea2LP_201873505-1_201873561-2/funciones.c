#include "lista.c"
#include "funciones.h"

//Se aplica una operacion *f a cada nodo de la lista y se retorna
//Un puntero a la lista nueva. Problema: init debe ser con **lista
//Si no, el usuario debe hacer malloc y free de su lista, y eso es estupido
//En espera de respuesta de pantuflin
struct lista* map(struct lista *a, struct dato (*f)(struct dato)){
    struct lista *b = (struct lista*)malloc(sizeof(struct lista));
    init(b);
    if(length(a) == 0){
        return b;
    }
    struct dato disp;
    struct dato aux;
    int pos;
    for(pos = 0; pos < length(a); pos++){
        disp = *at(a, pos);
        aux.tipo = disp.tipo;
        if(aux.tipo == 'l'){
            aux.contenido = (void*)malloc(sizeof(struct lista));
            *(struct lista*)aux.contenido = *map(disp.contenido, (*f));
        }
        if(aux.tipo == 'i'){
            aux.contenido = (void *)malloc(sizeof(int));
            *(int*)aux.contenido = *(int*)disp.contenido;
        }
        if(aux.tipo == 'f'){
            aux.contenido = (void *)malloc(sizeof(float));
            *(float*)aux.contenido = *(float*)disp.contenido;
        }
        append(b, (*f)(aux));
    }
    return b;
}

//Suma total de elementos de lista. En caso de lista vacia, retorna 0.
float sum(struct lista *a){
    float suma = 0;
    if (length(a) == 0){
        return suma;
    }
    struct dato disp;
    int pos;
    for(pos = 0; pos < length(a); pos++){
        //*at retorna puntero al elemento en posicion.
        disp = *at(a, pos);
        if(disp.tipo == 'l'){
            if(disp.tipo == 'i'){
                //dereferencia el (int*)
                suma += *(int*)disp.contenido;
            }
            else{
                //dereferencia el (float*)
                suma += *(float*)disp.contenido;
            }
        }
        else{
            //suma recursivamente
            suma += sum((struct lista*)disp.contenido);
        }
    }
    return suma;
}

void print(struct lista *a){
    //para lista normal imprimira al funcionar algo como  [1, 2.5, 0]
    //para incrustadas algo como [1, 2, [9, 0.9], 9.99]
    struct dato disp;
    printf("[");
    if (length(a) != 0){
        int pos;
        for (pos = 0; pos < length(a); pos++){
            //dereferencia el struct en posicion pos
            disp = *at(a, pos);
            if(disp.tipo == 'l'){
                if(disp.tipo == 'i'){
                    printf("%d, ", *(int*)disp.contenido);
                }
                else{
                    printf("%f, ", *(float*)disp.contenido);
                }
            }
            else{
                print((struct lista*)disp.contenido);
                printf(", ");
            }
        }
    }
    printf("]");
    return;
}

float average(struct lista *a){
    if (length(a) == 0){
        return 0;
    }
    float suma = 0;
    int cantElem = length(a);
    struct dato disp;
    int pos;
    for (pos = 0; pos < length(a); pos++){
        disp = *at(a, pos);
        if(disp.tipo == 'l'){
            if(disp.tipo == 'i'){
                suma += *(int*)disp.contenido;
            }
            else{
                suma += *(float*)disp.contenido;
            }
        }
        else{
            if(!length((struct lista*)disp.contenido)){
                //length es 0, no se considerara la lista vacia.
                cantElem--;
            }
            else{
                suma += average((struct lista*)disp.contenido);
            }
        }
    }
    return suma / cantElem;
}


void interface(struct lista *l){
    char tipo;
    int conf = 999;
    int pos;
    int func = 0;
    struct dato *display;
    struct dato data;
    while(conf != 0){
        printf("\nEl largo de la lista es %d\n\n", length(l));
        printf("Ingrese el número de la operacion que desea realizar:\n");
        printf("1: Insertar un elemento en una posición específica.\n2: Insertar un elemento al final de la lista.\n");
        printf("3: Remover un elemento en una posición específica.\n4: Obtener el dato de una posición en específico de la lista.\n");
        printf("5: Imprimir por pantalla la lista modificada por map.\n6: Obtener la suma de todos los elementos de la lista.\n");
        printf("7: Imprimir por pantalla la lista.\n8: Obtener el promedio de todos los elementos de la lista.\n");
        printf("9: Vaciar la lista.\n10: ingresar a una lista.\n");
        printf("0: Fin del programa.\n");
        scanf("%d", &conf);
        if((conf != 0) && (conf < 3)){
            printf("Ingrese el tipo de dato que desea agregar, i para entero, f para float y l para lista.\n");
            scanf("%c", &tipo);
            data.tipo = 'n';
            if(tipo != 'l'){
                if(tipo == 'i'){
                    data.contenido = (int*)malloc(sizeof(int));
                    data.contenido = (int*)data.contenido;
                    printf("Ingrese el int que desea agregar a la lista: ");
                    scanf("%d", (int*)data.contenido);
                }
                else if(tipo == 'f'){
                    data.contenido = (float*)malloc(sizeof(float));
                    printf("Ingrese el float que desea agregar a la lista: ");
                    scanf("%f", (float*)data.contenido);
                }
            }
            else{
                data.contenido = (struct lista*)malloc(sizeof(struct lista));
                init((struct lista*) data.contenido);
            }
            if(tipo == 'n'){
                printf("El tipo de dato ingresado no es válido.");
            }
            else{
                data.tipo = tipo;
                if (conf == 1){
                    printf("Ingrese la posición en donde desea insertar el nuevo elemento: ");
                    scanf("%d", &pos);
                    insert(l, pos, data);
                }
                else{
                    append(l, data);
                }
            }
        }
        else if (conf == 3){
            printf("Ingrese la posición en donde desea remover un elemento: ");
            scanf("%d", &pos);
            remov(l,pos);
            //remov2(l, pos);
        }
        else if (conf == 4){
            printf("Ingrese la posición del elemento que desea obtener: ");
            scanf("%d", &pos);
            display = at(l, pos);
            if(display == NULL){
                printf("La lista esta vacia. No se puede acceder a un elemento.\n");
                continue;
            }
            if(display->tipo != 'l'){
                if(display->tipo == 'i'){
                    printf("El elemento en la posición %d es un entero y su valor es: %d", pos, *(int*)display->contenido);
                }
                else{
                    printf("El elemento en la posición %d es un float y su valor es: %f", pos, *(float*)display->contenido);
                }
            }
            else{
                printf("El elemento en la posición %d es una lista y sus elementos son:\n", pos);
                print((struct lista*)display->contenido);
            }
        }
        else if (conf == 5){
            printf("aqui va el map");
        }
        else if (conf == 6){
            printf("La suma de todos los elementos de la lista (incluyendo los elementos de listas internas) es: %f", sum(l));
        }
        else if (conf == 7){
            printf("La lista contiene los siguientes elementos:\n");
            print(l);
        }
        else if (conf == 8){
            printf("El promedio de todos los elementos de la lista (incluyendo los elementos de listas internas) es: %f", average(l));
        }
        else if (conf == 9){
            clear(l);
        }
        else if (conf == 10){
            printf("Ingrese la posición de la lista a la que desea ingresar: ");
            scanf("%d", &pos);
            if(at(l, pos)->tipo == 'l'){
                interface(at(l, pos)->contenido);
            }
            else{
                printf("La posición elegida no contiene una lista.");
            }
        }
    }
}


int main(){
    struct lista *list = (struct lista*)malloc(sizeof(struct lista));
    init(list);
    interface(list);
    clear(list);
    free(list);
    return 0;
}
