#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lista.c"
#include "funciones2.c"

int main(){
    struct lista *listirijilla= (struct lista*)malloc(sizeof(struct lista));
    init(listirijilla);
    char tipo[1];
    int conf = 9;
    int pos;
    struct dato display;
    while(conf != 0){
        printf("\nEl largo de la lista es %d\n\n", length(listirijilla));
        printf("Ingrese el número de la operacion que desea realizar:\n");
        printf("1: Insertar un elemento en una posición específica.\n2: Insertar un elemento al final de la lista.\n");
        printf("3: Remover un elemento en una posición específica.\n4: Obtener el dato de una posición en específico de la lista.\n");
        printf("5: - Fuera de servicio -\n6: Obtener la suma de todos los elementos de la lista.\n");
        printf("7: Imprimir por pantalla la lista.\n8: Obtener el promedio de todos los elementos de la lista.\n");
        printf("9: Vaciar la lista.\n");
        printf("0: Fin del programa.\n");
        scanf("%d", &conf);
        if((conf != 0) && (conf < 3)){
            printf("Ingrese el tipo de dato que desea agregar, i para entero, f para float y l para lista.\n");
            scanf("%s", tipo);
            struct dato data;
            strcpy(data.tipo, "n");
            if(strcmp(tipo, "l") != 0){
                if(strcmp(tipo, "i") == 0){
                    data.contenido = (int *)malloc(sizeof(int));
                    data.contenido = (int *)data.contenido; 
                    printf("Ingrese el int que desea agregar a la lista: ");
                    scanf("%d", (int *)data.contenido);
                }
                else if(strcmp(tipo, "f") == 0){
                    data.contenido = (float *)malloc(sizeof(float));
                    printf("Ingrese el float que desea agregar a la lista: ");
                    scanf("%f", (float *)data.contenido);
                }
            }
            else{
                data.contenido = (struct lista*)malloc(sizeof(struct lista));
                init((struct lista *) data.contenido);
            }
            if(strcmp(tipo, "n") == 0){
                printf("El tipo de dato ingresado no es válido.");
            }
            else{
                strcpy(data.tipo, tipo);
                if (conf == 1){
                    printf("Ingrese la posición en donde desea insertar el nuevo elemento: ");
                    scanf("%d", &pos);
                    insert(listirijilla, pos, data);
                }
                else{
                    append(listirijilla, data);
                }
            }
        }
        else if (conf == 3){
            printf("Ingrese la posición en donde desea remover un elemento: ");
            scanf("%d", &pos);
            remov2(listirijilla, pos);
        }
        else if (conf == 4){
            printf("Ingrese la posición del elemento que desea obtener: ");
            scanf("%d", &pos);
            display = *at(listirijilla, pos);
            if(strcmp(display.tipo, "l") != 0){
                if(strcmp(display.tipo, "i") == 0){printf("El elemento en la posición %d es un entero y su valor es: %d", pos, *(int *)display.contenido);}
                else{printf("El elemento en la posición %d es un float y su valor es: %f", pos, *(float *)display.contenido);}
            }
            else{
                printf("El elemento en la posición %d es una lista y sus elementos son:\n", pos);
                print((struct lista *) display.contenido);
            }
        }
        else if (conf == 5){
            printf("\n\n---FUERA DE SERVICIO---\n");
            printf("Debiese ser el map, inserte map :v\n");
            printf("-----------------------");
        }
        else if (conf == 6){printf("La suma de todos los elementos de la lista (incluyendo los elementos de listas internas) es: %f", sum(listirijilla));}
        else if (conf == 7){
            printf("La lista contiene los siguientes elementos:\n");
            print(listirijilla);
        }
        else if (conf == 8){printf("El promedio de todos los elementos de la lista (incluyendo los elementos de listas internas) es: %f", average(listirijilla));}
        else if (conf == 9){clear(listirijilla);}
    }
    clear(listirijilla);
    free(listirijilla);
}