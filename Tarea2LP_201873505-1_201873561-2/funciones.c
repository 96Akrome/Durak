#include "lista.c"
#include "funciones.h"

struct lista* map(struct lista *a, struct dato (*f)(struct dato)){
    struct lista *b = (struct lista*)malloc(sizeof(struct lista));
    struct lista *c;
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
            aux.contenido=(void*)malloc(sizeof(struct lista));
            c = map((struct lista*)disp.contenido, (*f));
            *(struct lista*)aux.contenido = *c;
            append(b, aux);
            free(c);
        }
        else{
            if(aux.tipo == 'i'){
                aux.contenido = (void *)malloc(sizeof(int));
                *(int*)aux.contenido = *(int*)disp.contenido;
            }
            else{ // if(aux.tipo=='f')
                aux.contenido = (void *)malloc(sizeof(float));
                *(float*)aux.contenido = *(float*)disp.contenido;
            }
            append(b, (*f)(aux));
        }
    }
    return b;
}

float sum(struct lista *a){
    float suma = 0;
    if (length(a) == 0){
        return suma;
    }
    struct dato disp;
    int pos;
    for(pos=0; pos < length(a); pos++){
        //*at retorna puntero al elemento en posicion.
        disp = *at(a, pos);
        if(disp.tipo == 'i'){
            //dereferencia el (int*)
            suma += *(int*)disp.contenido;
        }
        else if(disp.tipo == 'f'){
            //dereferencia el (float*)
            suma += *(float*)disp.contenido;
        }
        else{ // disp.tip == 'l'
            //suma recursivamente
            suma += sum((struct lista*)disp.contenido);
        }
    }
    return suma;
}

void print(struct lista *a){
    struct dato *disp;
    printf("[");
    if (length(a)!= 0){
        int pos;
        for (pos = 0; pos < length(a); pos++){
            //dereferencia el struct en posicion pos
            disp = at(a, pos);
            if(disp->tipo == 'i'){
                printf("%d", *(int*)disp->contenido);
            }
            else if(disp->tipo == 'f'){
                printf("%f", *(float*)disp->contenido);
            }
            else{ // disp->tipo=='l'
                print((struct lista*)disp->contenido);
            }
            if(length(a)!= 1 && pos != length(a) - 1){
                printf(", ");
            }
        }
    }
    printf("]");
    return;
}

float average(struct lista *a){
    float suma = 0;
    float internalSum = 0;
    int cantElem = length(a);
    struct dato disp;
    int pos;
    for (pos = 0; pos < length(a); pos++){
        disp = *at(a, pos);
        if(disp.tipo != 'l'){
            if(disp.tipo == 'i'){
                suma += *(int*)disp.contenido;
            }
            else{
                suma += *(float*)disp.contenido;
            }
        }
        else{
            internalSum = average((struct lista*)disp.contenido);
            if(internalSum!=internalSum){
                //Si se cumple la condicion es porque internalSum es +-NaN
                cantElem--;
            }
            else{
                suma += internalSum;
            }
        }
    }
    return suma / cantElem;
}

/*
struct dato triplicado
Recibe un dato de la lista, y retorna el triple de este. En caso de listas, retorna
la misma lista sin cambios. Es decir, que los cambios se aplican a tipos numericos.
================================================================================
Inputs:
- struct dato data - un struct de tipo dato, que se requiere cambiar.
================================================================================
Outputs:
- retorna el struct dato - un dato modificado.
*/
struct dato triplicado(struct dato data){
    if(data.tipo == 'i'){
        *(int *)data.contenido = *(int *)data.contenido * 3;
    }
    if(data.tipo == 'f'){
        *(float *)data.contenido = *(float *)data.contenido * 3;
    }
    return data;
}

/*
struct dato halved
Recibe un dato de la lista, y retorna la mitad de este. En caso de listas, retorna
la misma lista sin cambios. Es decir, que los cambios se aplican a tipos numericos.
================================================================================
Inputs:
- struct dato data - un struct de tipo dato, que se requiere cambiar.
================================================================================
Outputs:
- retorna el struct dato - un dato modificado.
*/
struct dato halved(struct dato data){
    if(data.tipo == 'i'){
        *(int *)data.contenido = *(int *)data.contenido / 2;
    }
    if(data.tipo == 'f'){
        *(float *)data.contenido = *(float *)data.contenido / 2;
    }
    return data;
}

/*
void interface
Interfaz interactiva para el mejor uso de las funciones.
Al usuario se prentan las 10 opciones posibles, donde este puede elegir una por consola.
Opcion 1 permite crear un elemento de tipo i,f o l y insertarlo en la lista base.
Opcion 2 permite borrar un elemento en posicion especifica.
Opcion 3 permite obtener un dato en posicion cualquiera.
Opcion 4 aplica map a la lista (con funciones de ejemplo halved o triplicado)
Opcion 5 imprime la suma de todos los elementos
Opcion 6 imprime la lista por pantalla
Opcion 7 invoca funcion average y imprime el promedio. En caso de lista vacia, se
imprime un error
Opcion 8 aplica clear a la lista (la vacia)
Opcion 9 permite entrar a cualquier lista interna de la lista base
Opcion 0 permite salir de la lista interna a la anterior o termina la ejecucion, si
el usuario se encuentra en la lista base.

Nota: README contiene las explicacion en mas detalle sobre el funcionamiento de la
interfaz.
================================================================================
Inputs:
- struct lista *l - un puntero a la lista base generica, inicializada en el main.
================================================================================
Outputs:
- tipo void, no tiene output.
*/
void interface(struct lista *l){
    int conf = 999;
    int pos;
    int func = 0;
    struct dato *display;
    struct dato data;
    struct lista *mapeada;
    while(conf != 0){
        printf("\n\nEl largo de la lista es %d\nLa lista actual es la siguiente:\n", length(l));
        print(l);
        printf("\nIngrese el número de la operacion que desea realizar:\n");
        printf("-----------------------------------------------------\n");
        printf("1: Insertar un elemento en una posición específica.\n");
        printf("2: Remover un elemento en una posición específica.\n3: Obtener el dato de una posición en específica de la lista.\n");
        printf("4: Imprimir por pantalla la lista modificada por map.\n5: Obtener la suma de todos los elementos de la lista.\n");
        printf("6: Imprimir por pantalla la lista.\n7: Obtener el promedio de todos los elementos de la lista.\n");
        printf("8: Vaciar la lista.\n9: Ingresar a una lista interna.\n");
        printf("0: Salir de la lista actual (volver a la lista anterior/terminar).\n");
        printf("-----------------------------------------------------\n");
        scanf("%d", &conf);
        if(conf == 1){
            printf("Ingrese el tipo de dato que desea ingresar (i de int, f de float, l de lista): ");
            scanf(" %c", &data.tipo);
            if(data.tipo == 'i'){
                data.contenido = (int*)malloc(sizeof(int));
                data.contenido = (int*)data.contenido;
                printf("Ingrese el int que desea agregar a la lista: ");
                scanf("%d", (int*)data.contenido);
            }
            else if(data.tipo == 'f'){
                data.contenido =(float*)malloc(sizeof(float));
                printf("Ingrese el float que desea agregar a la lista: ");
                scanf("%f", (float*)data.contenido);
            }
            else if(data.tipo == 'l'){
                data.contenido = (struct lista*)malloc(sizeof(struct lista));
                init((struct lista*)data.contenido);
            }
            else{
                printf("El tipo de dato no es valido.\n");
                continue;
            }
            printf("Ingrese la posicion en donde desea insertar el nuevo elemento: " );
            scanf("%d", &pos);
            insert(l, pos, data);
        }
        else if(conf == 2){
            printf("Ingrese la posicion en donde desea remover el elemento: ");
            scanf("%d", &pos);
            remov(l,pos);
        }
        else if(conf == 3){
            printf("Ingrese la posicion de elemento que desea obtener: ");
            scanf("%d", &pos);
            display = at(l, pos);
            if(display == NULL){
                continue;
            }
            if(display->tipo != 'l'){
                if(display->tipo == 'i'){
                    printf("El elemento en posicion %d es un entero y su valor es: %d\n", pos, *(int*)display->contenido);
                }
                else{
                    printf("El elemento en posicion %d es un flotante y su valor es: %f\n", pos, *(float*)display->contenido);
                }
            }
            else{
                printf("El elemento en posicion %d es una lista y sus elementos son: ",pos);
                print((struct lista*)display->contenido);
                printf("\n");
            }

        }
        else if (conf == 4){
            mapeada = NULL;
            printf("\n1-) Función triplicado.\n2-) Función halved.\nIngrese el número de la función que desea utilizar: ");
            scanf("%d", &func);
            if(func == 1){
                mapeada = map(l, (*triplicado));
            }
            if(func == 2){
                mapeada = map(l, (*halved));
            }
            if(mapeada != NULL){
                print(mapeada);
                clear(mapeada);
                free(mapeada);
            }
        }
        else if (conf == 5){
            printf("La suma de todos los elementos de la lista (incluyendo los elementos de listas internas) es: %f\n", sum(l));
        }
        else if (conf == 6){
            printf("La lista contiene los siguientes elementos:\n");
            print(l);
        }
        else if (conf == 7){
            float av = average(l);
            if(av != av){
                printf("La lista ingresada no contiene elementos numericos! No es posible calcular el promedio.\n");
            }
            else{
                printf("El promedio de todos los elementos de la lista (incluyendo los elementos de listas internas) es: %f\n", average(l));
            }
        }
        else if (conf == 8){
            clear(l);
            printf("La lista actual es:\n");
            print(l);
            printf("\n");
        }
        else if (conf == 9){
            printf("Ingrese la posicion de la lista a que quiere ingresar: ");
            scanf("%d", &pos);
            if(at(l, pos)->tipo == 'l'){
                interface(at(l, pos)->contenido);
            }
            else{
                printf("La posición elegida no contiene una lista.\n");
            }
        }

    }
}

int main(){
    struct lista *lista = (struct lista*)malloc(sizeof(struct lista));
    init(lista);

    //comentar en caso de no querer usar la interfaz
    interface(lista);

    clear(lista);
    free(lista);
    return 0;
}
