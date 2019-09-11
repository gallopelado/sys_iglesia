import Postulacion from './Postulacion.js';

document.addEventListener('DOMContentLoaded', () => {

    const frm = new Postulacion();
    frm.getMinisterios();
    frm.getProfesiones();

});