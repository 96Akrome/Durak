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

}
