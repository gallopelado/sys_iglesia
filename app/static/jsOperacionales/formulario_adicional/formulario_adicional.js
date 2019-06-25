document.addEventListener('DOMContentLoaded', () => {
    let adi = new FormAdicionalUI();
    adi.cargarComboProfesion();
});

// Eventos para botones.
var btnAgregarTabla = document.getElementById('btnAgregarDatos');
btnAgregarTabla.addEventListener('click', () => {

    let adi = new FormAdicionalUI();
    adi.agregarProfesiones();

});

var btnAgregarProfesion = document.getElementById('btnAgregarProfesion');
btnAgregarProfesion.addEventListener('click', () => {

    let modal = new ModalProfesion();

    // Generar una instancia de jqueryconfirm.
    let c = mensajeConfirmacion('Mensaje de confirmación', 'Desea agregar una nueva profesión/oficio?');
    c.buttons.Si.action = () => modal.mostrar();
    c.open();

});

// Funciones
function eliminarFila() {
    let adi = new FormAdicionalUI();
    adi.eliminarFila();
}

class FormAdicionalUI {

    constructor() {

        this.idpersona = document.getElementById('idpersona');
        this.idnacionlidad = document.getElementById('cbo_nacionalidad');
        this.lugarnacimiento = document.getElementById('txt_lugarnac');
        this.alergia = document.getElementById('txt_alergia');
        this.tiposangre = document.getElementById('cbo_tiposangre');
        this.capacidades = document.getElementById('txt_capacidades');
        this.foto = document.getElementById('txt_foto')
        this.idprofesion = document.getElementById('cbo_profesion');
        this.puesto = document.getElementById('txt_puesto');
        this.lugartrabajo = document.getElementById('txt_lugartrabajo');

    }

    agregarProfesiones() {

        let fila, celda0, celda1, celda2, celda3, celda4, tabla = document.getElementById('tabla_profesiones'),
            boton = `<button type='button' class='btn btn-outline-danger btn-sm btn-block' onclick='eliminarFila()'><i class='fa fa-minus-square'></i> Eliminar</button>`;



        // Se buscar cual es la opcion que ha sido seleccionada.
        // Siendo asi, se recuper id, nombre de profesion para la tabla.
        for (let i = 0; i < this.idprofesion.length; i++) {

            if (this.idprofesion.value !== "" && this.puesto.value.trim() !== "" && this.lugartrabajo.value.trim() !== "") {

                if (this.idprofesion.children[i].selected === true) {
                    //console.log(`Seleccionado id:${this.idprofesion.children[i].id} es ${this.idprofesion.children[i].value}`);                   

                    if (this.controlarRepetidos() !== true) {

                        // Crear filas.
                        fila = tabla.insertRow();

                        // Crear celdas.
                        celda0 = fila.insertCell(0);
                        celda1 = fila.insertCell(1);
                        celda2 = fila.insertCell(2);
                        celda3 = fila.insertCell(3);
                        celda4 = fila.insertCell(4);

                        // Asignar variables
                        let idprofesion = "", descriprofesion = "", puesto = "", lugartrabajo = "";
                        idprofesion = this.idprofesion.children[i].id;
                        descriprofesion = this.idprofesion.children[i].value;
                        puesto = this.puesto.value.trim();
                        puesto = puesto.toUpperCase();
                        lugartrabajo = this.lugartrabajo.value.trim();
                        lugartrabajo = lugartrabajo.toUpperCase();

                        // Se agrega contenido a la tabla.
                        celda0.innerHTML = idprofesion;
                        celda1.innerHTML = descriprofesion;
                        celda2.innerHTML = puesto;
                        celda3.innerHTML = lugartrabajo;
                        celda4.innerHTML = boton;

                        // limpiar campos
                        this.idprofesion.value = "";
                        this.puesto.value = "";
                        this.lugartrabajo.value = "";
                        camposNoValidos(false);
                        break;

                    } else {
                        alert('Hay campos repetidos.');
                        camposNoValidos(true);
                        break;
                    }

                }
            } else {
                alert('No se permiten campos vacíos.');
                camposNoValidos(true);
                break;
            }

        }

    }

    controlarRepetidos() {

        // Capturar datos
        let tabla = document.getElementById('tabla_profesiones'), descriprofesion = "", puesto = "", lugartrabajo = "";
        descriprofesion = this.idprofesion.value;
        puesto = this.puesto.value.trim();
        puesto = puesto.toUpperCase();
        lugartrabajo = this.lugartrabajo.value.trim();
        lugartrabajo = lugartrabajo.toUpperCase();

        for (let i = 1; i < tabla.rows.length; i++) {

            if (tabla.rows[i].cells[1].innerHTML === descriprofesion && tabla.rows[i].cells[2].innerHTML === puesto && tabla.rows[i].cells[3].innerHTML === lugartrabajo) {
                return true;
            }

        }

        return false;

    }

    eliminarFila() {

        let fila, tabla = document.getElementById('tabla_profesiones');

        for (let i = 1; i < tabla.rows.length; i++) {

            console.log(tabla.rows[i].cells[4].children[0].parentElement.parentElement.rowIndex);

            tabla.rows[i].cells[4].children[0].onclick = function () {

                // El this indica lo que hay en tabla.rows[i].cells[4].children[0]
                console.log(this.parentElement.parentElement.rowIndex);
                // Se obtiene el indice del tr, el indice fila.
                fila = this.parentElement.parentElement.rowIndex;

                // Se borra la fila.
                tabla.deleteRow(fila);

            }

        }

    }

    async comboProfesion() {

        try {

            const res = await fetch('http://localhost:5000/profesion/listar_profesiones');
            const data = await res.json();
            
            return data;

        } catch (error) {
            console.error(error);
            return false;
        }
    }

    async cargarComboProfesion() {

        let select = document.getElementById('cbo_profesion'),
            option, profesiones = await this.comboProfesion();

        for (let i = 0; i < profesiones.length; i++) {

            option = document.createElement('option');
            option.text = profesiones[i][1];
            option.value = profesiones[i][1]
            option.id = profesiones[i][0];
            select.add(option);

        }

    }

}

function camposNoValidos(estado) {

    let adi = new FormAdicionalUI();

    if (estado === true) {
        adi.puesto.className = "is-invalid form-control form-control-sm";
        adi.lugartrabajo.className = "is-invalid form-control form-control-sm";
        adi.puesto.focus();
    } else {
        adi.puesto.className = "form-control form-control-sm";
        adi.lugartrabajo.className = "form-control form-control-sm";
    }

}