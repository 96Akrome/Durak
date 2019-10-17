class Edificacion{
    protected int consumo;

    int getConsumo(){
        return consumo;
    }
    void setConsumo(int consumo){
        this.consumo = consumo;
    }
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
