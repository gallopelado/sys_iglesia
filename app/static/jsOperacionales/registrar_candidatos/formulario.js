import ListaCandidato from './ListaCandidato.js';

document.addEventListener('DOMContentLoaded', async () => {

    const candi = new ListaCandidato();
    await candi.traerDetalle();
    await candi.cargarCandidatos();
    //candi.verificaRepetidos();

    // Eventos
    if (candi.txt_candidato !== null) {
        candi.txt_candidato.addEventListener('keypress', (e) => {

            if (e.key == 'Enter' && candi.txt_candidato.value.trim() !== '') {
                candi.agregarFila();
                candi.txt_candidato.value = '';
            }

        });
    }

    if (candi.btnGuardar !== null) {
        candi.btnGuardar.addEventListener('click', async () => {

            const res = await candi.guardarLista();
            if (res.estado === true) {
                alert('Se guardó con éxito');
                location.href = '/membresia/registrar_candidatos/';
            } else if (res.tipo === 'sin-candidato'){
                console.log(res);                
            } else {
                console.log(res);
                alert('Hubo un problema al intentar guardar. Favor contacte con el administrador del sistema');
            }

        });
    }

    // Funciones globales
    window.eliminarFila = (b) => {
        const conf = confirm('Desea eliminar esta fila ?');
        if (conf)
            candi.tabla.deleteRow(b.rowIndex);

    }


    window.eliminarRegistro = async (idpostulacion, idcandidato) => {
        const cf = confirm('Desea eliminar este registro ?');
        if (cf) {

            try {

                const res = await candi.eliminarCandidato(idpostulacion, idcandidato);

                if (res.estado === true) {
                    location.href = `/membresia/registrar_candidatos/asignar_candidatos/${idpostulacion}`;
                }

            } catch (error) {
                console.error(error);
            }

        }
    }

});