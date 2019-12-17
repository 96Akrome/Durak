import java.util.ArrayList;
class Empresa{
    protected int precioBalon;
    protected int precioLitro;
    protected int precioKm;
    ArrayList<Vehiculo> vehiculo; 

    /** (Empresa)
    (int)   (precioBalon)   -> Precio del balón de gas de la empresa
    (int)   (precioLitro)   -> Precio del litro de gas de la empresa
    (int)   (precioKm)      -> Precio por kilometro de la empresa
    --------------------
    Constructor de la Empresa, inicializa sus valores con los ingresados en los parámetros.
    --------------------
    */
    public Empresa(int precioBalon, int precioLitro, int precioKm){
        this.precioKm = precioKm;
        this.precioBalon = precioBalon;
        this.precioLitro = precioLitro;
        vehiculo = new ArrayList<Vehiculo>();
    }

    /** (getPrecioBalon)
    No recibe parámetros
    --------------------
    Retorna el precio del balon de gas de la empresa
    --------------------
    */
    int getPrecioBalon(){
        return precioBalon;
    }

    /** (setPrecioBalon)
    (int)   (precioBalon)   -> valor del nuevo precio para el balon de gas de la empresa
    --------------------
    Asigna un valor al precio del balon de gas
    --------------------
    */
    void setPrecioBalon(int precioBalon){
        this.precioBalon = precioBalon;
    }

    /** (getPrecioLitro)
    No recibe parámetros
    --------------------
    Retorna el precio del litro de gas de la empresa
    --------------------
    */
    int getPrecioLitro(){
        return precioLitro;
    }

    /** (setPrecioLitro)
    (int)   (precioLitro)   -> valor del nuevo precio para el Litro de gas de la empresa
    --------------------
    Asigna un valor al precio del litro de gas
    --------------------
    */
    void setPrecioLitro(int precioLitro){
        this.precioLitro = precioLitro;
    }

    /** (setPrecioKm)
    (int)   (precioKm)   -> valor del nuevo precio por kilometro de la empresa
    --------------------
    Asigna un valor al precio del kilometro
    --------------------
    */
    void setPrecioKm(int precioKm){
        this.precioKm = precioKm;
    }

    /** (getPrecioKm)
    No recibe parámetros
    --------------------
    Retorna el precio por kilometro de la empresa
    --------------------
    */
    int getPrecioKm(){
        return precioKm;
    }
}