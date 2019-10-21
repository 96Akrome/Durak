class Pais implements Grafo{
    private Node nodesList[];
    private int adjMatrix[][];
    int nNodes;
    int nEdges;
    //private Stack<Integer> stack; para dfs, si no, se borra


    public Pais(int nNodes,int nEdges){
        this.nNodes = nNodes;
        this.nEdges = nEdges;
        this.nodesList = new Node[nNodes];
        this.adjMatrix = new int[nNodes][nNodes];
        //stack = new Stack<Integer>();
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
    public void addNode(int id){
        nodesList[nNodes++] = new Node(id);
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
