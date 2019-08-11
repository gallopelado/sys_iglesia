import { end_carga_modificar, end_principal_miembrooficial } from '../helper/lista_endpoints.js';
import { autoCompletar, dateTimePicker4, mensajeConfirmacion, mensajeNormal } from '../helper/helper.js';

document.addEventListener('DOMContentLoaded', () => {

    console.log('cargado');
    window.modificar = (id) => {
        const m = mensajeConfirmacion('Modficar ?', 'Desea modificar este registro ?');
        m.buttons.Si = () => {
            location.href = `${end_carga_modificar}/${id}`;
        };
        m.open();
        
    };

});
