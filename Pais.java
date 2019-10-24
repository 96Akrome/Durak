import java.util.ArrayList;

class Pais implements Grafo{
    ArrayList<Node> nodesList; // lista de nodos, cada una de cuales es CIUDAD.
    //lista de ciudades es necesaria porque Pais a Ciudad tiene * (relacion One-To-Many)
    int adjMatrix[][];
    int nNodes;
    int nEdges;
    static final int INF = 9999;
    Empresa empresa;

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

    //getter de vertices
    public int getnVertex(){
        return nNodes;
    }
    //getter de arcos, no se para que de verdad pero pico
    public int getnEdges(){
        return nEdges;
    }

    //agrega un vertice a la lista de vertices
    public void addNode(int id, Ciudad ciudad){
        nodesList.set(id, (new Node(id,ciudad)));
    }

    //agrega el arco
    public void addEdge(int u,int v, int w){
        adjMatrix[u][v] = w;
        adjMatrix[v][u] = w;
        System.out.println("Se ha agregado el arco: " + u + " -> " + v + " con peso " + w);
    }

    //retorna el peso entre los arcos
    public float edgeWeight(int u, int v){
        System.out.println("El peso del arco" + u + " " + v + "es: " + adjMatrix[u][v]);
        return adjMatrix[u][v];
    }

    public void printAdjMatrix(){
        System.out.println("\nLa matriz de adyacencia del grafo es: ");
        for (int i = 0; i < adjMatrix.length; i++) {
            for (int j = 0; j < adjMatrix[i].length; j++) {
                if(adjMatrix[i][j] == INF){
                    System.out.print("inf" + " ");
                }
                else{
                    System.out.print(adjMatrix[i][j] + " ");
                }
            }
            System.out.println("\n");
        }
    }
    // Metodos nuevos:

    // Actualiza los precios de la empresa:
    public void setEmpresa(Empresa empresa){
        this.empresa = empresa;
    }

    // floyd warshall para obtener el shorthest-path
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
                    // Costo toma el valor de:
                    // cantidad de vehiculos en la ciudad j * la distancia desde i a j * el precio del Km 

                    floydMatrix[i][j] = ganancia - costo;
                    // Se cambia el valor de la matriz, pasando de guardar la menor distancia entre i - j
                    // a guardar la utilidad que se genera al ir desde i a j
                    System.out.print(floydMatrix[i][j]+"   "); 

                    utilidades.set(i, utilidades.get(i) + ganancia - costo);
                }
                else{
                    System.out.print("INF "); 
                }
            } 
            System.out.println(); 
        } 

        // Se imprime la lista de utilidades
        System.out.println("Print rapido, despues se separara por optimo");

        for (n = 0; n < V; n++){
            System.out.println("Al usar la ciudad " + n 
            + " como base se obtiene una utilidad total de " + utilidades.get(n)
            + ", tal que:");
            for (j = 0; j < V; j++){
                System.out.println("Ciudad " + j + ":"); 
                System.out.println("- Utilidad: " + floydMatrix[n][j]);
                System.out.println("- Se utilizaron: " + nodesList.get(j).getCiudad().getnVehiculos() + " vehiculos (TODO: Separar por tipo)");
            }
        }
    }
}
