import { end_principal } from '../helper/lista_endpoints.js';
import FormularioOficial from './FormularioOficial.js';

document.addEventListener('DOMContentLoaded', () => {

    // Generar instancia de la clase controladora.
    const ofi = new FormularioOficial();
    ofi.autocompletarMiembro();
    ofi.autoCompletarRequisitos();
    ofi.formatearFechas();

    // Manejar eventos.
    const botonFormAdmi = ofi.btnFormAdmi;
    botonFormAdmi.addEventListener('click', () => {
        ofi.abrirFormularioAdmision();
    });

    const botonGuardar = ofi.btnGuardar;
    botonGuardar.addEventListener('click', () => {

        const res = ofi.guardar();
        if (res === true) {
            setTimeout(() => {
                location.href = end_principal;
            }, 3000
            )
        }
    });

});