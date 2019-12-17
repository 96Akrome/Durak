import java.util.ArrayList;
class Ciudad{
    protected int id;
    protected int nEdificios;
    protected int nCasas;
    ArrayList<Edificacion> edificaciones;

    public Ciudad(int nCasas, int nEdificios){
        System.out.println("Se ha creado una ciudad, con " + nCasas + " casas y " + nEdificios + " edificios.");
        this.nCasas = nCasas;
        this.nEdificios = nEdificios;
        edificaciones = new ArrayList<Edificacion>();
    }

    /** (getId)
    No recibe parámetros
    --------------------
    Retorna la id de la ciudad 
    --------------------
    */
    int getId(){
        return id;
    }

    /** (setId)
    (int)   (id)    -> valor correspondiente a la id de la ciudad
    --------------------
    Asigna la id a la ciudad 
    --------------------
    */
    void setId(int id){
        this.id = id;
    }

    /** (getnEdificios)
    No recibe parámetros
    --------------------
    Retorna la cantidad de edificaciones de tipo "Edificio" que hay en la ciudad.
    --------------------
    */
    int getnEdificios(){
        return nEdificios;
    }

    /** (setnEdificios)
    (int)   (nEdificios)    -> cantidad de Edificios    
    --------------------
    Asigna un nuevo valor a la cantidad de edificios de la ciudad 
    --------------------
    */
    void setnEdificios(int nEdificios){
        this.nEdificios = nEdificios;
    }

    /** (getnCasas)
    No recibe parámetros
    --------------------
    Retorna la cantidad de edificaciones de tipo "Casa" que hay en la ciudad.
    --------------------
    */
    int getnCasas(){
        return nCasas;
    }

    /** (setnCasas)
    (int)   (nCasas)    -> cantidad de Casas    
    --------------------
    Asigna un nuevo valor a la cantidad de casas de la ciudad 
    --------------------
    */
    void setnCasas(int nCasas){
        this.nCasas = nCasas;
    }

    /** (addEdificacion)
    (Edificacion)   (edificacion)   -> cantidad de Edificios    
    --------------------
    Agrega una nueva edificación a la ciudad
    --------------------
    */
    void addEdificacion(Edificacion edificacion){
        System.out.println("Se ha agregado una edificio de tipo " + edificacion.getTipo());
        edificaciones.add(edificacion);
    }

    /** (getConsumoCiudad)
    No recibe parámetros
    --------------------
    Retorna el consumo total de gas en un arreglo de enteros, donde el primer elemento
    almacena el consumo total de las casas y el segundo elemento el consumo total de los edificios
    --------------------
    */
    ArrayList<Integer> getConsumoCiudad(){
        int i;
        ArrayList<Integer> consumoCiudad = new ArrayList<Integer>(2); // [cantidadTotalBalones, cantidadTotalLitros]
        for(i = 0; i < 2; i++){
            consumoCiudad.add(0);
        }
        for(i = 0; i < edificaciones.size(); i++){
            // Si la edificacion en la posicion i es de tipo "Casa"
            if(edificaciones.get(i).getTipo().equals("Casa")){
                consumoCiudad.set(0, consumoCiudad.get(0) + edificaciones.get(i).getConsumo());
            }
            // Si la edificacion en la posicion i es de tipo "Edificio"
            else if(edificaciones.get(i).getTipo().equals("Edificio")){
                consumoCiudad.set(1, consumoCiudad.get(1) + edificaciones.get(i).getConsumo());
            }
        }
        return consumoCiudad;
    }

    /** (getnCisternas)
    No recibe parámetros
    --------------------
    Retorna el número de camiones cisternas que necesita la ciudad según la cantidad de edificios que esta tenga
    --------------------
    */
    int getnCisternas(){
        return this.nEdificios; // 1 cisterna por cada edificio de la ciudad
    }

    /** (getnCamionetas)
    No recibe parámetros
    --------------------
    Retorna el número de camionetas que necesita la ciudad según la cantidad de casas que esta tenga
    --------------------
    */
    int getnCamionetas(){
        if(this.nCasas > 0){ // 1 camioneta para todas las casas de una ciudad
            return 1;
        }
        return 0;
    }

    /** (getnVehiculos)
    No recibe parámetros
    --------------------
    Retorna el número total de vehiculos (camionetas + camiones cisternas) que necesita la ciudad 
    según la cantidad de edificios y casas que esta tenga
    --------------------
    */
    int getnVehiculos(){
        int nVehiculos = this.nEdificios;
        if(this.nCasas > 0){
            nVehiculos += 1;
        }
        return nVehiculos;
    }
}