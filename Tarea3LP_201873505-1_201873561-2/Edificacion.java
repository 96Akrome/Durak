abstract class Edificacion{
    protected int consumo;
    protected Ciudad ciudad;
    static String tipo;

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
    public  String getTipo(){
        return tipo;
    }
}

class Casa extends Edificacion{
    public Casa(int consumo){
        super.consumo = consumo;
        Edificacion.tipo = "Casa";
    }

}

class Edificio extends Edificacion{
    public Edificio(int consumo){
        super.consumo = consumo;
        Edificacion.tipo = "Edificio";
    }

}
