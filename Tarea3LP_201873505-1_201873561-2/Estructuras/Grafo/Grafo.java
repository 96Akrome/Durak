interface Grafo{
//    int nNodes = 0; // wn variables de interfaz son estaticas y finales, no se que chucha
//    int nEdges = 0; //segun pdf van aca pero no los puedo reasignar
    public void addNode(int id);
    public void addEdge(int u,int v, int w);
    public float edgeWeight(int u, int v);
    //shortestPath
}


class Node{
    int id;
    boolean wasVisited; //si no vamos a usar dijkstra con dfs (mejor warshall), se puede borrar

    public Vertex(int id){
        this.id = id;
        this.wasVisited = false; //lo mismo
    }
}

class Pais implements Grafo{
    private Node nodesList[];
    private int adjMatrix[][];
    int nNodes;
    int nEdges;
    //private Stack<Integer> stack; para dfs, si no, se borra


    public Pais(int nNodes){
    //    Grafo.nNodes = nNodes;
        this.nNodes = nNodes;
        this.nEdges = 0;
        this.vertexList = new Node[nNodes];
        this.adjMatrix = new int[nNodes][nNodes];
        //stack = new Stack<Integer>();
    }

    //getter de vertices
    public int getnVertex(){
        return nVertex;
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

    static public void main(String [] args){

    }
}
