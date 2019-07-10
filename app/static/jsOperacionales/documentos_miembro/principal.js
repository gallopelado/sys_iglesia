import { hacerDataTable, mensajeConfirmacion } from '../helper/helper.js';
import PrincipalUI from './PrincipalUI.js';

// Init
document.addEventListener('DOMContentLoaded', () => {
    const doc = new PrincipalUI();
    doc.cargarTabla();
    hacerDataTable('tabla_formdocu');
});

window.modificar = (idpersona, iddocumento) => {

    const conf = mensajeConfirmacion('Mensaje confirmación', 'Desea modificar este registro ?');
    conf.buttons.Si.action = () => {
        
        const doc = new PrincipalUI();
        doc.guardarTemporal(idpersona, iddocumento);               
        window.location.href = 'http://localhost:5000/documentos_miembro/frm_mod';

    }
    conf.open();

}

window.eliminar = (idpersona, iddocumento) => {

    const conf = mensajeConfirmacion('Mensaje confirmación', 'Desea eliminar este registro ?');
    conf.buttons.Si.action = () => {
        console.log('eliminando');
    }
    conf.open();

}