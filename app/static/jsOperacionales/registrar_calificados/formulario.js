import ModalVer from './ModalVer.js';

document.addEventListener('DOMContentLoaded', () => {

    // Generar instancia del modal
    const mo = new ModalVer();

    window.verModal = (idperfil) => {

        if (idperfil !== '' || idperfil !== undefined) {
            mo.getPerfil(idperfil);
        } else {
            alert('Error al ver modal. Favor contacte con el Administrador');
            console.error(idperfil);
        }

    }

    window.guardarLista = async () => {

        let candidatos = '';
        let datos;
        const idpostulacion = document.getElementById('idpostulacion').value;
        const vacantes = document.getElementById('txt_vacantes').value;
        let contador = 0;
        const tb = document.getElementById('tb_detalle');
        if (tb.rows.length > 0) {

            for (let i = 0; i < tb.rows.length; i++) {
                if (tb.rows[i].children[2].children[0].children[0].checked === true) {
                    candidatos += `${tb.rows[i].id},`;
                    contador++;
                }
            }

            if (candidatos !== '' && contador <= vacantes) {

                candidatos = candidatos.slice(0, (candidatos.length - 1));
                datos = {
                    idpostulacion: idpostulacion,
                    candidatos: candidatos
                }                

                // Enviar por ajax
                const res = await fetch('/membresia/registrar_calificados/guardar_lista', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(datos)
                });

                const data = await res.json();

                if (data.estado === true) {
                    location.href = `/membresia/registrar_calificados/formulario/${idpostulacion}`;
                } else {
                    alert('Hubo un problema al guardar. Favor contacte con el administrador del sistema');
                    console.error(data);
                }
            } else {
                alert('No debe superar la cantidad de vacantes!!');
            }
        }

    }

    // Eventos
    const btnGuardar = document.getElementById('btnGuardar');
    if (btnGuardar !== undefined && btnGuardar !== '' && btnGuardar !== null) {
        btnGuardar.addEventListener('click', () => {

            guardarLista();

        });
    }
});