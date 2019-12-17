import java.util.ArrayList;
import java.util.Collections;
import java.util.*; 
import java.lang.*; 
import java.io.*; 
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

//clase para guardar nombres de archivos, analogo de define
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
            System.out.println("La cantidad de nodos (ciudades) es: " + n);
            System.out.println("La cantidad de arcos (caminos) es: " + e);
            graph = new Pais(n,e);
            while(input.hasNextInt()){
                int u = input.nextInt();
                int v = input.nextInt();
                int w = input.nextInt();
                System.out.println("La linea es " + u + " " + v + " " + w);
                graph.addEdge(u, v, w); 
                // Quizas revisaria que u != v
            }
        }
        catch(FileNotFoundException e){
            System.out.println("Error en apertura de archivo " + file +".");
            e.printStackTrace();
        }
        finally{
            input.close();
            graph.printAdjMatrix();
        }
        //lectura de archivo edificaciones.txt
        try{
            file = new File(Constants.archive_2);
            input = new Scanner(file);
            //ciudad casas edificios
            //consumo de cada casa
            //consumo de cada edificio
            //aqui queremos leer de a 3 lineas.
            while(input.hasNextInt()){
                int idCiudad = input.nextInt();
                int nCasas = input.nextInt();
                int nEdificios = input.nextInt();
                Ciudad c = new Ciudad(nCasas,nEdificios); 
                // quizas agregaria un set id para la ciudad
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
        }
        catch(FileNotFoundException e){
            System.out.println("Error en apertura de archivo " + file + ".");
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
            Empresa empresa = new Empresa(balon, litro, costoKm); //warning de no usar eso, una vez que llames a algun campo de empresa se va a desaparecer.
            graph.setEmpresa(empresa);
        }
        catch(FileNotFoundException e){
            System.out.println("Error en apertura de archivo " + file + ".");
            e.printStackTrace();
        }
        finally{
            input.close();
        }
        //con eso, tengo todos los datos guardados y se puede proceder a trabajar
        //con shortestPath
        //recordar usar getters para cosas como costo de balon de la empresa etc etc.
        //also, recordar que optimo puede ser NO UNICO (detalle importante)

        graph.printOptimo();
        Scanner numCiudad = new Scanner(System.in);

        System.out.println("\nPara utilizar la función shortestPath ingrese el número de la ciudad solicitada, de lo contrario ingrese un número menor a 0:");
        int ciudadDestino = 0;
        int ciudadOrigen = 0;
        while(ciudadDestino >= 0 && ciudadOrigen >= 0){
            System.out.println("- Ciudad de origen: ");
            try{
                ciudadOrigen = numCiudad.nextInt();

                if (ciudadOrigen >= 0){
                    System.out.println("- Ciudad de destino: ");
                    try{
                        ciudadDestino = numCiudad.nextInt();

                        // Caso de error: el numero ingresado se escapa del indice de la lista de nodos/ciudades
                        if (ciudadDestino >= 0){
                            if(ciudadDestino > graph.getnVertex() || ciudadOrigen > graph.getnVertex()){
                                System.out.println("Uno de los valores ingresados es mayor o igual que el número de ciudades que existen");
                                System.out.println("- Cantidad de ciudades: "+ graph.getnVertex());
                                System.out.println("*Las ciudades parten con indice 0*\n");
                            }
                            else{

                                List<Integer> camino = graph.shortestPath(ciudadOrigen, ciudadDestino);
                                System.out.println("El camino más corto entre ciudad " + ciudadOrigen + " y ciudad " + ciudadDestino + " es:");
                                int indice;
                                for (indice = 0; indice < camino.size() - 1; indice++){
                                    System.out.printf("%d ->", camino.get(indice));
                                }
                                System.out.println(camino.get(indice) + "\n");
                            }
                        }
                    }
                    // Caso de error: el tipo de dato ingresado no es un int
                    catch(InputMismatchException e){
                        System.out.println("Error al scanear input del usuario, tipo de dato esperado: int");
                        return;
                    }
                }
            }
            catch(InputMismatchException e){
                System.out.println("Error al scanear input del usuario, tipo de dato esperado: int");
                return;
            }
        }
    }
}
