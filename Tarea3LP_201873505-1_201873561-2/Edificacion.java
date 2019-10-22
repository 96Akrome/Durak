abstract class Edificacion{
    protected int consumo;
    protected Ciudad ciudad;

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
    public final String tipo = "Casa";
    public Casa(int consumo){
        super.consumo = consumo;
    }

    public  String getTipo(){
        return tipo;
    }
}

class Edificio extends Edificacion{
    public final String tipo = "Edificio";
    public Edificio(int consumo){
        super.consumo = consumo;
    }

    public  String getTipo(){
        return tipo;
    }
}
