import { autoCompletar } from '../helper/helper.js';

export default class Postulacion {

    constructor() {

        this.id = document.getElementById('idpostulacion');
        this.idcomite = document.getElementById('idministerio');
        this.nombrecomite = document.getElementById('txt_ministerio');
        this.descripcion = document.getElementById('txt_descripcion');
        this.lugaresdisponibles = document.getElementById('txt_lugares');
        this.preview_documento = document.getElementById('txt_nombredocumento');
        this.documento = document.getElementById('txt_documento');
        this.idpuesto = document.getElementById('idpuesto');
        this.puesto = document.getElementById('txt_puesto');
        this.vacancias =  document.getElementById('txt_vacancias');
        this.tabla = document.getElementById('tabla_detalle');
        this.tabla_tbody = document.getElementById('tb_detalle');
        this.fechainicio = document.getElementById('txt_fechainicio');
        this.fechafin = document.getElementById('txt_fechafin');
        this.btnguardar = document.getElementById('btnGuardar');
        this.btncancelar = document.getElementById('btnCancelar');

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

    /**
     * Formatea las fechas con la libreria datetimepicker de tempus.
     * La fecha de inicio/fin permiten solamente la seleccion
     * de fecha actual y futura.
     */
    inicializarFechas() {

        $(`#picker_fechainicio`).datetimepicker({
            minDate: new Date(),
            defaultDate: '',
            format: 'L',
            locale: 'es',
            format: 'DD/MM/YYYY',
            useCurrent: false        
        });

        $(`#picker_fechafin`).datetimepicker({
            minDate: new Date() + 1,
            defaultDate: '',
            format: 'L',
            locale: 'es',
            format: 'DD/MM/YYYY',
            useCurrent: false        
        });

    }

    gestionarDetalle() {

        const tabla = document.getElementById('tb_detalle');
        const dimen = tabla.rows.length;
        //if (dimen >)

    }


}