import java.util.ArrayList;
class Empresa{
    protected int precioBalon;
    protected int precioLitro;
    protected int precioKm;
    ArrayList<Vehiculo> vehiculo;
    public Empresa(int precioBalon, int precioLitro, int precioKm){
        this.precioKm = precioKm;
        this.precioBalon = precioBalon;
        this.precioLitro = precioLitro;
        vehiculo = new ArrayList<Vehiculo>();
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

    void setPrecioKm(int precioKm){
        this.precioKm = precioKm;
    }

    int getPrecioKm(){
        return precioKm;
    }


}
