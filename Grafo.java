interface Grafo{
    public void addNode(int id, Ciudad ciudad); //pantufla permitio agregar mas cosas en addNode
    public void addEdge(int u,int v, int w);
    public float edgeWeight(int u, int v);
    //shortestPath
}


class Node{
    int id;
    Ciudad ciudad;
    
    /** (Node)
    (int)       (id)        -> identificador del nodo/ciudad
    (Ciudad)    (ciudad)    -> ciudad que se almacenará en el nodo
    --------------------
    Constructor del nodo correspondiente a cada ciudad identificado con una id ingresada
    --------------------
    */
    public Node(int id, Ciudad ciudad){
        this.id = id;
        this.ciudad = ciudad;
        //this.wasVisited = false; lo mismo
    }

    /** (getId)
    No recibe parámetros
    --------------------
    Retorna la id almacenada en el nodo
    --------------------
    */
    public int getId(){
        return id;
    }

    /** (getCiudad)
    No recibe parámetros
    --------------------
    Retorna la ciudad almacenada en el nodo
    --------------------
    */
    public Ciudad getCiudad(){
        return ciudad; 
    }
}
