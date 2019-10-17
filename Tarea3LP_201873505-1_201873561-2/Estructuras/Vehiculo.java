class Vehiculo{
    protected int consumo;
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
