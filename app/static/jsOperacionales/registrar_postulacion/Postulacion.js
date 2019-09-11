import { autoCompletar } from '../helper/helper.js';

export default class Postulacion {

    constructor(id, idcomite, nombrecomite, descripcion,
        lugaresdisponibles, preview_documento, documento, 
        idpuesto, puesto, tabla, tabla_tbody, fechainicio,
        fechafin, btnguardar, btncancelar) {

        this.id = id;
        this.idcomite = idcomite;
        this.nombrecomite = nombrecomite;
        this.descripcion = descripcion;
        this.lugaresdisponibles = lugaresdisponibles;
        this.preview_documento = preview_documento;
        this.documento = documento;
        this.idpuesto = idpuesto;
        this.puesto = puesto;
        this.tabla = tabla;
        this.tabla_tbody = tabla_tbody;
        this.fechainicio = fechainicio;
        this.fechafin = fechafin;
        this.btnguardar = btnguardar;
        this.btncancelar = btncancelar;

    }

    async getMinisterios() {

        const endpoint = '/membresia/formulario_postulacion/get_ministerios';

        try {
            
            const res = await fetch(endpoint);
            const data = await res.json()

            autoCompletar(data, 'descripcion', 'id', 'idministerio', 'txt_ministerio');
            
        } catch (error) {
            console.error(error);
        }

    }

    async getProfesiones() {

        const endpoint = '/membresia/formulario_postulacion/get_profesiones';

        try {
            
            const res = await fetch(endpoint);
            const data = await res.json()            

            autoCompletar(data, 'descripcion', 'id', 'idpuesto', 'txt_puesto');
            
        } catch (error) {
            console.error(error);
        }

    }

}