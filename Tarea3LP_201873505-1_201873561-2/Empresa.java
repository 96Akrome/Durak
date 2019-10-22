class Empresa{
    protected int precioBalon;
    protected int precioLitro;
    protected int precioKm;
//    private Collection<Vehiculo> vehiculo;
    public Empresa(int precioBalon, int precioLitro, int precioKm){
        this.precioKm = precioKm;
        this.precioBalon = precioBalon;
        this.precioLitro = precioLitro;
    }
    int getPrecioBalon(){
        return precioBalon;
    }
    void setPrecioBalon(int precioBalon){
        this.precioBalon = precioBalon;
    }

    int getPrecioLitro(){
        return precioLitro;
    }
    void setPrecioLitro(int precioLitro){
        this.precioLitro = precioLitro;
    }
}
