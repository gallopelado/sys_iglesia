import Postulacion from './Postulacion.js';

document.addEventListener('DOMContentLoaded', () => {

    const pos = new Postulacion();

    pos.validarFechas();
    // Funciones globales
    window.reprogramar = (opcion, idpostulacion, fechainicio = null, fechafin = null) => {
        let resp;
        switch (opcion) {

            case 'dia':
                resp = confirm('Desea agregar 1 día ?');
                if (resp) {
                    let resp = pos.reprogramar(opcion, idpostulacion);
                    if (resp.estado === true) {
                        location.href = '/membresia/formulario_postulacion';
                    } else {
                        console.error(resp);
                        alert('Hubo un error, favor contacte con el Administrador del Sistema');
                    }
                }
                break;
            case 'semana':
                resp = confirm('Desea agregar 1 semana ?');
                if (resp) {
                    let resp = pos.reprogramar(opcion, idpostulacion);
                    if (resp.estado === true) {
                        location.href = '/membresia/formulario_postulacion';
                    } else {
                        console.error(resp);
                        alert('Hubo un error, favor contacte con el Administrador del Sistema');
                    }
                }
                break;
            case 'mes':
                resp = confirm('Desea agregar 1 mes ?');
                if (resp) {
                    let resp = pos.reprogramar(opcion, idpostulacion);
                    if (resp.estado === true) {
                        location.href = '/membresia/formulario_postulacion';
                    } else {
                        console.error(resp);
                        alert('Hubo un error, favor contacte con el Administrador del Sistema');
                    }
                }
                break;
            case 'personalizado':
                alert('Abriendo modal');
                break;

        }

    }

});

