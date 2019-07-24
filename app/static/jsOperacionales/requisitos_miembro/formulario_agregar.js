
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

    const tabla = document.getElementById('tabla_requisitos');
    const tablaLongi = tabla.rows.length;
    
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

        if (tablaLongi > 1) {

            // Recorrer la tabla.
            for (let i = 1; i < tabla.rows.length; i++) {

                if (tabla.rows[i].cells[0] !== undefined) {

                    if (tabla.rows[i].cells[0].innerHTML === datos.txt_requisito.trim()) {

                        alert('Repetido');
                        noencontrado = true;
                        return false;

                    }

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

            }

        } else {

            celda1 = fila.insertCell(0);
            celda2 = fila.insertCell(1);

            celda1.innerHTML = datos.txt_requisito;
            celda2.innerHTML = botonEliminar;

        }


    }

    // Agregar elementos a la tabla requisitos.

});

const btnGuardar = document.getElementById('btnGuardar');
btnGuardar.addEventListener('click', () => {
    console.log('Guardando...');
    const req = new FormularioMiembroRequisito();
    req.guardar();
});
// Funciones globales.
window.eliminarFila = () => {


    // Obtener datos de la tabla
    const tabla = document.getElementById('tabla_requisitos');
    const tablaLongi = tabla.rows.length;
    let indice;    

    console.log(tablaLongi);

    // Recorrer la tabla
    for (let i = 1; i < tablaLongi; i++) {

        // Ligar el evento click al boton dentro de la tabla.
        tabla.rows[i].cells[2].children[0].onclick = function () {

            // Obtener el indice de fila.                
            indice = this.parentElement.parentElement.rowIndex;
            console.log(this.parentElement.parentElement);
            console.log(indice);

            // Borrar fila
            tabla.deleteRow(indice);            
            
            // Agregar para borrar
            //borrar.push()

        }

    }

}