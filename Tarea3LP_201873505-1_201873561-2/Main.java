import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

//clase para guardar nombres de archivos, analogo de define
//dato freak: #define no existe en java porque no hay un pre-compilador
class Constants {
    public static final String archive_1 = "mapa.txt";
    public static final String archive_2 = "edificaciones.txt";
    public static final String archive_3 = "empresa.txt";
}

class Main{
    static public void main(String [] args){
        //Lectura de archivo (usando clase Scanner)
        Pais graph = null;
        Scanner input = null;
        File file = null;
        //lectura de archivo mapa.txt
        try{
            file = new File(Constants.archive_1);
            input = new Scanner(file);
            //primera linea - nNodes, segunda - nEdges, adelante: u v w;
            int n = input.nextInt();
            int e = input.nextInt();
            System.out.println("La cantidad de nodos es: " + n);
            System.out.println("La cantidad de arcos es: " + e);
            graph = new Pais(n,e);
            while(!(input.nextLine()).isEmpty()){
                System.out.println(input.nextLine().isEmpty());
                int u = input.nextInt();
                int v = input.nextInt();
                int w = input.nextInt();
                graph.addEdge(u, v, w);
            }
        }
        catch(FileNotFoundException e){
            System.out.println("Error en apertura de archivo " + file +".");
            e.printStackTrace();
        }
        finally{
            input.close();
        }
        System.out.println("Llegue a leer las edificaciones");
        //lectura de archivo edificaciones.txt
        try{
            file = new File(Constants.archive_2);
            input = new Scanner(file);
            //ciudad casas edificios
            //consumo de cada casa
            //consumo de cada edificio
            //aqui queremos leer de a 3 lineas.
            while(!(input.nextLine()).isEmpty()){
                int idCiudad = input.nextInt();
                int nCasas = input.nextInt();
                int nEdificios = input.nextInt();
                Ciudad c = new Ciudad(nCasas,nEdificios);


                //crear cosas con casas y edificios
                for(int i = 0; i < nCasas; i++){
                    int consumo = input.nextInt();
                    Casa ca = new Casa(consumo);
                    c.addEdificacion(ca);
                }
                for(int i = 0; i < nEdificios; i++){
                    int consumo = input.nextInt();
                    Edificio edi = new Edificio(consumo);
                    c.addEdificacion(edi);

                }
                //finalmente, agrego ciudad al pais.
                graph.addNode(idCiudad, c);
            }
            input.close();
        }
        catch(FileNotFoundException e){
            System.out.println("Error en apertura de archivo " + file +".");
            e.printStackTrace();
        }
        finally{
            input.close();
        }

        try{
            file = new File(Constants.archive_3);
            input = new Scanner(file);
            //Formato de archivo: (solo 3 lineas)
            //precio balon de gas
            //precio litro de gas
            //costo por kilometro
            int balon = input.nextInt();
            int litro = input.nextInt();
            int costoKm = input.nextInt();
            Empresa empresa = new Empresa(balon, litro, costoKm);
            input.close();
        }
        catch(FileNotFoundException e){
            System.out.println("Error en apertura de archivo " + file +".");
            e.printStackTrace();
        }
        finally{
            input.close();
        }
    }
}
