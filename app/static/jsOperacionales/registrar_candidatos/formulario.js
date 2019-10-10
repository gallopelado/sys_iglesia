import ListaCandidato from './ListaCandidato.js';

document.addEventListener('DOMContentLoaded', async() => {

    const candi = new ListaCandidato();
    const detalle_candi = await candi.traerDetalle();
    candi.cargarCandidatos();    
    candi.verificaRepetidos();

    // Eventos
    candi.txt_candidato.addEventListener('keypress', (e) => {

        if (e.key == 'Enter') {
            candi.agregarFila();
        }        

    });

    // Funciones globales
    window.eliminarFila = (b) => {
        const conf = confirm('Desea eliminar esta fila ?');
        if (conf)
            candi.tabla.deleteRow(b.rowIndex);

    } 

});