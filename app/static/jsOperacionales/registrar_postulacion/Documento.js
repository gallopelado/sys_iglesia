class Documento {

    constructor() {

        this.nombre;
        this.extension;
        this.dimension;
        this.ruta;
        this.nropaginas;
        this.binario;
        
    }

    agregarDocumento(documento) {
        this.binario = documento;
    }

}