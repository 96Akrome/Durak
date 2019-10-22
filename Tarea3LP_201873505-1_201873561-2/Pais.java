import java.util.ArrayList;

class Pais implements Grafo{
    ArrayList<Node> nodesList; // lista de nodos, cada una de cuales es CIUDAD.
    //lista de ciudades es necesaria porque Pais a Ciudad tiene * (relacion One-To-Many)
    int adjMatrix[][];
    int nNodes;
    int nEdges;
    static final int INF = 9999;
    public Pais(int nNodes,int nEdges){
        System.out.println("Se ha creado un nuevo pais!");
        this.nNodes = nNodes;
        this.nEdges = nEdges;
        nodesList = new ArrayList<Node>();
        this.adjMatrix = new int[nNodes][nNodes];
        //inicializo todas las distancias como INF
        for (int i = 0; i < adjMatrix.length; i++) {
            for (int j = 0; j < adjMatrix[i].length; j++) {
                adjMatrix[i][j] =  INF;
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
        nodesList.add(new Node(id,ciudad));
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

    public void printNodes(){
        System.out.println("\nLa lista de nodos es: ");
        System.out.println(nodesList);
    }
}
