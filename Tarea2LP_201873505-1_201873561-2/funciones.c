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
    for (pos = 0; pos < length(a); pos++){
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
    for (pos = 0; pos < length(a); pos++){
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
    //para lista normal imprimira al funcionar algo como  {1, 2.5, 0, NULL}
    //para incrustadas algo como {1, 2, {9, 0.9, NULL}, 9.99, NULL}
    struct dato disp;
    printf("{");
    if (length(a) != 0){
      int pos;
      for (pos = 0; pos < length(a); pos++){
        //dereferencia el struct en posicion pos
        disp = *at(a, pos);
        if(disp.tipo == 'l'){
          if(disp.tipo == 'i')){
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
  printf("NULL}");
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
    return suma/cantElem;
}
