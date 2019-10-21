class Pais implements Grafo{
    protected Node nodesList[]; // lista de nodos, cada una de cuales es CIUDAD.
    //lista de ciudades es necesaria porque Pais a Ciudad tiene * (relacion One-To-Many)
    protected int adjMatrix[][];
    int nNodes;
    int nEdges;


    public Pais(int nNodes,int nEdges){
        this.nNodes = nNodes;
        this.nEdges = nEdges;
        this.nodesList = new Node[nNodes];
        this.adjMatrix = new int[nNodes][nNodes];
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
        nodesList[nNodes++] = new Node(id,ciudad);
    }

    //agrega el arco
    public void addEdge(int u,int v, int w){
        adjMatrix[u][v] = w;
        adjMatrix[v][u] = w;
        this.nEdges++;
    }

    //retorna el peso entre los arcos
    public float edgeWeight(int u, int v){
        return adjMatrix[u][v];
    }

    public void printAdjMatrix(){
        for (int i = 0; i < adjMatrix.length; i++) {
            for (int j = 0; j < adjMatrix[i].length; j++) {
                System.out.print(adjMatrix[i][j] + " ");
            }
        }
    }
}
