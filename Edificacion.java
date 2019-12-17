abstract class Edificacion{
    protected int consumo;
    protected Ciudad ciudad;
    static String tipo;
 
    /** (getConsumo)
    No recibe parámetros
    --------------------
    Retorna el valor del consumo de la edificación.
    --------------------
    */
    int getConsumo(){
        return consumo;
    }

    /** (setConsumo)
    (int)   (consumo)   -> valor del nuevo consumo que tendrá la edificación
    --------------------
    Asigna un valor al consumo de la edificación
    --------------------
    */
    void setConsumo(int consumo){
        this.consumo = consumo;
    }

    /** (getCiudad)
    No recibe parámetros
    --------------------
    Retorna la ciudad a la que pertenece la edificación
    --------------------
    */
    Ciudad getCiudad(){
        return ciudad;
    }

    /** (setCiudad)
    (Ciudad)    (ciudad)    -> valor de la ciudad a la que pertenece la edificación
    --------------------
    Asigna la ciudad a la que pertenece la edificación
    --------------------
    */
    void setCiudad(Ciudad ciudad){
        this.ciudad = ciudad;
    }

    /** (getTipo)
    No recibe parámetros
    --------------------
    Retorna el tipo de edificación correspondiente. 
    --------------------
    */
    public String getTipo(){
        return tipo;
    }
}

class Casa extends Edificacion{

    /** (Casa)
    (int)   (consumo)   -> valor del nuevo consumo que tendrá la casa
    --------------------
    Constructor de la casa. Asigna un valor al consumo de esta y asigna "Casa" a su tipo de edificación.
    --------------------
    */
    public Casa(int consumo){
        super.consumo = consumo;
        Edificacion.tipo = "Casa";
    }

}

class Edificio extends Edificacion{

    /** (Edificio)
    (int)   (consumo)   -> valor del nuevo consumo que tendrá el edificio
    --------------------
    Constructor del edificio. Asigna un valor al consumo de este y asigna "Edificio" a su tipo de edificación.
    --------------------
    */
    public Edificio(int consumo){
        super.consumo = consumo;
        Edificacion.tipo = "Edificio";
    }
}