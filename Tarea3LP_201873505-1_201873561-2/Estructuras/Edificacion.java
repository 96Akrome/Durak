abstract class Edificacion{
    protected int consumo;
    private Ciudad ciudad;

    int getConsumo(){
        return consumo;
    }
    void setConsumo(int consumo){
        this.consumo = consumo;
    }

    Ciudad getCiudad(){
        return ciudad;
    }
    void setCiudad(Ciudad ciudad){
        this.ciudad = ciudad;
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
