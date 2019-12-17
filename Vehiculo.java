abstract class Vehiculo{
    protected int consumo;
    protected Empresa empresa;

    /** (getConsumo)
    No recibe parámetros
    --------------------
    Retorna el consumo por kilometro del vehiculo
    --------------------
    */
    int getConsumo(){
        return consumo;
    }

    /** (setConsumo)
    (int)   (consumo)   -> consumo por kilometro
    --------------------
    Asigna un valor al consumo del vehículo
    --------------------
    */
    void setConsumo(int consumo){
        this.consumo = consumo;
    }

    /** (setEmpresa)
    (Empresa)   (empresa)   -> empresa a la que pertenece el vehículo
    --------------------
    Se asigna la empresa que corresponda al vehículo
    --------------------
    */
    void setEmpresa(Empresa empresa){
        this.empresa = empresa;
    }

    /** (getEmpresa)
    No recibe parámetro
    --------------------
    Retorna la empresa a la que pertenece el vehículo
    --------------------
    */
    Empresa getEmpresa(){
        return empresa;
    }
}

class camionCisterna extends Vehiculo{
    
    /** (camionCisterna)
    (int)   (consumo)   -> consumo por kilometro
    --------------------
    Constructor del vehículo de tipo Cisterna. Inicualiza el consumo con un valor ingresado.
    --------------------
    */
    public camionCisterna(int consumo){
        super.consumo = consumo;
    }
}

class Camioneta extends Vehiculo{

    /** (Camioneta)
    (int)   (consumo)   -> consumo por kilometro
    --------------------
    Constructor del vehículo de tipo Camioneta. Inicualiza el consumo con un valor ingresado.
    --------------------
    */
    public Camioneta(int consumo){
        super.consumo = consumo;
    }
}
