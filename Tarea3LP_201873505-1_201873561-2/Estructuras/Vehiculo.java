abstract class Vehiculo{
    protected int consumo;
    protected Empresa empresa;

    int getConsumo(){
        return consumo;
    }
    void setConsumo(int consumo){
        this.consumo = consumo;
    }
    void setEmpresa(Empresa empresa){
        this.empresa = empresa;
    }
    Empresa getEmpresa(){
        return empresa;
    }
}

class camionCisterna extends Vehiculo{
    public camionCisterna(int consumo){
        super.consumo = consumo;
    }
}

class Camioneta extends Vehiculo{
    public Camioneta(int consumo){
        super.consumo = consumo;
    }
}
