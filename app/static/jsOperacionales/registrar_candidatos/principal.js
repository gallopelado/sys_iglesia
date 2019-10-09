import ListaCandidato from './ListaCandidato.js';

document.addEventListener('DOMContentLoaded', () => {

    // Generar instancia.
    const cand = new ListaCandidato();
    cand.cargarTabla('ABIERTA');

    window.cargarTabla = (opcion) => {
        
        cand.cargarTabla(opcion);

    }

});