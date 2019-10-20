import java.util.List;
import java.util.LinkedList;

class Pais implements Grafo{
    public void Grafo(int nNodes){
        Grafo.nNodes = nNodes;
        adjList =  new LinkedList[nNodes];
        for(int i = 0; i < adjList.length; i++)
			adjList[i] = new LinkedList<>();
	}

    void addEdge(int u, int v, int w){
        //u - inicio
        //v - destino
        //w - peso
		adjList[u].add(new Edge(v, w));
        Grafo.nEdges++;
	}
    public String toString(){
		String result="";
		for(int i = 0;i < adjList.length; i++)
			result += i + "->" + adjList[i] + "\n";
		return result;
	}

    static public void main(String [] args){
        Grafo g = new Grafo(3);
        g.addEdge(0,1,3);
        System.out.println(g.toString());
    }
    //float edgeWeight(){

//}
}
