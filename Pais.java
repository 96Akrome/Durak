import java.util.ArrayList;
import java.util.Collections;

import java.util.*; 
import java.lang.*; 
import java.io.*; 


class Pais implements Grafo{
    ArrayList<Node> nodesList; // lista de nodos, cada una de cuales es CIUDAD.
    //lista de ciudades es necesaria porque Pais a Ciudad tiene * (relacion One-To-Many)
    int[][] adjMatrix;
    int nNodes;
    int nEdges;
    static final int INF = 9999999;
    Empresa empresa;

    /** (Pais)
    (int)   (nNodes)    -> Número de ciudades/nodos/vertices que tendrá el país.
    (int)   (nEdges)    -> Número de caminos/arcos que tendrá el país.
    --------------------
    Constructor del grafo Pais. Inicializa todo sus valores según la cantidad de nodos y aristas.
    --------------------
    */
    public Pais(int nNodes,int nEdges){
        System.out.println("Se ha creado un nuevo pais!");
        this.nNodes = nNodes;
        this.nEdges = nEdges;
        nodesList = new ArrayList<Node>();
        for (int n = 0; n < nNodes; n++){
            nodesList.add(new Node(n, new Ciudad(0, 0)));
        }
        this.adjMatrix = new int[nNodes][nNodes];
        //inicializo todas las distancias como INF
        for (int i = 0; i < adjMatrix.length; i++) {
            for (int j = 0; j < adjMatrix[i].length; j++) {
                if(i == j){ // Modifique aqui, agregue el = 0
                    adjMatrix[i][j] =  0;
                }
                else{
                    adjMatrix[i][j] =  INF;
                }
            }
        }
    }

    /** (getnVertex)
    No recibe parámetros
    --------------------
    Retorna el número de nodos/vertices del grafo.
    --------------------
    */
    public int getnVertex(){
        return nNodes;
    }
    
    /** (getnEdges)
    No recibe parámetros
    --------------------
    Retorna el número de arcos del grafo.
    --------------------
    */
    public int getnEdges(){
        return nEdges;
    }

    /** (addNode)
    (int)       (id)        -> nodo u
    (Ciudad)    (ciudad)    -> ciudad con identificador u
    --------------------
    Agrega a la lista de Nodos un Nodo que almacena la información de ciudad, cuyo identificador es u.
    --------------------
    */
    public void addNode(int id, Ciudad ciudad){
        nodesList.set(id, (new Node(id,ciudad)));
    }

    /** (addEdge)
    (int)   (u) -> nodo u
    (int)   (v) -> nodo v
    (int)   (w) -> peso w
    --------------------
    Agrega un arco con peso w, uniendo el nodo u con el nodo v
    --------------------
    */
    public void addEdge(int u,int v, int w){
        adjMatrix[u][v] = w;
        adjMatrix[v][u] = w;
        System.out.println("Se ha agregado el arco: " + u + " -> " + v + " con peso " + w);
    }

    /** (edgeWeight)
    (int)   (u) -> nodo u
    (int)   (v) -> nodo v
    --------------------
    Retorna el peso del arco formado por el nodo u y el nodo v
    --------------------
    */
    public float edgeWeight(int u, int v){
        System.out.println("El peso del arco" + u + " " + v + "es: " + adjMatrix[u][v]);
        return adjMatrix[u][v];
    }

    /** (printAdjMatrix)
    No recibe parámetros
    --------------------
    Imprime por pantalla la matriz de adyacencia del grafo país según los datos ingresados en los archivos de texto.
    --------------------
    */
    public void printAdjMatrix(){
        System.out.println("\nLa matriz de adyacencia del grafo es: ");
        for (int i = 0; i < adjMatrix.length; i++) {
            for (int j = 0; j < adjMatrix[i].length; j++) {
                if(adjMatrix[i][j] == INF){
                    System.out.printf("%12s", "---");
                }
                else{
                    System.out.printf("%12d", adjMatrix[i][j]);
                }
            }
            System.out.println("\n");
        }
    }


    /** (setEmpresa)
    (Empresa)   (empresa)   -> empresa que se le asignara al país
    --------------------
    Asigna la empresa correspondiente al país.
    --------------------
    */
    public void setEmpresa(Empresa empresa){
        this.empresa = empresa;
    }

    // floyd warshall para obtener el óptimo
    /** (printOptimo)
    No recibe parámetros
    --------------------
    El método printOptimo utiliza el algoritmo Floyd-Warshall para obtener todas las utilidades generadas al utilizar todas las ciudades como base.
    Luego busca entre todas las utilidades obtenidas la que sea mayor (puede ser una o varias con el mismo valor) y las muestra por pantalla
    junto a los vehículos utilizados y las utilidades individuales generadas en el camino a partir de la ciudad seleccionada. 
    --------------------
    */
    public void printOptimo(){
        int V = this.nNodes; // numero de nodos (se podria cambiar por el get, pero al ser de la misma clase como que meh)
        int floydMatrix[][] = new int[V][V]; // array con las distancias minimas
        int i, j, k;

        // Se inicializa la matriz de distancia mas corta con los valores de la matriz de adyacencia
        for(i = 0; i < V; i++) {
            for(j = 0; j < V; j++) {
                floydMatrix[i][j] = this.adjMatrix[i][j]; 
            }
        }

        // Se revisan los caminos con largo > 1 (con vertices intermedios)
        for(k = 0; k < V; k++) { 
            for(i = 0; i < V; i++) {
                for(j = 0; j < V; j++) { 
                    // Si el nodo k esta en el camino mas corto entre el nodo i - j
                    if (floydMatrix[i][k] + floydMatrix[k][j] < floydMatrix[i][j]) 
                        floydMatrix[i][j] = floydMatrix[i][k] + floydMatrix[k][j]; 
                } 
            }  
        }
        // Ahora se actualizan sus valores para que indiquen la utilidad que generan entre todos los nodos
        // Se podria haber hecho todo arriba, pero por amor a la legibilidad se separo en dos partes

        int ganancia = 0; // balones de gas * costo de balon + litros de gas * costo de litro
        int costo = 0; // distancia a recorrer (weight) * cantidad de vehiculos * costo del Km
        ArrayList<Integer> utilidades = new ArrayList<Integer>(nNodes); 
        // Lista de las utilidades obtenidas al usar la ciudad i como base
        // siendo i un indice de la lista y a la vez la id de una ciudad.

        // Se inicializa todos los valores de la lista de utilidades en 0
        int n;
        for (n = 0; n < nNodes; n++){
            utilidades.add(0);
        }

        ArrayList<Integer> consumoCiudad;
        
        System.out.println("Matriz con la utilidad de los caminos mas cortos:"); 
        for(i = 0; i < V; i++){ 

            for(j = 0; j < V; j++){ 
                if(floydMatrix[i][j] != INF){ 
                    consumoCiudad = nodesList.get(j).getCiudad().getConsumoCiudad();
                    // Consumo ciudad ahora es una lista [cantBalon, cantLitros] de la ciudad j
                
                    ganancia = consumoCiudad.get(0) * empresa.getPrecioBalon() + consumoCiudad.get(1) * empresa.getPrecioLitro();
                    // Ganancia toma el valor de cant*precio de los respectivos tipos de gas. 

                    costo = nodesList.get(j).getCiudad().getnVehiculos() * floydMatrix[i][j] * empresa.getPrecioKm();
                    // multiplicar costo * 2 si se considera ida y vuelta
                    // Costo toma el valor de:
                    // cantidad de vehiculos en la ciudad j * la distancia desde i a j * el precio del Km 

                    floydMatrix[i][j] = ganancia - costo;
                    // Se cambia el valor de la matriz, pasando de guardar la menor distancia entre i - j
                    // a guardar la utilidad que se genera al ir desde i a j
                    utilidades.set(i, utilidades.get(i) + ganancia - costo);

                    System.out.printf("%12d", floydMatrix[i][j]);                     
                }
                else{
                    System.out.printf("%12s", "---"); 
                }
            } 
            System.out.println("\n"); 
        } 

        // Se imprime la lista de utilidades
        ArrayList<Integer> indiceOptimo = new ArrayList<Integer>();
        for (n = 0; n < V; n++){

            if (indiceOptimo.size() == 0){
                indiceOptimo.add(n);
            }
            else{
                System.out.println(utilidades.get(n) + " == " + utilidades.get(indiceOptimo.get(0)));
                
                if(Integer.compare(utilidades.get(n), utilidades.get(indiceOptimo.get(0))) == 0){
                    System.out.println(" = " );

                    indiceOptimo.add(n);
                }
                if(Integer.compare(utilidades.get(n), utilidades.get(indiceOptimo.get(0))) == 1){
                    indiceOptimo.clear();
                    indiceOptimo.add(n);
                }
            }
            System.out.println("indiceOptimo: " + indiceOptimo.toString());

        }

        if (indiceOptimo.size() == 1){
            System.out.println("La ciudad " + indiceOptimo.get(0) + " es la ubicación óptima");
        }
        else{
            System.out.print("Las ciudades ");
            for (n = 0; n < indiceOptimo.size() - 1; n++){
                System.out.print(indiceOptimo.get(n) + ", "); 
            }
            System.out.print(" y " + indiceOptimo.get(n) + "son las ubicaciones óptimas\n"); 
        }

        int index;
        for (index = 0; index < indiceOptimo.size(); index++){
            System.out.println("\nAl usar la ciudad " + indiceOptimo.get(index) 
            + " como base se obtiene una utilidad total de " + utilidades.get(indiceOptimo.get(index))
            + ", tal que:");
            for (j = 0; j < V; j++){
                System.out.println("Ciudad " + j + ":"); 
                if (floydMatrix[index][j] == INF){
                    System.out.println("- Utilidad: Null, No existe camino");
                }
                else{
                    System.out.println("- Utilidad: " + floydMatrix[index][j]);
                }
                System.out.println("- Se utilizaron: " + nodesList.get(j).getCiudad().getnCisternas() + " camiones cisternas y "
                                                       + nodesList.get(j).getCiudad().getnCamionetas() + " camionetas");
            }
        }
    }


    /** (shortestPath)
    (int)   (origen)    -> id de la ciudad de partida.
    (int)   (destino)   -> id de la ciudad de llegada.
    --------------------
    El método shortestPath utiliza el algoritmo dijkstra a partir de la matriz de adyacencia del grafo.
    Encuentra todos los caminos más cortos desde un nodo (ciudad) hacia todas las demás,
    luego filtra los datos según la ciudad de llegada ingresada por el usuario.
    --------------------
    */
    public List<Integer> shortestPath(int origen, int destino){

        int nVertices = adjMatrix[0].length; 
  
        // menorDistancias[i] almacena la menor distancia que hay entre la ciudad de origen y la ciudad i
        int[] menorDistancias = new int[nVertices]; 
  
        // incluido[i] almacenará true si la ciudad i está incluida en el camino más corto entre origen -> destino.
        boolean[] incluido = new boolean[nVertices]; 

        // el estado inicial de las menores distancias es infinito
        // el estado inicial de las ciudades incluidas en el camino es false
        for (int nodeIndex = 0; nodeIndex < nVertices;  nodeIndex++) { 
            menorDistancias[nodeIndex] = INF; 
            incluido[nodeIndex] = false; 
        } 
          
        // la distancia entre la ciudad de origen y si misma se inicializa en 0 al ser la misma
        menorDistancias[origen] = 0; 
        
        // parents array que almacena el arbol del camino mas corto
        int[] parents = new int[nVertices]; 
  
        // el nodo inicial no tiene padre
        parents[origen] = -1; 
  
        // encuentra el camino más corto para todos los nodos
        for (int i = 1; i < nVertices; i++) { 
  
            int nodoMasCercano = -1; 
            int menorDistancia = INF; 

            // actualiza el nodo mas cercano y su respectiva distancia
            for (int nodeIndex = 0; nodeIndex < nVertices; nodeIndex++) { 
                if (!incluido[nodeIndex] && menorDistancias[nodeIndex] < menorDistancia) {
                    nodoMasCercano = nodeIndex; 
                    menorDistancia = menorDistancias[nodeIndex]; 
                } 
            } 
            
            // si el nodoMasCercano es igual a -1 significa que no encontro un camino más corto para el nodo en el indice
            if(nodoMasCercano != -1){
                // marca el nodo mas cercano como incluido en el camino mas corto
                incluido[nodoMasCercano] = true; 
    
                // actualiza las distancias de los nodos adyacentes al elegido. 
                for (int nodeIndex = 0; nodeIndex < nVertices; nodeIndex++)  { 
                    
                    int edgeDistance = adjMatrix[nodoMasCercano][nodeIndex]; 
                    
                    if (edgeDistance > 0 && ((menorDistancia + edgeDistance) < menorDistancias[nodeIndex])) {

                        parents[nodeIndex] = nodoMasCercano; 
                        menorDistancias[nodeIndex] = menorDistancia + edgeDistance; 
                    } 
                } 
            }  
        } 
        // Al final de las iteraciones, parents almacenará los padres que conforman el menor camino desde la ciudad origen ingresada hacia cualquier otra ciudad del grafo
        // por ejemplo, si el camino mas corto desde 0 -> 3 es 0->2->3, parents tendra la forma [-1, i, 0, 2], donde el padre de la ciudad 3 es 2 y el padre de la ciudad 2 es 0,
        // formando asi el camino más corto.
        List<Integer> camino = new ArrayList<Integer>();
        // Para formar el camino entre el destino indicado por el usuario basta con usar dicho valor como indice del arreglo parents y comenzar a seguir 
        // los indices almacenados hasta llegar al -1 (-1 significa que el nodo que lo almacena no tiene padre, es decir, es el nodo de partida/origen)
        int nodoActual = destino;
        while (nodoActual != -1){
            camino.add(nodoActual);

            nodoActual = parents[nodoActual];
        }
        Collections.reverse(camino); // Como se recorre desde destino -> origen ...
        return camino;
    } 
}
