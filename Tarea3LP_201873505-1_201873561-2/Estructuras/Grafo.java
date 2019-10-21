interface Grafo{
    public void addNode(int id, Ciudad ciudad); //pantufla permitio agregar mas cosas en addNode
    public void addEdge(int u,int v, int w);
    public float edgeWeight(int u, int v);
    //shortestPath
}


class Node{
    int id;
    Ciudad ciudad;
    //boolean wasVisited; si no vamos a usar dijkstra con dfs (mejor warshall), se puede borrar

    public Node(int id, Ciudad ciudad){
        this.id = id;
        this.ciudad = ciudad;
        //this.wasVisited = false; lo mismo
    }
}

//clase para guardar nombres de archivos, analogo de define
//dato freak: #define no existe en java porque no hay un pre-compilador
public class Constants {
    public static final String archive_1 = "mapa.txt";
    public static final String archive_2 = "edificaciones.txt";
    public static final String archive_3 = "empresa.txt";
}
