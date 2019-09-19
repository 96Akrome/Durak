// void remov(struct lista *a, int i){
//     if((a->length == 0) | (i >= a->length) || (i < 0)){
//         printf("La lista es vacia o el indice esta out of bounds.\n");
//         return;
//     }
//     if((a -> length == 1) && (i == 0)){
//         clear(a);
//         return;
//     }
//     struct nodo *aux; // aux almacenará el nodo a remover.
//     a -> actual = a -> head; // iterador de la lista
    
//     if(i == 0){ // Al inicio de la lista
//         printf("Se requiere borrar el primer elemento de la lista no vacia.\n");
//         aux = a -> head;
//         a->head = a -> actual -> next; // Le asigno a head el puntero hacia el siguiente nodo.
//     }
//     else{
//         int k;
//         for(k = 0; k < i - 1; k++){a -> actual = a -> next;} // Itera hasta llegar a la posición (i - 1)
//         aux = a -> actual -> next; // Al salir del for, aux será el elemento a remover (posicion i)
//         if(i == a -> length-1){ // Al final de la lista
//             printf("Se requiere borrar el elemento en el final de la lista.\n");
//             a -> tail = a -> actual; 
//         }
//         else{ // Posición cualquiera de la lista
//             printf("Se requiere borrar el elemento en la posicion %d\n.",i );
//             a -> actual -> next = aux -> next; 
//         }
//     }
//     if(strcmp(aux -> info.tipo, 'l')){clear((struct lista*)aux);} // Si el nodo era una lista lo borra con la funcion clear
//     else{ // Si no, lo borra con free
//         free(aux -> info.contenido); // limpia el contenido
//         free(aux); // libera el nodo
//         } 
//     a->length--;
//     return;
// }