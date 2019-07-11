import { mensajeNormal, mensajeConfirmacion } from '../helper/helper.js';
import PrincipalUI from './PrincipalUI.js';
import ModalVer from './ModalVer.js';

// Init
document.addEventListener('DOMContentLoaded', () => {

    const doc = new PrincipalUI();
    doc.cargarTabla();

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

        const doc = new PrincipalUI();
        const res = doc.eliminarFormulario(idpersona, iddocumento);

        if (res) {
            const m = mensajeNormal('Exito', 'Se ha dado de baja con éxito');
            m.open();
        } else {
            console.error('Paso algo !');
        }

    }
    conf.open();

}

window.ver = (idpersona, iddocumento) => {
    const m = new ModalVer();
    m.mostrarModal();
    m.setearFormulario(idpersona, iddocumento);
}


