
import FormularioMiembroRequisito from './FormularioMiembroRequisito.js';

document.addEventListener('DOMContentLoaded', () => {

    const frm = new FormularioMiembroRequisito();
    //frm.obtenerRequisitos();
    frm.cargarInputs();
});

// Variables globales.
var lista = [];


// Eventos elementos.
const btnAgregar = document.getElementById('btnAgregaItem');
btnAgregar.addEventListener('click', () => {

    const frm = new FormularioMiembroRequisito();

    const tabla = document.getElementById('tb_requisitos');
    const tablaLongi = tabla.rows.length;
    console.log(tablaLongi);

    let fila;
    let celda1;
    let celda2;
    let celda3;
    let botonEliminar = `
    <button type="button" class="btn btn-danger btn-sm" onclick="eliminarFila()">
        <i class="fa fa-flash"></i> Eliminar
    </button>`;
    let noencontrado = false;

    if (frm.validarFormulario()) {

        const datos = frm.validarFormulario();
        fila = tabla.insertRow();

        //if (tablaLongi > 1) {

        // Recorrer la tabla.
        for (let i = 0; i < tabla.rows.length; i++) {

            if (tabla.rows[i].cells[0] !== undefined) {
                //console.log(tabla.rows[i].cells[0].innerHTML);
                if (tabla.rows[i].cells[0].innerHTML === datos.txt_requisito.trim()) {

                    alert('Repetido');
                    noencontrado = true;
                    return false;

                }

            } else {
                console.log('filas indefinidas');
            }

        }

        if (!noencontrado) {

            fila.id = datos.txt_idrequisito;
            celda1 = fila.insertCell(0);
            celda2 = fila.insertCell(1)
            celda3 = fila.insertCell(2);

            celda1.innerHTML = datos.txt_requisito;
            celda2.innerHTML = datos.txt_obs.toUpperCase();
            celda3.innerHTML = botonEliminar;

            frm.txt_requisito.value = '';
            frm.txt_obs.value = '';

        }

        /*} else {

            fila.id = datos.txt_idrequisito;
            celda1 = fila.insertCell(0);
            celda2 = fila.insertCell(1);
            celda3 = fila.insertCell(2);

            celda1.innerHTML = datos.txt_requisito;
            celda2.innerHTML = datos.txt_obs.toUpperCase();
            celda3.innerHTML = botonEliminar;

        }*/


    }

    // Agregar elementos a la tabla requisitos.

});

const btnGuardar = document.getElementById('btnGuardar');
btnGuardar.addEventListener('click', () => {
    console.log('Guardando...');
    const req = new FormularioMiembroRequisito();
    let correcto = req.guardar();
    if (correcto) {
        window.location.href = `/requisitos_miembro/frm_requisito/${req.idmiembro.value}`;
    }
});
// Funciones globales.
window.eliminarFila = () => {


    // Obtener datos de la tabla
    const tabla = document.getElementById('tabla_requisitos');
    const tablaLongi = tabla.rows.length;
    let indice;
    let idfila;
    const req = new FormularioMiembroRequisito();

    //console.log(tablaLongi);

    // Recorrer la tabla
    for (let i = 1; i < tablaLongi; i++) {

        // Ligar el evento click al boton dentro de la tabla.
        tabla.rows[i].cells[2].children[0].onclick = function () {

            // Obtener el indice de fila.                
            indice = this.parentElement.parentElement.rowIndex;
            //console.log(this.parentElement.parentElement.style.backgroundColor);
            const estiloFila = this.parentElement.parentElement.style.backgroundColor;
            //console.log(indice);
            if (estiloFila === 'rgb(241, 243, 232)') {

                const confirmacion = confirm('Este registro existe en la Base de Datos, desea eliminarlo?');
                if (confirmacion) {
                    idfila = this.parentElement.parentElement.id;
                    //console.log(this.parentElement.parentElement.id);
                    const res = req.eliminar(idfila);
                    if (res) {
                        window.location.href = `/requisitos_miembro/frm_requisito/${req.idmiembro.value}`;
                        alert('Eliminado id= ' + idfila);
                    }
                }
            } else {

                // Borrar fila
                tabla.deleteRow(indice);

            }

        }

    }

}