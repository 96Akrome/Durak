abstract class Vehiculo{
    protected int consumo;
    private Empresa empresa;

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

    static public void main(String [] args){
        Camioneta c = new Camioneta(10);
        c.mostrar();
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
