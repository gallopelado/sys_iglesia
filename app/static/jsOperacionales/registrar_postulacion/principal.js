import Postulacion from './Postulacion.js';

document.addEventListener('DOMContentLoaded', () => {

    const pos = new Postulacion();

    // Eventos
    // Boton cambiar para el modal personalizar.
    const btnCambiar = document.getElementById('btnCambiar');
    btnCambiar.addEventListener('click', () => {

        // Recuperar idpostulacion
        const idpostulacion = localStorage.getItem('idpostulacion');

        // Recuperar datos del modal.
        const txtfechainicio = document.getElementById('txt_fechainicio').value;
        const txtfechafin = document.getElementById('txt_fechafin').value;

        // Validar formulario
        if (txtfechainicio.trim() === '') {
            alert('No debe dejar espacios vacíos!');
            document.getElementById('txt_fechainicio').focus();            
            return;
        } 
        if (txtfechafin.trim() === ''){
            alert('No debe dejar espacios vacíos!');
            document.getElementById('txt_fechafin').focus();
            return;
        }

        // Enviar datos
        personalizarFechas(idpostulacion, txtfechainicio, txtfechafin);
            
        // Cerrar modal.
        $('#modalPersonalizar').modal('toggle');

    });

    // Funciones globales
    window.reprogramar = async (opcion, idpostulacion, fechainicio = null, fechafin = null) => {
        let resp;
        switch (opcion) {

            case 'dia':
                resp = confirm('Desea agregar 1 día ?');
                if (resp) {
                    let resp = await pos.reprogramar(opcion, idpostulacion);
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
                    let resp = await pos.reprogramar(opcion, idpostulacion);
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
                    let resp = await pos.reprogramar(opcion, idpostulacion);
                    if (resp.estado === true) {
                        location.href = '/membresia/formulario_postulacion';
                    } else {
                        console.error(resp);
                        alert('Hubo un error, favor contacte con el Administrador del Sistema');
                    }
                }
                break;
            case 'personalizado':
                //pos.validarFechas( '03-10-2019', '03-01-2019' );
                pos.fechainicio.value = '';
                pos.fechafin.value = '';
                pos.fechainicio.focus();
                // Iniciar el modal.
                pos.inicializarFechas();
                $('#modalPersonalizar').modal();
                // Enviar el idpostulacion.
                localStorage.setItem('idpostulacion', idpostulacion);
                // Recolectar las fechas.
                // Enviar datos al servidor.
                break;

        }

    }

    window.personalizarFechas = async (idpostulacion, fechainicio, fechafin) => {

        try {

            const res = await pos.configurarFechas(idpostulacion, fechainicio, fechafin);
            console.log(res);

        } catch (error) {
            console.error(error);
        }

    }
});

