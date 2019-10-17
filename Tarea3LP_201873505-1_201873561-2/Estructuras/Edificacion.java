class Edificacion{
    protected int consumo;
}

class Casa extends Edificacion{
    public Casa(int consumo){
        super.consumo = consumo;
    }
}

class Edificio extends Edificacion{
    public Edificio(int consumo){
        super.consumo = consumo;
    }
}
