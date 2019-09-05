class Postulacion {

    constructor() {

        this.id = document.getElementById('idpostulacion');
        this.idcomite = document.getElementById('idministerio');
        this.nombrecomite = document.getElementById('txt_ministerio');
        this.descripcion = document.getElementById('txt_descripcion');
        this.lugaresdisponibles = document.getElementById('txt_lugares');
        this.preview_documento = '';
        this.documento;
        this.idpuesto;
        this.puesto;
        this.tabla;
        this.tabla_tbody;
        this.fechainicio;
        this.fechafin;
        this.btnguardar;
        this.btncancelar;

    }

}