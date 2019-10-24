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

    int getId(){
        return id;
    }
    void setId(int id){
        this.id = id;
    }

    int getnEdificios(){
        return nEdificios;
    }
    void setnEdificios(int nEdificios){
        this.nEdificios = nEdificios;
    }

    int getnCasas(){
        return nCasas;
    }
    void setnCasas(int nCasas){
        this.nCasas = nCasas;
    }

    void addEdificacion(Edificacion edificacion){
        System.out.println("Se ha agregado una edificio de tipo " + edificacion.getTipo());
        edificaciones.add(edificacion);
    }

    // Metodos nuevos:

    // Consumo de gas de la ciudad
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

    // Numero de vehiculos necesarios para la ciudad
    int getnVehiculos(){
        int nVehiculos = this.nEdificios;
        if(this.nCasas > 0){
            nVehiculos += 1;
        }
        return nVehiculos;
    }
}
