import { end_carga_modificar, end_baja_miembrooficial } from '../helper/lista_endpoints.js';
import { autoCompletar, dateTimePicker4, mensajeConfirmacion, mensajeNormal } from '../helper/helper.js';
import ModalBaja from './ModalBaja.js';

document.addEventListener('DOMContentLoaded', () => {


    // Eventos a botones.
    const btnProceder = document.getElementById('btnProceder');
    btnProceder.addEventListener('click', () => {
        
        //Ejecutar la función de baja.
        procesarBajar();

    });

    /**
     * Función global modificar.
     * Se define un mensaje de confirmación para
     * la modificación del registro.
     * 
     * @param {integer} id
     * 
     */
    window.modificar = (id) => {
        const m = mensajeConfirmacion('Modficar ?', 'Desea modificar este registro ?');
        m.buttons.Si = () => {
            location.href = `${end_carga_modificar}/${id}`;
        };
        m.open();

    };


    /**
     * Función global baja.
     * Se define un mensaje de confirmación para
     * dar de baja un registro según opciones.
     * 
     * @param {integer} id
     * 
     */
    window.baja =  (id) => {

        const m = mensajeConfirmacion('Dar de baja? ?', 'Desea dar de baja este registro ?');
        m.buttons.Si = async() => {

            // instaciar la clase ModalBaja,
            // obtener el nombre del miembro.
            const mb = new ModalBaja();
            const datos = await mb.obtenerDatos(id);        

            // Asignar en el formulario.
            mb.idpersona.value = datos.encontrado[0];
            mb.txt_persona.value = datos.encontrado[1];

            // Mostrar mensaje.
            $('#modal_baja').modal('toggle');

        };
        m.open();

    };

    const procesarBajar = async () => {
        try {

            
            // instaciar la clase ModalBaja,
            // obtener el nombre del miembro.
            const mb = new ModalBaja();
            const res = await mb.eliminar();
            console.log(res);

        } catch (error) {
            console.error(error);
        }
    }    

});
