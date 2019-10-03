import { autoCompletar } from '../helper/helper.js';
import Documento from '../helper/Documento.js';

/**
 * Clase Postulación.
 * 
 * Se definen los métodos para gestionar la vista Postulación.
 * 
 * @author Juan José González Ramírez <juanftp100@gmail.com>
 */
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
        this.vacancias = document.getElementById('txt_vacancias');
        this.tabla = document.getElementById('tabla_detalle');
        this.tabla_tbody = document.getElementById('tb_detalle');
        this.fechainicio = document.getElementById('txt_fechainicio');
        this.fechafin = document.getElementById('txt_fechafin');
        this.btnguardar = document.getElementById('btnGuardar');
        this.btncancelar = document.getElementById('btnCancelar');

    }


    /**
     * Método getMinisterios.(ASINCRÓNICO)
     * 
     * Se obtiene vía GET id, descripción en formato JSON
     * para autocompletar campo.
     * 
     */
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


    /**
     * Método getProfesiones.(ASINCRÓNICO)
     * 
     * Se obtiene vía GET id, descripción en formato JSON
     * para autocompletar campo.
     * 
     */
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


    /**
     * Método validarForm
     * 
     * Sirve para validar campos vacíos del formulario.
     * 
     */
    validarForm() {

        if (this.nombrecomite.value === '') {
            alert('Nombre de comite vacio');
            this.nombrecomite.focus();
            return false;
        }
        if (this.descripcion.value === '') {
            alert('Descripcion vacio');
            this.descripcion.focus();
            return false;
        }

        if (this.tabla_tbody.rows.length === 0) {
            alert('Tabla de puestos vacio');
            this.puesto.focus();
            return false;
        }
        if (this.fechainicio.value === '') {
            alert('Fecha de inicio vacio');
            this.fechainicio.focus();
            return false;
        }
        if (this.fechafin.value === '') {
            alert('Fecha fin vacio');
            this.fechafin.focus();
            return false;
        }

        return true;

    }


    /**
     * Método getDatosFormulario
     * 
     * Obtiene todos los datos(Ya validados!) del formulario.
     * 
     */
    getDatosFormulario() {

        if (this.validarForm()) {
            // Generar instancia de FormData
            const datos = new FormData();

            // Generar instancia de la clase Documento.
            const docu = new Documento(this.documento.files[0]);
            let docu_binario = docu.validarDocumento(['PDF', 'EPUB'], 30720);
            if (!docu_binario)
                docu_binario = '';

            let cadena_idpuesto = '';
            let cadena_vacancia = '';
            // Obtener detalle.
            const tabla = this.tabla;

            if (this.tabla.rows !== undefined) {

                if (this.tabla.rows.length > 0) {

                    // recorrer la tabla
                    for (let i = 1; i < this.tabla.rows.length; i++) {

                        // Concatenar cada valor con una coma.
                        cadena_idpuesto += tabla.rows[i].id + ',';
                        cadena_vacancia += tabla.rows[i].children[1].innerText + ',';

                    }

                }

            }

            // Limpieza de la última coma.
            cadena_idpuesto = cadena_idpuesto.slice(0, (cadena_idpuesto.length - 1));
            cadena_vacancia = cadena_vacancia.slice(0, (cadena_vacancia.length - 1));

            // Agregando al objeto datos.
            datos.append('idcomite', this.idcomite.value);
            datos.append('descripcion', this.descripcion.value.trim());
            datos.append('docu_binario', docu_binario);
            datos.append('idpuestos', cadena_idpuesto);
            datos.append('vacancias', cadena_vacancia);
            datos.append('fechainicio', this.fechainicio.value.trim());
            datos.append('fechafin', this.fechafin.value.trim());

            alert('Datos cargados exitosamente.. enviando formulario !');
            return datos;
        }
        return false;
    }


    /**
     * Método guardar.
     * 
     * Mediante AJAX, enviamos toda la información para su persistencia.
     * 
     */
    async guardar() {

        const datos = this.getDatosFormulario();

        if (datos !== false) {
            try {

                const res = await fetch('/membresia/formulario_postulacion/guardar_formulario', {
                    method: 'PUT',
                    body: datos
                });
                const data = await res.json();

                if (data.procesado === true) {
                    location.href = '/membresia/formulario_postulacion/';
                }

            } catch (error) {
                alert('Hubo un error en el servidor');
                console.error(error);
            }
        }
    }


    /**
     * Método reprogramar.
     * 
     * Se define la manera de enviar valores al servidor según postulación,
     * con la posibilidad de configurar nueva fecha de inicio y fin.
     * Opciones: dia, semana, mes, personalizado.
     * 
     * @param {string} opcion 
     * @param {int} idpostu 
     * @param {date} fechainicio 
     * @param {date} fechafin 
     */
    async reprogramar(opcion, idpostu, fechainicio = null, fechafin = null) {

        const datos = {
            opcion: opcion
            , idpostu: parseInt(idpostu)
            , fechainicio: fechainicio
            , fechafin: fechafin
        }
        try {

            const res = await fetch('/membresia/formulario_postulacion/reprogramar', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            });
            const data = await res.json();

            console.log(data);
            return data;

        } catch (error) {
            console.error(error);
        }

    }


    /**
     * Método validarFechas.
     * 
     * Se define las validaciones en cuanto a lógica con 
     * la fecha de inicio y la fecha de finalización
     * de la postulación.
     * 
     * @param {Date} fechainicio 
     * @param {Date} fechafin 
     * @returns {boolean} estado
     */
    validarFechas(fechainicio, fechafin) {

        if (fechainicio !== undefined && fechafin !== undefined && fechainicio.trim() !== '' && fechafin.trim() !== '') {

            const fechaHoy = new Date();
            const v_fechainicio = new Date(fechainicio);
            const v_fechafin = new Date(fechafin);
            const diafinicio = v_fechainicio.getDay();
            const diaffin = v_fechafin.getDay();

            if (v_fechainicio.getFullYear() < fechaHoy.getFullYear()) {
                alert('El año de la fecha de inicio esta desactualizado');
                return false;
            }

            if (v_fechafin.getFullYear() < fechaHoy.getFullYear()) {
                alert('El año de la fecha de finalizacion esta desactualizado');
                return false;
            }
            if (v_fechainicio.getDate() < fechaHoy.getDate()) {

                alert('La fechainicio es menor al actual');
                return false;

            } else if (v_fechainicio.getDate() > v_fechafin.getDate()) {

                alert('La fechainicio es mayor que la fechafin');
                return false;

            } else if (diafinicio === diaffin) {

                alert('La fecha de finalización no debe ser igual a la fecha de inicio');
                return false;

            } else if (v_fechafin.getDate() < fechaHoy.getDate()) {

                alert('La fechafin es menor a la fecha actual');
                return false;
            }

            return true;

        } else {
            console.error('No debe estar vacío fechainicio y fechafin');
            return false;
        }

    }


    async configurarFechas(idpostulacion, fechainicio, fechafin) {

        const res = this.validarFechas(fechainicio, fechafin);
        if (res === true) {
            
            try {
                
                const res = await this.reprogramar('personalizado', idpostulacion, fechainicio, fechafin);
                return res;

            } catch (error) {
                console.error(error);
            }

        }

    } 
}