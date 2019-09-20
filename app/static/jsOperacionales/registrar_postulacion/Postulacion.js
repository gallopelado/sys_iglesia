import { autoCompletar } from '../helper/helper.js';
import Documento from '../helper/Documento.js';

export default class Postulacion {

    constructor() {
        
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
    

    validarForm() {

        if (this.nombrecomite === '')
            return false;
        
        if (this.descripcion === '')
            return false;

        if (this.tabla.tBodies.length === 0)
            return false;
        
        if (this.fechainicio.value === '')
            return false;

        if (this.fechafin.value === '')
            return false;

        return true;

    }

    getDatosFormulario() {

        // Generar instancia de FormData
        const datos = new FormData();

        // Generar instancia de la clase Documento.
        const docu = new Documento();

        // Obtener detalle.
        const tabla = this.tabla;
        //console.log(this.tabla.rows.length);
        if (this.tabla.rows !== undefined) {
            
            if(this.tabla.rows.length > 0) {

                // recorrer la tabla
                for (let i = 1; i < this.tabla.rows.length; i++) {

                    console.log(tabla.rows[i].id);

                }

            }

        }
        
        // Agregando al objeto datos.
        //datos.append('idcomite', this.idcomite.value);
        //datos.append('descripcion', this.descripcion.value.trim());        

    }


}