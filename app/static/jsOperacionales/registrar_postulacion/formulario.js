import Postulacion from './Postulacion.js';
import { dateTimePicker4 } from '../helper/helper.js';

var lugares = 0;
document.addEventListener('DOMContentLoaded', () => {

    const frm = new Postulacion();

    // Campos de autocompletado.
    frm.getMinisterios();
    frm.getProfesiones();

    // Campos con datetimepicker
    frm.inicializarFechas();

    // Capturar evento keypress del campo vacancas.
    // Nodo vacancias.
    const txtVacancias = document.getElementById('txt_vacancias');

    
    txtVacancias.addEventListener('keypress', (e) => {

        if (e.code === 'Enter' || e.code === 'NumpadEnter') {

            // Variables a usar.
            // Tabla, tbody.
            const tbody = document.getElementById('tb_detalle');
            const tablaLongi = tbody.length;
            let fila;
            let celda1;
            let celda2;
            let celda3;
            let botonEliminar = `
        <button type="button" class="btn btn-danger btn-sm" onclick="eliminarFila()">
            <i class="fa fa-flash"></i> Eliminar
        </button>`;
            let noencontrado = false;

            // Validacion del campo puesto y su id, vacancias.
            const v_idpuesto = frm.idpuesto.value.trim();
            const v_puesto = frm.puesto.value.trim();
            const vacancias = txtVacancias.value.trim();

            if (v_puesto !== '' && v_idpuesto !== '' && vacancias !== '') {
                fila = tbody.insertRow(tablaLongi);

                for (let i = 0; i < tbody.rows.length; i++) {

                    if (tbody.rows[i].cells[0] !== undefined) {

                        if (tbody.rows[i].cells[0].innerHTML === v_puesto) {

                            alert('Repetido');
                            noencontrado = true;
                            return false;

                        }

                    } else {
                        console.log('Filas indefinidas');
                    }

                }

                if (!noencontrado) {

                    fila.id = v_idpuesto;
                    celda1 = fila.insertCell(0);
                    celda2 = fila.insertCell(1);
                    celda3 = fila.insertCell(2);

                    celda1.innerHTML = v_puesto;
                    celda2.innerHTML = vacancias;
                    celda3.innerHTML = botonEliminar;

                    lugares = parseInt(lugares) + parseInt(vacancias);
                    frm.lugaresdisponibles.value = lugares;
                    frm.idpuesto.value = '';
                    frm.puesto.value = '';
                    txtVacancias.value = '';

                }
            } else {
                alert('No debe estar vacios puesto y vacancias!');
            }
            //
        }
    });

}); // Fin de DOMContentLoaded

// Funciones globales.
window.eliminarFila = () => {

    // Obtener datos de la tabla.
    const tabla = document.getElementById('tabla_detalle');
    const tablaLongi = tabla.rows.length;
    let indice;
    let idfila;

    // Recorrer tabla
    for (let i = 1; i < tablaLongi; i++) {

        // Ligar evento click al boton dentro de la tabla.
        tabla.rows[i].cells[2].children[0].onclick = () => {

            if (tabla.rows[i] !== undefined) {
                const boton = tabla.rows[i].cells[2].children[0];
                // Obtener el indice de la fila.
                indice = boton.parentElement.parentElement.rowIndex;

                const confirmacion = confirm('Desea eliminarlo?');
                if (confirmacion) {

                    let res = document.getElementById('txt_lugares').value;
                    lugares = lugares - parseInt(tabla.rows[i].cells[1].innerHTML);
                    res = parseInt(res) - parseInt(tabla.rows[i].cells[1].innerHTML);
                    
                    document.getElementById('txt_lugares').value = res;
                    tabla.deleteRow(indice);
                }
            } else {
                console.log('problemas con tabla indefinida');
                console.log(tabla.rows[i]);
            }
        }

    }

}