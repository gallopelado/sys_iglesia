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
        
        ofi.validarFormulario();
        
       
    });

});