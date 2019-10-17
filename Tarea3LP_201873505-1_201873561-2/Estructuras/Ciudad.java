class Ciudad{
    protected int id;
    protected int nEdificios;
    protected int nCasas;
    private Collection<Edificacion> edificacion;
    int getId(){
        return id;
    }
    void setId(int id){
        this.id = id;
    }

    int getnEdificios(){
        return nEdificios;
    }
    void setnEdificios(int nEdificios){
        this.nEdificios = nEdificios;
    }

    int getnCasas(){
        return nCasas;
    }
    void setnCasas(int nCasas){
        this.nCasas = nCasas;
    }
}
